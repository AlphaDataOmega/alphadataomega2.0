"""
Parser Agent: Extracts milestones and PRPs from project overview documents.
Uses LlamaIndex for document querying and milestone extraction.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

from llama_index.core import Document, VectorStoreIndex, Settings
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
import PyPDF2


class ParserAgent:
    """
    Agent responsible for parsing project overviews and extracting structured data.
    
    Capabilities:
    - Parse MD/PDF project overviews
    - Extract milestones as JSON
    - Identify PRPs (Product Requirement Patterns)
    - Handle chunked document processing for large files
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the ParserAgent.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.llm = Ollama(model=config.get('ollama_model', 'llama3'))
        self.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        
        # Configure LlamaIndex settings
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        
        # Patterns for milestone extraction
        self.milestone_patterns = [
            r'Week\s+(\d+)[\-\s]*(\d+)?\s*[:\-]\s*(.+?)(?=Week|\Z)',
            r'Phase\s+(\d+)[\-\s]*(\d+)?\s*[:\-]\s*(.+?)(?=Phase|\Z)',
            r'Milestone\s+(\d+)[\-\s]*(\d+)?\s*[:\-]\s*(.+?)(?=Milestone|\Z)',
            r'##\s*(.+?)(?=##|\Z)'
        ]
    
    def parse_project_overview(self, file_path: str) -> Tuple[List[Dict], List[Dict]]:
        """
        Parse project overview document and extract milestones and PRPs.
        
        Args:
            file_path: Path to project overview file (MD or PDF)
            
        Returns:
            Tuple of (milestones, prps) as lists of dictionaries
        """
        try:
            # Load document content
            content = self._load_document(file_path)
            
            # Create document index for querying
            document = Document(text=content)
            index = VectorStoreIndex.from_documents([document])
            query_engine = index.as_query_engine()
            
            # Extract milestones
            milestones = self._extract_milestones(content, query_engine)
            
            # Extract PRPs
            prps = self._extract_prps(content, query_engine)
            
            print(f"📊 Extracted {len(milestones)} milestones and {len(prps)} PRPs")
            
            return milestones, prps
            
        except Exception as e:
            print(f"❌ Error parsing project overview: {str(e)}")
            return [], []
    
    def _load_document(self, file_path: str) -> str:
        """
        Load document content from MD or PDF file.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            str: Document content as text
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")
        
        if path.suffix.lower() == '.pdf':
            return self._extract_pdf_content(file_path)
        elif path.suffix.lower() in ['.md', '.markdown', '.txt']:
            return self._extract_text_content(file_path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")
    
    def _extract_pdf_content(self, file_path: str) -> str:
        """Extract text content from PDF file."""
        content = ""
        
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                content += page.extract_text() + "\n"
        
        return content
    
    def _extract_text_content(self, file_path: str) -> str:
        """Extract content from text-based files."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def _extract_milestones(self, content: str, query_engine) -> List[Dict]:
        """
        Extract milestones from document content.
        
        Args:
            content: Document content
            query_engine: LlamaIndex query engine
            
        Returns:
            List of milestone dictionaries
        """
        milestones = []
        
        # Use LlamaIndex query to extract milestones
        milestone_query = """
        Extract all project milestones, phases, and timeline information from this document.
        Return as a JSON array where each milestone has:
        - title: milestone name
        - timeline: week/phase number or date range
        - description: detailed description
        - deliverables: list of deliverables
        - success_metrics: success criteria
        - dependencies: other milestones this depends on
        """
        
        try:
            response = query_engine.query(milestone_query)
            
            # Try to parse as JSON first
            try:
                parsed_milestones = json.loads(str(response))
                if isinstance(parsed_milestones, list):
                    milestones.extend(parsed_milestones)
            except json.JSONDecodeError:
                # Fallback to pattern matching
                milestones.extend(self._pattern_extract_milestones(content))
            
            # Enhance with additional details
            for milestone in milestones:
                milestone = self._enhance_milestone(milestone, query_engine)
                
        except Exception as e:
            print(f"⚠️  LlamaIndex query failed, using pattern matching: {str(e)}")
            milestones = self._pattern_extract_milestones(content)
        
        return milestones
    
    def _pattern_extract_milestones(self, content: str) -> List[Dict]:
        """Extract milestones using regex patterns."""
        milestones = []
        
        for pattern in self.milestone_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.DOTALL)
            
            for match in matches:
                if pattern.startswith(r'Week'):
                    timeline = f"Week {match.group(1)}"
                    if match.group(2):
                        timeline += f"-{match.group(2)}"
                    description = match.group(3).strip()
                elif pattern.startswith(r'Phase'):
                    timeline = f"Phase {match.group(1)}"
                    description = match.group(3).strip()
                else:
                    timeline = "TBD"
                    description = match.group(1).strip()
                
                milestone = {
                    'title': description.split('\n')[0][:100],
                    'timeline': timeline,
                    'description': description,
                    'deliverables': self._extract_deliverables(description),
                    'success_metrics': [],
                    'dependencies': []
                }
                
                milestones.append(milestone)
        
        return milestones
    
    def _extract_deliverables(self, description: str) -> List[str]:
        """Extract deliverables from milestone description."""
        deliverables = []
        
        # Look for bulleted lists
        bullet_patterns = [
            r'[-•*]\s*(.+?)(?=\n|$)',
            r'^\d+\.\s*(.+?)(?=\n|$)',
            r'✅\s*(.+?)(?=\n|$)'
        ]
        
        for pattern in bullet_patterns:
            matches = re.findall(pattern, description, re.MULTILINE)
            deliverables.extend([match.strip() for match in matches])
        
        return deliverables[:10]  # Limit to first 10 deliverables
    
    def _enhance_milestone(self, milestone: Dict, query_engine) -> Dict:
        """Enhance milestone with additional context from document."""
        try:
            enhancement_query = f"""
            For the milestone "{milestone['title']}", provide:
            1. Success metrics or KPIs
            2. Dependencies on other milestones
            3. Risk factors or challenges
            4. Resource requirements
            
            Return as JSON with keys: success_metrics, dependencies, risks, resources
            """
            
            response = query_engine.query(enhancement_query)
            
            try:
                enhancements = json.loads(str(response))
                if isinstance(enhancements, dict):
                    milestone.update(enhancements)
            except json.JSONDecodeError:
                pass  # Skip enhancement if parsing fails
            
        except Exception:
            pass  # Skip enhancement on error
        
        return milestone
    
    def _extract_prps(self, content: str, query_engine) -> List[Dict]:
        """
        Extract Product Requirement Patterns (PRPs) from document.
        
        Args:
            content: Document content
            query_engine: LlamaIndex query engine
            
        Returns:
            List of PRP dictionaries
        """
        prps = []
        
        prp_query = """
        Extract all product requirements, features, and technical specifications.
        Return as JSON array where each PRP has:
        - name: feature/requirement name
        - type: type of requirement (functional, non-functional, technical)
        - description: detailed description
        - acceptance_criteria: list of acceptance criteria
        - priority: priority level (high, medium, low)
        - complexity: estimated complexity (1-10)
        - category: category (frontend, backend, blockchain, etc.)
        """
        
        try:
            response = query_engine.query(prp_query)
            
            try:
                parsed_prps = json.loads(str(response))
                if isinstance(parsed_prps, list):
                    prps.extend(parsed_prps)
            except json.JSONDecodeError:
                # Fallback to pattern extraction
                prps.extend(self._pattern_extract_prps(content))
                
        except Exception as e:
            print(f"⚠️  PRP extraction failed: {str(e)}")
            prps = self._pattern_extract_prps(content)
        
        return prps
    
    def _pattern_extract_prps(self, content: str) -> List[Dict]:
        """Extract PRPs using pattern matching."""
        prps = []
        
        # Look for feature sections
        feature_patterns = [
            r'###\s*(.+?)(?=###|\Z)',
            r'Feature:\s*(.+?)(?=Feature:|\Z)',
            r'Requirement:\s*(.+?)(?=Requirement:|\Z)'
        ]
        
        for pattern in feature_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.DOTALL)
            
            for match in matches:
                feature_text = match.group(1).strip()
                
                prp = {
                    'name': feature_text.split('\n')[0][:100],
                    'type': 'functional',
                    'description': feature_text,
                    'acceptance_criteria': self._extract_acceptance_criteria(feature_text),
                    'priority': 'medium',
                    'complexity': 5,
                    'category': self._categorize_prp(feature_text)
                }
                
                prps.append(prp)
        
        return prps
    
    def _extract_acceptance_criteria(self, text: str) -> List[str]:
        """Extract acceptance criteria from PRP text."""
        criteria = []
        
        # Look for acceptance criteria patterns
        patterns = [
            r'acceptance criteria?[:\-]\s*(.+?)(?=\n\n|\Z)',
            r'must\s+(.+?)(?=\n|$)',
            r'should\s+(.+?)(?=\n|$)',
            r'shall\s+(.+?)(?=\n|$)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
            criteria.extend([match.strip() for match in matches])
        
        return criteria[:5]  # Limit to first 5 criteria
    
    def _categorize_prp(self, text: str) -> str:
        """Categorize PRP based on content."""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['ui', 'frontend', 'react', 'interface']):
            return 'frontend'
        elif any(word in text_lower for word in ['api', 'backend', 'server', 'database']):
            return 'backend'
        elif any(word in text_lower for word in ['blockchain', 'contract', 'solidity', 'dao']):
            return 'blockchain'
        elif any(word in text_lower for word in ['test', 'testing', 'validation']):
            return 'testing'
        elif any(word in text_lower for word in ['security', 'audit', 'encryption']):
            return 'security'
        else:
            return 'general'