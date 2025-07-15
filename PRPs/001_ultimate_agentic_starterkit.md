name: "Ultimate Agentic StarterKit: Automated Project Builder"
description: |
  Complete implementation of an agentic factory that transforms project overviews into executable code through multi-agent coordination.

## Goal
Build an Ultimate Agentic StarterKit that automates the entire project build process. Input: Project overview MD/PDF files. Output: Working code with milestone reports and automated testing. The system should use multi-agent coordination (Parser, Coder, Tester, Advisor) to decompose specifications, implement code in small chunks, test iteratively, and provide human alerts on milestones/blockers.

## Why
- **Accelerate Development**: Transform project specifications into working code automatically
- **Reduce Human Error**: Systematic approach with validation loops and testing
- **Enable Rapid Prototyping**: Quick MVP generation from project overviews
- **Standardize Workflows**: Consistent approach to project implementation
- **Support ADO Ecosystem**: Build foundation for multi-project parallel development

## What
A comprehensive agentic factory system that:
- Parses project overviews (MD/PDF) and extracts milestones/PRPs as JSON
- Uses multi-agent system (Parser, Coder, Tester, Advisor) for collaborative development
- Implements iterative development with 3-retry loops and >80% confidence threshold
- Provides Docker-based environment with Ollama, n8n, OpenProject
- Generates working code with comprehensive testing and validation
- Integrates with Git for version control and project tracking
- Sends alerts on completion/blockers via print or GitHub API

### Success Criteria
- [ ] Successfully parses project overviews and extracts structured milestones
- [ ] Multi-agent system collaborates effectively to implement features
- [ ] Code generation with automated testing and validation loops
- [ ] Docker environment setup with all required services
- [ ] Git integration for version control and change tracking
- [ ] Alert system functional for milestone/blocker notifications
- [ ] All validation gates pass (syntax, tests, integration)
- [ ] README.md updated with comprehensive usage instructions

## All Needed Context

### Documentation & References
```yaml
# Core Technologies - MUST READ
- url: https://docs.crewai.com/en/concepts/agents
  why: CrewAI agent creation patterns, role definitions, collaboration framework
  critical: Agent initialization, role assignment, task delegation

- url: https://github.com/ollama/ollama-python
  why: Ollama Python integration, local LLM management, API usage patterns
  critical: Local LLM setup, model management, API integration

- url: https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/
  why: LlamaIndex query engines, document parsing, milestone extraction
  critical: Document processing, query engine setup, JSON extraction

- url: https://docs.n8n.io/workflows/components/nodes/
  why: n8n workflow automation, HTTP nodes, JavaScript integration
  critical: Workflow chaining, agent coordination, automation patterns

# Existing Project Context
- file: /home/ubuntu/alphadataomega/CLAUDE.md
  why: Project rules, development standards, testing requirements
  critical: 500-line file limits, pytest patterns, virtual environment usage

- file: /home/ubuntu/alphadataomega/docs/CONTEXT.md
  why: Project assumptions, technology stack, development preferences
  critical: Python/FastAPI patterns, modular architecture, documentation standards

- file: /home/ubuntu/alphadataomega/docs/PLANNING.md
  why: Project architecture, development roadmap, phase alignment
  critical: Multi-project coordination, parallel development strategy

- file: /home/ubuntu/alphadataomega/testing/scripts/visual-test.js
  why: Visual testing patterns, validation approaches, automated testing
  critical: Test automation, validation loops, error handling

- file: /home/ubuntu/alphadataomega/testing/scripts/prp-visual-validator.js
  why: PRP validation patterns, iterative testing, confidence scoring
  critical: Validation frameworks, success criteria, report generation

- file: /home/ubuntu/alphadataomega/agents/parser.py
  why: Existing parser implementation, LlamaIndex patterns, document processing
  critical: Document parsing, milestone extraction, error handling patterns

- file: /home/ubuntu/alphadataomega/kit.py
  why: Main orchestration patterns, agent coordination, configuration management
  critical: Agent initialization, workflow orchestration, error handling
```

### Current Codebase Tree
```bash
alphadataomega/
├── .claude/
│   └── commands/
│       ├── generate-prp.md
│       ├── execute-prp.md
│       ├── generate-plan.md
│       └── learn.md
├── agents/
│   ├── __init__.py
│   └── parser.py
├── docs/
│   ├── CONTEXT.md
│   ├── PLANNING.md
│   └── VISUAL_TESTING.md
├── PRPs/
│   └── templates/
│       └── prp_base.md
├── testing/
│   ├── scripts/
│   │   ├── visual-test.js
│   │   └── prp-visual-validator.js
│   └── screenshots/
├── work-orders/
│   └── 001_INITIAL.md
├── CLAUDE.md
├── README.md
├── kit.py
└── package.json
```

### Desired Codebase Tree with Files to be Added
```bash
alphadataomega/
├── agents/
│   ├── __init__.py
│   ├── parser.py (exists)
│   ├── coder.py (NEW - code generation agent)
│   ├── tester.py (NEW - testing validation agent)
│   ├── advisor.py (NEW - code review agent)
│   └── orchestrator.py (NEW - workflow coordination)
├── utils/
│   ├── __init__.py (NEW)
│   ├── docker_manager.py (NEW - Docker service management)
│   ├── alert_system.py (NEW - alert/notification system)
│   └── git_manager.py (NEW - Git integration)
├── config/
│   ├── __init__.py (NEW)
│   └── default_config.json (NEW - default configuration)
├── examples/
│   ├── parser.py (NEW - example parser implementation)
│   ├── coder.py (NEW - example code generation)
│   ├── tester.py (NEW - example testing patterns)
│   ├── advisor.py (NEW - example code review)
│   └── workflow.json (NEW - n8n workflow example)
├── docker/
│   ├── docker-compose.yml (NEW - service orchestration)
│   └── ollama.dockerfile (NEW - Ollama service)
├── tests/
│   ├── __init__.py (NEW)
│   ├── test_parser.py (NEW)
│   ├── test_coder.py (NEW)
│   ├── test_tester.py (NEW)
│   ├── test_advisor.py (NEW)
│   ├── test_orchestrator.py (NEW)
│   └── test_integration.py (NEW)
├── requirements.txt (NEW)
└── setup.py (NEW)
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: CrewAI requires specific initialization patterns
# CrewAI agents need role, goal, and backstory defined
# Must use @agent decorator for proper initialization

# CRITICAL: Ollama requires service to be running
# ollama.run() blocks until model is loaded
# Local models need to be pulled before use: ollama.pull('llama3')

# CRITICAL: LlamaIndex requires proper document chunking
# Large documents need chunking to avoid memory issues
# VectorStoreIndex requires embedding model configuration

# CRITICAL: n8n requires Docker service running
# HTTP nodes need proper authentication setup
# JavaScript functions have limited npm package access

# CRITICAL: Our project requirements
# - Maximum 500 lines per file (split into modules)
# - Use venv_linux for all Python commands
# - Follow PEP8 with type hints and Google docstrings
# - Create pytest unit tests for all new features
# - Update README.md with new features

# CRITICAL: Docker integration challenges
# - Container startup order matters (Ollama before agents)
# - Network configuration for inter-container communication
# - Volume mounts for persistent data and model storage
```

## Implementation Blueprint

### Data Models and Structure
```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class MilestoneData(BaseModel):
    title: str
    timeline: str
    description: str
    deliverables: List[str]
    success_metrics: List[str]
    dependencies: List[str]
    priority: str = "medium"

class PRPData(BaseModel):
    name: str
    type: str
    description: str
    acceptance_criteria: List[str]
    priority: str = "medium"
    complexity: int = Field(ge=1, le=10)
    category: str

class TaskData(BaseModel):
    id: str
    title: str
    description: str
    status: TaskStatus
    priority: str
    iteration: int = 0
    max_iterations: int = 3
    confidence: float = 0.0
    advice: Optional[str] = None
    code_output: Optional[str] = None
    test_results: Optional[Dict] = None

class ProjectState(BaseModel):
    milestones: List[MilestoneData]
    prps: List[PRPData]
    tasks: List[TaskData]
    completed_tasks: List[TaskData]
    failed_tasks: List[TaskData]
    current_iteration: int = 0
    confidence_threshold: float = 0.8
```

### Task List (Implementation Order)

```yaml
Task 1: Create Core Agent Infrastructure
MODIFY agents/__init__.py:
  - ADD imports for new agent classes
  - ENSURE proper module structure

CREATE agents/coder.py:
  - IMPLEMENT CoderAgent class with CrewAI integration
  - ADD task implementation methods
  - INCLUDE retry logic and error handling

CREATE agents/tester.py:
  - IMPLEMENT TesterAgent class
  - ADD subprocess-based test execution
  - INCLUDE result parsing and error reporting

CREATE agents/advisor.py:
  - IMPLEMENT AdvisorAgent class
  - ADD code review and improvement suggestions
  - INCLUDE confidence scoring mechanisms

CREATE agents/orchestrator.py:
  - IMPLEMENT OrchestratorAgent class
  - ADD workflow coordination logic
  - INCLUDE task decomposition and assignment

Task 2: Create Utility Systems
CREATE utils/__init__.py:
  - SETUP utility module structure

CREATE utils/docker_manager.py:
  - IMPLEMENT DockerManager class
  - ADD service startup/shutdown methods
  - INCLUDE health checking and monitoring

CREATE utils/alert_system.py:
  - IMPLEMENT AlertSystem class
  - ADD print and GitHub API alert methods
  - INCLUDE alert formatting and routing

CREATE utils/git_manager.py:
  - IMPLEMENT GitManager class
  - ADD commit, branch, and merge operations
  - INCLUDE conflict resolution helpers

Task 3: Configuration and Environment
CREATE config/__init__.py:
  - SETUP configuration module

CREATE config/default_config.json:
  - DEFINE default configuration values
  - INCLUDE service endpoints and timeouts
  - ADD agent-specific settings

CREATE docker/docker-compose.yml:
  - DEFINE service orchestration
  - INCLUDE Ollama, n8n, OpenProject services
  - ADD network and volume configurations

CREATE requirements.txt:
  - LIST all Python dependencies
  - INCLUDE version constraints
  - ADD development dependencies

Task 4: Example Implementations
CREATE examples/parser.py:
  - IMPLEMENT example milestone extraction
  - SHOW LlamaIndex usage patterns
  - DEMONSTRATE JSON output formatting

CREATE examples/coder.py:
  - IMPLEMENT example code generation
  - SHOW CrewAI agent usage
  - DEMONSTRATE output formatting

CREATE examples/tester.py:
  - IMPLEMENT example test execution
  - SHOW subprocess usage patterns
  - DEMONSTRATE error handling

CREATE examples/advisor.py:
  - IMPLEMENT example code review
  - SHOW improvement suggestions
  - DEMONSTRATE confidence scoring

CREATE examples/workflow.json:
  - DEFINE n8n workflow structure
  - SHOW agent chaining patterns
  - DEMONSTRATE HTTP node usage

Task 5: Testing Infrastructure
CREATE tests/__init__.py:
  - SETUP test module structure

CREATE tests/test_parser.py:
  - IMPLEMENT unit tests for ParserAgent
  - TEST milestone extraction functionality
  - VALIDATE error handling

CREATE tests/test_coder.py:
  - IMPLEMENT unit tests for CoderAgent
  - TEST code generation functionality
  - VALIDATE retry mechanisms

CREATE tests/test_tester.py:
  - IMPLEMENT unit tests for TesterAgent
  - TEST subprocess execution
  - VALIDATE result parsing

CREATE tests/test_advisor.py:
  - IMPLEMENT unit tests for AdvisorAgent
  - TEST code review functionality
  - VALIDATE confidence scoring

CREATE tests/test_orchestrator.py:
  - IMPLEMENT unit tests for OrchestratorAgent
  - TEST workflow coordination
  - VALIDATE task management

CREATE tests/test_integration.py:
  - IMPLEMENT integration tests
  - TEST full workflow execution
  - VALIDATE Docker integration

Task 6: Documentation Updates
MODIFY README.md:
  - ADD Ultimate Agentic StarterKit section
  - INCLUDE setup and usage instructions
  - ADD example workflows
  - DOCUMENT configuration options
  - INCLUDE troubleshooting guide

CREATE setup.py:
  - DEFINE package metadata
  - INCLUDE entry points
  - ADD dependencies

Task 7: Final Integration and Polish
MODIFY kit.py:
  - ENHANCE with new agent integration
  - ADD configuration loading
  - IMPROVE error handling
  - VALIDATE all functionality

Task 8: Validation and Testing
RUN all validation gates:
  - Execute syntax and style checks
  - Run complete test suite
  - Validate Docker integration
  - Test end-to-end workflows
```

### Per Task Pseudocode

```python
# Task 1: CoderAgent Implementation
class CoderAgent:
    def __init__(self, config: Dict):
        # PATTERN: Use CrewAI agent initialization
        self.agent = Agent(
            role="Senior Python Developer",
            goal="Generate high-quality, tested code from specifications",
            backstory="Expert in Python, FastAPI, and test-driven development",
            tools=[PythonCodeTool(), TestGeneratorTool()],
            llm=Ollama(model=config['ollama_model'])
        )
        
    def implement_task(self, task: TaskData) -> Dict:
        # CRITICAL: Follow 3-retry pattern with confidence scoring
        for attempt in range(task.max_iterations):
            try:
                # PATTERN: Use CrewAI task execution
                result = self.agent.execute_task(
                    description=task.description,
                    context=task.context,
                    expected_output="Python code with docstrings and type hints"
                )
                
                # GOTCHA: Validate code syntax before returning
                if self._validate_syntax(result.code):
                    return {
                        'success': True,
                        'code': result.code,
                        'confidence': result.confidence,
                        'attempt': attempt + 1
                    }
                    
            except Exception as e:
                # PATTERN: Log errors and continue retrying
                logger.error(f"Code generation failed: {str(e)}")
                
        return {'success': False, 'error': 'Max retries exceeded'}

# Task 2: TesterAgent Implementation  
class TesterAgent:
    def test_implementation(self, code: str) -> Dict:
        # CRITICAL: Use subprocess for test execution
        # PATTERN: Create temporary test file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py') as f:
            f.write(code)
            f.flush()
            
            # GOTCHA: Use venv_linux for Python commands
            result = subprocess.run([
                'venv_linux/bin/python', '-m', 'pytest', 
                f.name, '-v', '--tb=short'
            ], capture_output=True, text=True, timeout=30)
            
            return {
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'tests_passed': self._parse_test_results(result.stdout)
            }

# Task 3: DockerManager Implementation
class DockerManager:
    def start_service(self, service_name: str) -> bool:
        # CRITICAL: Check service health before proceeding
        try:
            # PATTERN: Use docker-compose for service management
            result = subprocess.run([
                'docker-compose', '-f', 'docker/docker-compose.yml',
                'up', '-d', service_name
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                return self._wait_for_service_health(service_name)
            
        except Exception as e:
            logger.error(f"Failed to start {service_name}: {str(e)}")
            
        return False
```

### Integration Points
```yaml
DOCKER_SERVICES:
  - service: ollama
    port: 11434
    health_check: "curl -f http://localhost:11434/api/health"
    
  - service: n8n
    port: 5678
    health_check: "curl -f http://localhost:5678/healthz"
    
  - service: openproject
    port: 8080
    health_check: "curl -f http://localhost:8080/health"

AGENT_COORDINATION:
  - parser: "Extract milestones from project overview"
  - orchestrator: "Decompose milestones into tasks"
  - coder: "Generate code for each task"
  - tester: "Validate code implementation"
  - advisor: "Review and improve code quality"

GIT_INTEGRATION:
  - branch: "feature/agentic-starterkit"
  - commit_pattern: "feat: implement {component} for agentic starterkit"
  - merge_strategy: "squash and merge"
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check --fix agents/ utils/ tests/
mypy agents/ utils/ tests/
black agents/ utils/ tests/

# Expected: No errors. If errors, READ the error and fix.
```

### Level 2: Unit Tests
```python
# CREATE comprehensive test suite
def test_parser_milestone_extraction():
    """Test milestone extraction from project overviews"""
    parser = ParserAgent(config)
    result = parser.parse_project_overview("test_project.md")
    assert len(result[0]) > 0  # milestones
    assert len(result[1]) > 0  # prps

def test_coder_implementation():
    """Test code generation functionality"""
    coder = CoderAgent(config)
    task = TaskData(title="Simple function", description="Create hello world")
    result = coder.implement_task(task)
    assert result['success'] is True
    assert 'def hello_world' in result['code']

def test_docker_service_management():
    """Test Docker service startup and health checking"""
    docker_mgr = DockerManager()
    assert docker_mgr.start_service('ollama') is True
    assert docker_mgr.check_service_health('ollama') is True
```

```bash
# Run and iterate until passing:
venv_linux/bin/python -m pytest tests/ -v --tb=short
# If failing: Read error, understand root cause, fix code, re-run
```

### Level 3: Integration Test
```bash
# Test full workflow execution
venv_linux/bin/python kit.py --overview work-orders/001_INITIAL.md --setup-env

# Test Docker services
docker-compose -f docker/docker-compose.yml ps
# Expected: All services running and healthy

# Test agent coordination
venv_linux/bin/python -c "
from agents.parser import ParserAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.advisor import AdvisorAgent

# Test full agent workflow
parser = ParserAgent({})
milestones, prps = parser.parse_project_overview('work-orders/001_INITIAL.md')
print(f'Extracted {len(milestones)} milestones and {len(prps)} PRPs')
"

# Expected: Successful milestone extraction and agent coordination
```

## Final Validation Checklist
- [ ] All tests pass: `venv_linux/bin/python -m pytest tests/ -v`
- [ ] No linting errors: `ruff check agents/ utils/ tests/`
- [ ] No type errors: `mypy agents/ utils/ tests/`
- [ ] Docker services start: `docker-compose -f docker/docker-compose.yml up -d`
- [ ] Manual workflow test: `python kit.py --overview work-orders/001_INITIAL.md`
- [ ] Agent coordination functional: All agents can communicate and execute tasks
- [ ] Error handling graceful: Failed tasks don't crash the system
- [ ] Alerts working: Print and GitHub API alerts functional
- [ ] Git integration working: Commits created for generated code
- [ ] README.md updated: Complete usage instructions and examples
- [ ] Configuration flexible: Easy to modify for different use cases

---

## Anti-Patterns to Avoid
- ❌ Don't create agents without proper CrewAI initialization
- ❌ Don't skip Docker service health checks before proceeding
- ❌ Don't ignore the 3-retry pattern for task execution
- ❌ Don't hardcode file paths or service endpoints
- ❌ Don't skip validation of generated code before execution
- ❌ Don't create files longer than 500 lines (split into modules)
- ❌ Don't skip comprehensive error handling and logging
- ❌ Don't forget to update README.md with new functionality

## Confidence Score: 9/10

This PRP provides comprehensive context for implementing the Ultimate Agentic StarterKit with:
- Complete technical specifications and architecture
- Detailed implementation tasks in proper order
- Comprehensive validation loops and testing strategies
- Real-world examples and patterns to follow
- Proper error handling and retry mechanisms
- Docker integration and service management
- Git integration and project tracking
- Documentation updates and usage instructions

The high confidence score reflects the thorough research, existing codebase analysis, and comprehensive implementation blueprint that should enable successful one-pass implementation.