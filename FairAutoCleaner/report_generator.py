"""
Module for generating markdown reports from AutoClean JSON audit trails.
"""

from typing import Dict
import json
from datetime import datetime
from pathlib import Path
import os

class ReportGenerator:
    def __init__(self, json_file_path):
        """
        Initialize the report generator with a JSON file path.
        
        Args:
            json_file_path (str): Path to the JSON audit trail file
        """
        self.json_file_path = json_file_path
        self.data = self._load_json()
        
    def _load_json(self):
        """Load and parse the JSON file."""
        with open(self.json_file_path, 'r') as f:
            return json.load(f)
    
    def _format_duration(self, seconds):
        """Format duration in seconds to a readable string."""
        if seconds is None:
            return "N/A"
        if seconds < 1:
            return f"{seconds*1000:.2f} ms"
        elif seconds < 60:
            return f"{seconds:.2f} seconds"
        else:
            minutes = int(seconds // 60)
            remaining_seconds = seconds % 60
            return f"{minutes} minutes {remaining_seconds:.2f} seconds"

    def _format_shape(self, shape):
        """Format shape tuple to readable string."""
        if not shape:
            return "N/A"
        return f"{shape[0]} rows x {shape[1]} columns"
    
    def write_dict(self, dictionary: Dict, content: list,x):
        space = "    " * x
        for key, value in dictionary.items():
            if isinstance(value, dict):
                content.append(f"{space}- **{key}**: ")
                self.write_dict(value, content,x+1)
            elif isinstance(value, list):
                content.append(f"{space}- **{key}**: ")
                self.write_list(value, content,x+1)
            else:
                content.append(f"{space}- **{key}**: {value}")
                
    def write_list(self, list: list, content: list,x):
        space = "    " * x
        for item in list:
            if isinstance(item, dict):
                if "column" in item:
                    content.append(f"{space}- **{item['column']}**")
                else:
                    content.append(f"{space}- value:")
                self.write_dict(item, content,x+1)
            else:
                content.append(f"{space}- {item}")
                
    def generate_report(self, output_dir="output"):
        """
        Generate a markdown report from the JSON audit trail.
        
        Args:
            output_dir (str): Directory where the report will be saved
        
        Returns:
            str: Path to the generated report
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate report content
        content = []
        
        # Header
        content.append("# FairAutoCleaner Report\n")
        
        # Summary section
        content.append("## Summary")
        content.append(f"- **Start Time**: {self.data.get('start_time', 'N/A')}")
        content.append(f"- **End Time**: {self.data.get('end_time', 'N/A')}")
        content.append(f"- **Total Duration**: {self._format_duration(self.data.get('total_duration_seconds'))}")
        content.append(f"- **Total Operations**: {self.data.get('final_metrics', {}).get('total_operations', 0)}\n")
        
        # Operations Details
        content.append("## Operations Details")
        
        for op in self.data.get('operations', []):
            # Operation header
            content.append(f"### {op['operation_name']}")
            content.append(f"_{op['description']}_\n")
            
            # Operation parameters
            content.append("#### Parameters")
            self.write_dict(op['parameters'], content, 0)
            content.append("")
            
            # Operation metrics
            content.append("#### Metrics")
            metrics = op['metrics']
            content.append(f"- **Duration**: {self._format_duration(metrics.get('duration_seconds'))}")
            content.append(f"- **Input Shape**: {self._format_shape(metrics.get('input_shape'))}")
            content.append(f"- **Output Shape**: {self._format_shape(metrics.get('output_shape'))}")
            content.append(f"- **Success**: {metrics.get('success', False)}")
            
            if metrics.get('error'):
                content.append(f"- **Error**: {metrics['error']}")
                
            # Changes made
            content.append("\n#### Changes Made")
            self.write_dict(metrics.get('changes_made', {}), content, 0)
            
            # Warnings
            if op.get('warnings'):
                content.append("\n#### Warnings")
                for warning in op['warnings']:
                    content.append(f"- {warning}")
            
            content.append("\n---\n")
        
        # Write to file
        report_path = os.path.join(output_dir, "report.md")
        with open(report_path, 'w') as f:
            f.write('\n'.join(content))
            
        return report_path

if __name__ == "__main__":
    # Example usage
    json_path = "output/audit_trail.json"
    generator = ReportGenerator(json_path)
    report_path = generator.generate_report()
    print(f"Report generated at: {report_path}")
