"""AI-based code analysis module for detecting ethical biases in data processing pipelines."""

from typing import List, Dict, Any, Optional, Union, AsyncIterator
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from openai import AsyncOpenAI, APIError
from loguru import logger
from dataclasses import dataclass
import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()  # Load environment variables from .env file

class AnalysisSeverity(str, Enum):
    """Severity levels for code analysis findings."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CodeSection(BaseModel):
    """Model representing a problematic code section."""
    code_snippet: str = Field(..., description="The problematic code snippet")
    issue_type: str = Field(..., description="Type of ethical issue detected")
    explanation: str = Field(..., description="Detailed explanation of the issue")

class CodeBiasAnalysisResult(BaseModel):
    """Model for code bias analysis results from AI."""
    is_problematic: bool = Field(
        ...,
        description="Whether the code contains potential ethical issues"
    )
    sensitivity_level: int = Field(
        ...,
        ge=0,
        le=10,
        description="The sensitivity level of the potential biases (0-10)"
    )
    problematic_sections: List[CodeSection] = Field(
        ...,
        description="List of problematic code sections with metadata"
    )
    recommendations: List[str] = Field(
        ...,
        description="List of recommendations for addressing the potential biases"
    )
    severity: AnalysisSeverity = Field(
        ...,
        description="Overall severity of the identified issues"
    )

@dataclass
class Dependency:
    """Model representing code dependencies for analysis."""
    code: str = Field(..., description="The code content to analyze")
    file_path: str = Field(..., description="Path to the source file")
    context: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional context about the code"
    )

class AICodeAnalyzer:
    """AI-powered code analyzer for detecting ethical biases in data processing code."""
    
    def __init__(self):
        """Initialize the AI code analyzer with configuration."""
        self.llm = os.getenv('LLM_MODEL', 'deepseek-chat')
        self.base_url = os.getenv('BASE_URL', 'https://api.deepseek.com/v1')
        self.api_key = os.getenv('API_KEY')
        
        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")
            
        try:
            self.client = AsyncOpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
                timeout=30.0
            )
            self.model = OpenAIModel(self.llm, openai_client=self.client)
        except Exception as e:
            logger.error(f"Failed to initialize AI client: {str(e)}")
            raise

        self.system_prompt = """You are an expert AI ethics advisor specializing in analyzing Python code for potential ethical biases. Your task is to:

1. Identify code sections that could introduce ethical biases in data processing or model training
2. Focus on:
   - Data filtering or selection that might exclude certain groups
   - Feature engineering that could amplify biases
   - Preprocessing steps that might disproportionately affect certain demographics
   - Direct or indirect use of sensitive attributes
   - Sampling methods that might not preserve demographic distributions
3. Provide specific line numbers and explanations for problematic code
4. Rate the overall sensitivity level from 0-10
5. Offer concrete recommendations for addressing the issues
6. Assess the severity of each finding (low, medium, high, critical)

Be thorough but avoid false positives. Focus on real ethical concerns rather than general code quality issues."""

    def analyze_file(self, file_path: str) -> Union[CodeBiasAnalysisResult, str]:
        """Analyze a Python file for potential ethical biases using AI.
        
        Args:
            file_path: Path to the Python file to analyze
            
        Returns:
            CodeBiasAnalysisResult containing the analysis or error message
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()

            agent = Agent(
                model=self.model,
                system_prompt=self.system_prompt,
                retries=3,
                result_type=CodeBiasAnalysisResult,
                deps_type=Dependency
            )
            
            deps = Dependency(
                code=code_content,
                file_path=file_path,
                context={
                    "file_size": len(code_content),
                    "file_type": "python"
                }
            )
            
            @agent.system_prompt
            def prompt(ctx: RunContext[Dependency]) -> str:
                return self.system_prompt + f"""\n{ctx.deps.context['file_type']} file: {ctx.deps.file_path} \n contents: {ctx.deps.code}"""

            result = agent.run_sync(
                "Analyze the Python code for ethical biases",
                deps=deps,
            )
            
            logger.info(f"Analysis completed for {file_path}")
            return result.data

        except (APIError, ValidationError) as e:
            logger.error(f"Error analyzing file {file_path}: {str(e)}")
            return f"Error analyzing file {file_path}: {str(e)}"
        except Exception as e:
            logger.error(f"Unexpected error analyzing file {file_path}: {str(e)}")
            return f"Unexpected error analyzing file {file_path}: {str(e)}"

    def analyze_path(self, path: str) -> List[Dict[str, Any]]:
        """Analyze all Python files in the given path for potential biases.
        
        Args:
            path: Path to a file or directory to analyze
            
        Returns:
            List of analysis results for each file
        """
        path_obj = Path(path)
        results = []

        def analyze_single_file(file_path: str):
            result = self.analyze_file(file_path)
            return {
                "file": file_path,
                # "analysis": result.model_dump() if isinstance(result, BaseModel) else result
                "analysis": result.model_dump()
            }

        if path_obj.is_file() and path_obj.suffix == '.py':
            results.append(analyze_single_file(str(path_obj)))
        elif path_obj.is_dir():
            for py_file in path_obj.rglob('*.py'):
                results.append(analyze_single_file(str(py_file)))

        return results

    async def analyze_path_concurrently(self, path: str) -> List[Dict[str, Any]]:
        """Analyze all Python files in the given path concurrently for potential biases.
        
        Args:
            path: Path to a file or directory to analyze
            
        Returns:
            List of analysis results for each file
        """
        path_obj = Path(path)
        results = []

        async def analyze_single_file(file_path: str):
            result = self.analyze_file(file_path)
            return {
                "file": file_path,
                "analysis": result.model_dump() if isinstance(result, BaseModel) else result
            }

        if path_obj.is_file() and path_obj.suffix == '.py':
            results.append(await analyze_single_file(str(path_obj)))
        elif path_obj.is_dir():
            import asyncio
            tasks = [analyze_single_file(str(py_file)) for py_file in path_obj.rglob('*.py')]
            results = await asyncio.gather(*tasks)

        return results