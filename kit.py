#!/usr/bin/env python3
"""
Ultimate Agentic StarterKit: Automated Project Builder
Transforms project overviews into executable code through multi-agent coordination.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from agents.parser import ParserAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.advisor import AdvisorAgent
from agents.orchestrator import OrchestratorAgent
from utils.docker_manager import DockerManager
from utils.alert_system import AlertSystem
from utils.git_manager import GitManager


class StarterKit:
    """
    Main StarterKit class that orchestrates the entire project build process.
    
    Flow:
    1. Parse project overview (MD/PDF) → Extract milestones/PRPs as JSON
    2. Decompose into small tasks
    3. Agent execution: Assign/implement/test/advise
    4. Merge/Track: Chain outputs, alert on complete/blocker
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the StarterKit with configuration.
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.config = self._load_config(config_path)
        self.docker_manager = DockerManager()
        self.alert_system = AlertSystem()
        self.git_manager = GitManager()
        
        # Initialize agents
        self.parser_agent = ParserAgent(self.config)
        self.coder_agent = CoderAgent(self.config)
        self.tester_agent = TesterAgent(self.config)
        self.advisor_agent = AdvisorAgent(self.config)
        self.orchestrator = OrchestratorAgent(self.config)
        
        # Track project state
        self.project_state = {
            'milestones': [],
            'tasks': [],
            'completed_tasks': [],
            'failed_tasks': [],
            'current_iteration': 0,
            'max_iterations': 3
        }
    
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load configuration from file or use defaults."""
        default_config = {
            'ollama_model': 'llama3',
            'max_retries': 3,
            'output_dir': './output',
            'docker_services': ['ollama', 'n8n', 'openproject'],
            'git_auto_commit': True,
            'alert_methods': ['print', 'github_issue'],
            'confidence_threshold': 0.8
        }
        
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            default_config.update(user_config)
        
        return default_config
    
    def run(self, project_overview_path: str) -> bool:
        """
        Main execution flow for the StarterKit.
        
        Args:
            project_overview_path: Path to project overview MD/PDF file
            
        Returns:
            bool: True if successful, False if failed
        """
        try:
            print(f"🚀 Starting Ultimate Agentic StarterKit for: {project_overview_path}")
            
            # Phase 1: Parse project overview
            print("\n📋 Phase 1: Parsing project overview...")
            milestones, prps = self.parser_agent.parse_project_overview(project_overview_path)
            self.project_state['milestones'] = milestones
            
            if not milestones:
                self.alert_system.send_alert("CRITICAL", "No milestones extracted from project overview")
                return False
            
            # Phase 2: Decompose into tasks
            print("\n🔨 Phase 2: Decomposing into executable tasks...")
            tasks = self.orchestrator.decompose_milestones(milestones, prps)
            self.project_state['tasks'] = tasks
            
            # Phase 3: Execute tasks with agents
            print("\n⚙️  Phase 3: Executing tasks with multi-agent system...")
            success = self._execute_tasks(tasks)
            
            # Phase 4: Final review and merge
            print("\n🔍 Phase 4: Final review and project merge...")
            if success:
                self._finalize_project()
                print("✅ Project build completed successfully!")
                return True
            else:
                self.alert_system.send_alert("ERROR", "Project build failed after max retries")
                return False
                
        except Exception as e:
            self.alert_system.send_alert("CRITICAL", f"StarterKit execution failed: {str(e)}")
            return False
    
    def _execute_tasks(self, tasks: List[Dict]) -> bool:
        """
        Execute tasks using the multi-agent system with retry logic.
        
        Args:
            tasks: List of task dictionaries
            
        Returns:
            bool: True if all tasks completed successfully
        """
        for task in tasks:
            success = False
            iteration = 0
            
            while not success and iteration < self.config['max_iterations']:
                iteration += 1
                print(f"\n📝 Executing task: {task['title']} (Iteration {iteration})")
                
                # Step 1: Code implementation
                code_result = self.coder_agent.implement_task(task)
                
                if not code_result['success']:
                    print(f"❌ Code implementation failed: {code_result['error']}")
                    continue
                
                # Step 2: Test implementation
                test_result = self.tester_agent.test_implementation(code_result['output'])
                
                if not test_result['success']:
                    print(f"❌ Tests failed: {test_result['error']}")
                    # Get advisor input for improvement
                    advice = self.advisor_agent.analyze_failure(task, code_result, test_result)
                    task['advice'] = advice
                    continue
                
                # Step 3: Advisor review
                review_result = self.advisor_agent.review_implementation(
                    task, code_result, test_result
                )
                
                if review_result['confidence'] >= self.config['confidence_threshold']:
                    print(f"✅ Task completed successfully (Confidence: {review_result['confidence']})")
                    self.project_state['completed_tasks'].append(task)
                    success = True
                else:
                    print(f"⚠️  Low confidence ({review_result['confidence']}), needs improvement")
                    task['advice'] = review_result['recommendations']
            
            if not success:
                print(f"❌ Task failed after {self.config['max_iterations']} iterations")
                self.project_state['failed_tasks'].append(task)
                self.alert_system.send_alert("ERROR", f"Task failed: {task['title']}")
        
        # Check if critical tasks failed
        failed_critical = [t for t in self.project_state['failed_tasks'] if t.get('critical', False)]
        if failed_critical:
            return False
        
        return len(self.project_state['failed_tasks']) == 0
    
    def _finalize_project(self):
        """Finalize the project by merging outputs and creating documentation."""
        print("🔄 Finalizing project...")
        
        # Merge all code outputs
        self.orchestrator.merge_outputs(self.project_state['completed_tasks'])
        
        # Generate project documentation
        self.orchestrator.generate_documentation(self.project_state)
        
        # Commit to git if enabled
        if self.config['git_auto_commit']:
            self.git_manager.commit_changes("🤖 Generated project with Ultimate Agentic StarterKit")
        
        # Send completion alert
        self.alert_system.send_alert("SUCCESS", "Project build completed successfully!")
    
    def setup_environment(self):
        """Set up the development environment with Docker services."""
        print("🐳 Setting up Docker environment...")
        
        # Start required Docker services
        services = self.config['docker_services']
        for service in services:
            if not self.docker_manager.start_service(service):
                self.alert_system.send_alert("WARNING", f"Failed to start {service}")
        
        # Wait for services to be ready
        self.docker_manager.wait_for_services(services)
        print("✅ Environment setup complete!")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Ultimate Agentic StarterKit')
    parser.add_argument('--overview', '-o', required=True, 
                       help='Path to project overview MD/PDF file')
    parser.add_argument('--config', '-c', 
                       help='Path to configuration file')
    parser.add_argument('--setup-env', action='store_true',
                       help='Set up Docker environment before running')
    
    args = parser.parse_args()
    
    # Initialize StarterKit
    kit = StarterKit(config_path=args.config)
    
    # Setup environment if requested
    if args.setup_env:
        kit.setup_environment()
    
    # Run the main process
    success = kit.run(args.overview)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()