"""AI-based code analysis module for detecting ethical biases."""
from typing import List, Dict, Any
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.models.openai import OpenAIModel
from openai import AsyncOpenAI
from loguru import logger
import os

class CodeBiasAnalysisResult(BaseModel):
    """Model for code bias analysis results from AI."""
    is_problematic: bool = Field(..., description="Whether the code contains potential ethical issues")
    sensitivity_level: int = Field(
        ..., 
        ge=0, 
        le=10, 
        description="The sensitivity level of the potential biases (0-10)"
    )
    problematic_sections: List[Dict[str, Any]] = Field(
        ..., 
        description="List of problematic code sections with line numbers and explanations"
    )
    recommendations: List[str] = Field(
        ..., 
        description="List of recommendations for addressing the potential biases"
    )
    
class Dependency(BaseModel):
    code: str
    file_path: str

class AICodeAnalyzer:
    """AI-powered code analyzer for detecting ethical biases."""
    
    def __init__(self):
        """Initialize the AI code analyzer."""
        # llm = os.getenv('LLM_MODEL', 'gpt-4o-mini')
        # llm = os.getenv('LLM_MODEL', 'llama3.2:3b')
        llm = os.getenv('LLM_MODEL', 'deepseek-chat')
        base_url = os.getenv('BASE_URL', 'https://api.deepseek.com/v1')
        api_key = os.getenv('API_KEY', 'sk-feab401304ce4af48849c9e630511d48') #TODO to change
        # try:
        #     client = AsyncOpenAI(base_url="https://api.openai.com/v1", api_key="sk-abcdef1234567890abcdef1234567890abcdef12")
        # except Exception as e:
        #     logger.error(f"Error initializing OpenAI client: {str(e)}")
        #     client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        
        # client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        client = AsyncOpenAI(base_url=base_url, api_key=api_key)
        
        # self.model = OpenAIModel(llm, openai_client=client)
        self.model = (
            OpenAIModel(llm)
            if llm.lower().startswith("gpt")
            else OpenAIModel(llm, openai_client=client)
        )
        
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

Be thorough but avoid false positives. Focus on real ethical concerns rather than general code quality issues."""

    def analyze_file(self, file_path: str) -> CodeBiasAnalysisResult:
        """Analyze a Python file for potential ethical biases using AI.
        
        Args:
            file_path: Path to the Python file to analyze
            
        Returns:
            CodeBiasAnalysisResult containing the analysis
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()

            agent = Agent(
                model=self.model,
                system_prompt=self.system_prompt,
                retries=10,
                result_type=CodeBiasAnalysisResult,
                deps_type=Dependency
            )
            
            @agent.system_prompt
            def prompt(ctx: RunContext[Dependency]) -> str:
                return self.system_prompt
            
            deps = Dependency(code=code_content, file_path=file_path)
            # context = RunContext(deps=deps)

            result = agent.run_sync(
                "Analyze the Python code for ethical biases",
                deps=deps,
            )
            
            print("\n\n")
            print(result.data)
            
            return result.data

        except Exception as e:
            logger.error(f"Error analyzing file {file_path} with AI: {str(e)}")
            return f"Error analyzing file {file_path} with AI: {str(e)}"

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
                "analysis": result.model_dump()
            }

        if path_obj.is_file() and path_obj.suffix == '.py':
            results.append(analyze_single_file(str(path_obj)))
        elif path_obj.is_dir():
            for py_file in path_obj.rglob('*.py'):
                results.append(analyze_single_file(str(py_file)))

        return results
