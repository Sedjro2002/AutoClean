"""Configuration management for AutoClean."""
from pathlib import Path
from typing import Dict, Any, List
import json
from dataclasses import dataclass

@dataclass
class Config:
    """Main configuration class."""
    dataset_config: Dict[str, Any]
    output_dir: Path
    sample_size: int = 1000
    profile_threshold: int = 10000
    code_analysis_paths: List[str] = None  # List of paths to analyze for potential biases
    code_analysis_type: str = "syntax"  # Can be "syntax" or "ai"

    @classmethod
    def from_file(cls, config_path: str) -> "Config":
        """Load configuration from a JSON file."""
        with open(config_path) as f:
            config_data = json.load(f)
        
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        return cls(
            dataset_config=config_data,
            output_dir=output_dir,
            code_analysis_paths=config_data.get('code_analysis_paths', None),
            code_analysis_type=config_data.get('code_analysis_type', 'syntax')
        )
