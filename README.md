# FairAutoClean

FairAutoClean is a Python package for automated data preprocessing and cleaning with a focus on fairness and bias detection. It helps data scientists and analysts clean their datasets while being mindful of potential biases and ethical considerations.

## Features

- Automated data cleaning and preprocessing
- Fairness analysis and bias detection
- Configurable cleaning parameters
- Command-line interface for easy use

## Installation

```bash
pip install FairAutoClean
```

## Usage

### As a Python Package

```python
from FairAutoClean import process_dataset

# Process your dataset
cleaned_df = process_dataset(
    config_path="path/to/config.json",
    dataset_path="path/to/dataset.csv",
    output_path="path/to/output" 
)
```

### As a Command-Line Tool

```bash
fairautoclean --config path/to/config.json --dataset path/to/dataset.csv --output path/to/output
```

Required arguments:
- `--config`: Path to the JSON configuration file
- `--dataset`: Path to the input dataset (CSV format)
- `--output`: Path to save the cleaned dataset

## Configuration

Create a JSON configuration file to specify your data cleaning parameters. Example:

```json
{
    "dataset_config": {
        "dataset": {
            "sensitive_features": ["gender", "race"],
            "target": "outcome"
        }
    }
}
```

## Environment variables

This is needed only for sensitive features detection and for AI code analysis

- `LLM_MODEL`: Model name (e.g., "gpt-4o-mini" or "llama3.2:3b")
- `BASE_URL`: Base URL for OpenAI like API (e.g., "https://api.openai.com/v1" or "http://localhost:11434/v1")
- `API_KEY`: API key for OpenAI like API (e.g., "sk-...")

## Documentation

For detailed documentation and examples, visit our [documentation](link-to-documentation).

## Features in Detail

### Data Cleaning
- Missing value imputation
- Categorical encoding
- Feature scaling
- Outlier detection and handling

### Fairness Analysis
- Bias detection in data processing
- Sensitive feature identification
- AI-powered code analysis for potential biases
- Detailed audit trails

### Report Generation
- Markdown report generation
- Detailed operation logs
- Transparency in data transformations
- Bias analysis results

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use FairAutoClean in your research, please cite:

```bibtex
@software{fairautoclean2025,
  author = {Sedjro BONOU},
  title = {FairAutoClean: Automated Fair Data Preprocessing & Cleaning},
  year = {2025},
  version = {1.2.0}
}
```