"""Configuration management for AutoClean."""
from pathlib import Path
from typing import Dict, Any
import json
from dataclasses import dataclass

@dataclass
class Config:
    """Main configuration class."""
    dataset_config: Dict[str, Any]
    output_dir: Path
    sample_size: int = 1000
    profile_threshold: int = 10000

    @classmethod
    def from_file(cls, config_path: str) -> "Config":
        """Load configuration from a JSON file."""
        with open(config_path) as f:
            config_data = json.load(f)
        
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        return cls(
            dataset_config=config_data,
            output_dir=output_dir
        )
