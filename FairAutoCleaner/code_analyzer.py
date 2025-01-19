"""Module for analyzing code for potential ethical biases."""
import ast
from pathlib import Path
from typing import List, Dict, Any, Set
from dataclasses import dataclass
from loguru import logger

@dataclass
class CodeBiasResult:
    """Container for code bias analysis results."""
    file_path: str
    potential_biases: List[Dict[str, Any]]
    risk_level: str
    recommendations: List[str]

class CodeBiasAnalyzer:
    """Analyzes Python code for potential ethical biases."""

    # Keywords and patterns that might indicate bias
    BIAS_INDICATORS = {
        'data_filtering': {
            'keywords': ['filter', 'drop', 'remove', 'exclude'],
            'risk': 'Selection bias through data filtering'
        },
        'feature_engineering': {
            'keywords': ['encode', 'transform', 'normalize', 'scale'],
            'risk': 'Potential encoding bias in feature engineering'
        },
        'sampling': {
            'keywords': ['sample', 'random', 'stratify'],
            'risk': 'Sampling bias'
        },
        'sensitive_attributes': {
            'keywords': ['gender', 'race', 'ethnicity', 'age', 'religion', 'nationality'],
            'risk': 'Direct use of sensitive attributes'
        }
    }

    def __init__(self):
        """Initialize the CodeBiasAnalyzer."""
        self.analyzed_files: Set[str] = set()

    def analyze_path(self, path: str) -> List[CodeBiasResult]:
        """Analyze all Python files in the given path for potential biases.
        
        Args:
            path: Path to a file or directory to analyze
            
        Returns:
            List of CodeBiasResult objects containing analysis results
        """
        path_obj = Path(path)
        results = []

        if path_obj.is_file() and path_obj.suffix == '.py':
            results.append(self.analyze_file(str(path_obj)))
        elif path_obj.is_dir():
            for py_file in path_obj.rglob('*.py'):
                if str(py_file) not in self.analyzed_files:
                    results.append(self.analyze_file(str(py_file)))

        return [r for r in results if r is not None]

    def analyze_file(self, file_path: str) -> CodeBiasResult:
        """Analyze a single Python file for potential biases.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            CodeBiasResult object containing analysis results
        """
        if file_path in self.analyzed_files:
            return None

        self.analyzed_files.add(file_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()

            tree = ast.parse(code)
            visitor = CodeVisitor()
            visitor.visit(tree)

            potential_biases = []
            for node_info in visitor.nodes_of_interest:
                for category, info in self.BIAS_INDICATORS.items():
                    if any(kw in node_info['name'].lower() for kw in info['keywords']):
                        potential_biases.append({
                            'category': category,
                            'risk': info['risk'],
                            'location': f"Line {node_info['lineno']}",
                            'code_element': node_info['name'],
                            'context': node_info.get('context', '')
                        })

            risk_level = self._assess_risk_level(potential_biases)
            recommendations = self._generate_recommendations(potential_biases)

            return CodeBiasResult(
                file_path=file_path,
                potential_biases=potential_biases,
                risk_level=risk_level,
                recommendations=recommendations
            )

        except Exception as e:
            logger.error(f"Error analyzing file {file_path}: {str(e)}")
            return None

    def _assess_risk_level(self, biases: List[Dict[str, Any]]) -> str:
        """Assess the overall risk level based on detected biases."""
        if not biases:
            return "LOW"
        if len(biases) > 5:
            return "HIGH"
        if any('sensitive_attributes' in b['category'] for b in biases):
            return "HIGH"
        return "MEDIUM" if len(biases) > 2 else "LOW"

    def _generate_recommendations(self, biases: List[Dict[str, Any]]) -> List[str]:
        """Generate recommendations based on detected biases."""
        recommendations = []
        
        if not biases:
            recommendations.append("No immediate bias concerns detected.")
            return recommendations

        bias_categories = {b['category'] for b in biases}
        
        if 'data_filtering' in bias_categories:
            recommendations.append(
                "Review data filtering operations to ensure they don't inadvertently exclude "
                "important demographic groups or create selection bias."
            )
            
        if 'feature_engineering' in bias_categories:
            recommendations.append(
                "Audit feature transformations to ensure they maintain fair representation "
                "across different demographic groups."
            )
            
        if 'sampling' in bias_categories:
            recommendations.append(
                "Verify that sampling methods preserve the distribution of sensitive attributes "
                "and consider using stratified sampling when appropriate."
            )
            
        if 'sensitive_attributes' in bias_categories:
            recommendations.append(
                "Review direct usage of sensitive attributes and consider implementing "
                "fairness-aware preprocessing techniques."
            )

        return recommendations


class CodeVisitor(ast.NodeVisitor):
    """AST visitor to collect information about code elements."""
    
    def __init__(self):
        self.nodes_of_interest = []
        self.current_context = []

    def visit_FunctionDef(self, node):
        """Visit function definitions."""
        self.current_context.append(node.name)
        self.nodes_of_interest.append({
            'type': 'function',
            'name': node.name,
            'lineno': node.lineno,
            'context': ' > '.join(self.current_context)
        })
        self.generic_visit(node)
        self.current_context.pop()

    def visit_Call(self, node):
        """Visit function calls."""
        if isinstance(node.func, ast.Name):
            self.nodes_of_interest.append({
                'type': 'call',
                'name': node.func.id,
                'lineno': node.lineno,
                'context': ' > '.join(self.current_context)
            })
        elif isinstance(node.func, ast.Attribute):
            self.nodes_of_interest.append({
                'type': 'call',
                'name': node.func.attr,
                'lineno': node.lineno,
                'context': ' > '.join(self.current_context)
            })
        self.generic_visit(node)
