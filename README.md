# modelflow

**modelflow** is a Python package that automates the generation of Hugging Face model skeletons, including configuration files, API endpoints, Docker containerization, and deployment integration. It streamlines the process of preparing machine learning models for production, making it easy for developers to go from model selection to deployable code with minimal effort.

## Features

- Fetches model configuration directly from Hugging Face Hub.
- Auto-generates Python code, FastAPI endpoints, Dockerfiles, and requirements.
- Produces ready-to-deploy project skeletons for your chosen model.
- CLI interface for fast, repeatable project generation.

## Installation

```bash
pip install .
```
Or, if you want to install from source in editable mode:
```bash
pip install -e .
```

## Usage

After installation, use the `modelflow` CLI to generate a model project skeleton:

```bash
modelflow generate --modelid <huggingface-model-id> --output_dir <output-directory>
```

- `--modelid` (required): The Hugging Face model ID (e.g., `Qwen/Qwen2.5-Coder-7B-Instruct`)
- `--output_dir` (optional): Directory to output the generated files (defaults to the model ID)

### Example

```bash
modelflow generate --modelid Qwen/Qwen2.5-Coder-7B-Instruct --output_dir modelPackage
```

This will create a directory `modelPackage` containing:
- `Model.py` (model loading and inference)
- `api.py` (FastAPI server)
- `requirements.txt`
- `Dockerfile`
- `.dockerignore`
- `model_log` (model configuration log)

## Requirements

- Python 3.7+
- [transformers](https://pypi.org/project/transformers/)
- [jinja2](https://pypi.org/project/Jinja2/)
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

All dependencies are installed automatically.

## Author

Maharshi Patel  
maharshi7178@gmail.com
