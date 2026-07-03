#!/usr/bin/env python3
"""
Template Generator for AI Smart Retail Intelligence Platform
This script generates the complete project file structure for a comprehensive
retail intelligence system with multiple business problem solutions.
"""

import os
from pathlib import Path


def create_directory(path: str) -> None:
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def create_file(path: str, content: str = "") -> None:
    """Create file with optional content."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_project_structure() -> None:
    """Generate the complete project file structure."""
    
    # Root level files
    root_files = {
        "README.md": "# AI Smart Retail Intelligence Platform\n\n"
                   "A comprehensive platform solving multiple business problems in retail.\n\n"
                   "## Features\n"
                   "- Data Cleaning\n"
                   "- EDA (Exploratory Data Analysis)\n"
                   "- SQL Integration\n"
                   "- Feature Engineering\n"
                   "- Machine Learning\n"
                   "- Time Series Forecasting\n"
                   "- Customer Segmentation\n"
                   "- Recommendation Engine\n"
                   "- Dashboard (Plotly/Dash)\n"
                   "- FastAPI REST API\n"
                   "- Docker Containerization\n"
                   "- MLflow Experiment Tracking\n"
                   "- DVC Data Version Control\n"
                   "- CI/CD Pipeline\n",
        ".gitignore": "__pycache__/\n*.pyc\n*.pyo\n.env\n.venv/\n.env.local\n"
                   ".mlflow/\n.dvc/\n.mlruns/\n*.dvc\n"
                   "data/raw/*\n!data/raw/.gitkeep\n"
                   "data/processed/*\n!data/processed/.gitkeep\n"
                   "models/trained/*\n!models/trained/.gitkeep\n"
                   ".vscode/\n.idea/\n*.egg-info/\n",
        "requirements.txt": "# Core dependencies\npandas\nnumpy\nscikit-learn\n"
                           "matplotlib\nseaborn\nsqlalchemy\nfastapi\nuvicorn\n"
                           "mlflow\ndvc\njupyter\nplotly\ndash\n"
                           "# Additional ML libraries\nxgboost\nlightgbm\nstatsmodels\n"
                           "# Database\npsycopg2-binary\npymongo\nredis\n"
                           "# API & Web\npython-multipart\npython-jose\npasslib\n"
                           "# Testing\npytest\npytest-cov\n",
        "setup.py": "from setuptools import setup, find_packages\n\nsetup(\n"
                   "    name='ai-smart-retail-intelligence',\n"
                   "    version='1.0.0',\n"
                   "    packages=find_packages(),\n"
                   "    install_requires=[],\n"
                   "    python_requires='>=3.8',\n"
                   ")",
        "config.yaml": "# Configuration file for the project\nproject:\n  name: ai-smart-retail-intelligence\n  version: 1.0.0\n\n"
                     "data:\n  raw_path: data/raw\n  processed_path: data/processed\n\n"
                     "models:\n  path: models/trained\n\n"
                     "api:\n  host: 0.0.0.0\n  port: 8000\n",
        "dvc.yaml": "stages:\n  data_cleaning:\n    cmd: python scripts/run_pipeline.py\n    deps:\n      - src/data_cleaning/cleaner.py\n      - data/raw\n    outs:\n      - data/processed\n\n  feature_engineering:\n    cmd: python src/feature_engineering/creator.py\n    deps:\n      - data/processed\n    outs:\n      - data/features\n",
        "params.yaml": "# Model and training parameters\ndata:\n  test_size: 0.2\n  random_state: 42\n\n"
                       "model:\n  n_estimators: 100\n  max_depth: 10\n",
    }
    
    for file, content in root_files.items():
        create_file(file, content)
    
    # Directory structure
    directories = [
        # Data directories
        "data/raw",
        "data/processed",
        "data/interim",
        "data/external",
        "data/features",
        
        # Notebooks
        "notebooks",
        
        # Source code
        "src",
        "src/data_cleaning",
        "src/eda",
        "src/sql",
        "src/feature_engineering",
        "src/machine_learning",
        "src/time_series",
        "src/customer_segmentation",
        "src/recommendation",
        "src/dashboard",
        "src/api",
        
        # Models
        "models",
        "models/trained",
        "models/checkpoints",
        
        # Tests
        "tests",
        "tests/unit",
        "tests/integration",
        
        # Scripts
        "scripts",
        
        # Docker
        "docker",
        
        # CI/CD
        ".github/workflows",
        
        # Documentation
        "docs",
        
        # MLflow
        "mlflow",
        
        # DVC
        "dvc",
        
        # Logs
        "logs",
    ]
    
    for directory in directories:
        create_directory(directory)
    
    # Create .gitkeep files in data directories
    create_file("data/raw/.gitkeep", "")
    create_file("data/processed/.gitkeep", "")
    create_file("models/trained/.gitkeep", "")
    
    # Source code files
    src_files = {
        "src/__init__.py": "",
        "src/data_cleaning/__init__.py": "",
        "src/data_cleaning/cleaner.py": "# Data cleaning module\n",
        "src/data_cleaning/validators.py": "# Data validation module\n",
        
        "src/eda/__init__.py": "",
        "src/eda/analyzer.py": "# EDA analysis module\n",
        "src/eda/visualizer.py": "# EDA visualization module\n",
        
        "src/sql/__init__.py": "",
        "src/sql/queries.py": "# SQL queries module\n",
        "src/sql/connection.py": "# Database connection module\n",
        
        "src/feature_engineering/__init__.py": "",
        "src/feature_engineering/creator.py": "# Feature creation module\n",
        "src/feature_engineering/selector.py": "# Feature selection module\n",
        
        "src/machine_learning/__init__.py": "",
        "src/machine_learning/train.py": "# Model training module\n",
        "src/machine_learning/predict.py": "# Model prediction module\n",
        "src/machine_learning/evaluate.py": "# Model evaluation module\n",
        
        "src/time_series/__init__.py": "",
        "src/time_series/forecaster.py": "# Time series forecasting module\n",
        "src/time_series/preprocessing.py": "# Time series preprocessing\n",
        
        "src/customer_segmentation/__init__.py": "",
        "src/customer_segmentation/segmenter.py": "# Customer segmentation module\n",
        "src/customer_segmentation/clustering.py": "# Clustering algorithms\n",
        
        "src/recommendation/__init__.py": "",
        "src/recommendation/engine.py": "# Recommendation engine module\n",
        "src/recommendation/collaborative.py": "# Collaborative filtering\n",
        "src/recommendation/content_based.py": "# Content-based filtering\n",
        
        "src/dashboard/__init__.py": "",
        "src/dashboard/app.py": "# Dashboard application\n",
        "src/dashboard/components.py": "# Dashboard components\n",
        
        "src/api/__init__.py": "",
        "src/api/main.py": "# FastAPI main application\n",
        "src/api/routes.py": "# API routes\n",
        "src/api/models.py": "# Pydantic models\n",
    }
    
    for file, content in src_files.items():
        create_file(file, content)
    
    # Test files
    test_files = {
        "tests/__init__.py": "",
        "tests/unit/__init__.py": "",
        "tests/unit/test_cleaner.py": "# Unit tests for cleaner\n",
        "tests/unit/test_analyzer.py": "# Unit tests for analyzer\n",
        "tests/integration/__init__.py": "",
        "tests/integration/test_pipeline.py": "# Integration tests\n",
    }
    
    for file, content in test_files.items():
        create_file(file, content)
    
    # Script files
    script_files = {
        "scripts/run_pipeline.py": "# Run complete data pipeline\n",
        "scripts/train_models.py": "# Train all models\n",
        "scripts/evaluate_models.py": "# Evaluate all models\n",
        "scripts/setup_dvc.py": "# DVC setup script\n",
    }
    
    for file, content in script_files.items():
        create_file(file, content)
    
    # Docker files
    docker_files = {
        "docker/Dockerfile": "FROM python:3.9-slim\n"
                             "WORKDIR /app\n"
                             "COPY requirements.txt .\n"
                             "RUN pip install -r requirements.txt\n"
                             "COPY . .\n"
                             "EXPOSE 8000\n"
                             "CMD ['uvicorn', 'src.api.main:app', '--host', '0.0.0.0', '--port', '8000']\n",
        "docker/docker-compose.yml": "version: '3.8'\n"
                                    "services:\n"
                                    "  app:\n"
                                    "    build: .\n"
                                    "    ports:\n"
                                    "      - '8000:8000'\n"
                                    "    volumes:\n"
                                    "      - ./data:/app/data\n"
                                    "      - ./models:/app/models\n",
        "docker/.dockerignore": "__pycache__\n*.pyc\n.git\n.env\n.venv\n",
    }
    
    for file, content in docker_files.items():
        create_file(file, content)
    
    # CI/CD files
    cicd_files = {
        ".github/workflows/ci.yml": "name: CI\n"
                                   "on: [push, pull_request]\n"
                                   "jobs:\n"
                                   "  test:\n"
                                   "    runs-on: ubuntu-latest\n"
                                   "    steps:\n"
                                   "      - uses: actions/checkout@v2\n"
                                   "      - run: pip install -r requirements.txt\n"
                                   "      - run: pytest --cov=src\n",
        ".github/workflows/cd.yml": "name: CD\n"
                                   "on: [push]\n"
                                   "jobs:\n"
                                   "  deploy:\n"
                                   "    runs-on: ubuntu-latest\n"
                                   "    steps:\n"
                                   "      - uses: actions/checkout@v2\n"
                                   "      - run: echo 'Deploy to production'\n",
    }
    
    for file, content in cicd_files.items():
        create_file(file, content)
    
    # Documentation files
    doc_files = {
        "docs/index.md": "# Documentation\n",
        "docs/architecture.md": "# Architecture\n",
        "docs/api.md": "# API Documentation\n",
    }
    
    for file, content in doc_files.items():
        create_file(file, content)
    
    # DVC config
    dvc_files = {
        "dvc/config": "[core]\n    remote = myremote\n",
        "dvc/.gitignore": "*.dvc\n",
    }
    
    for file, content in dvc_files.items():
        create_file(file, content)
    
    # MLflow config
    mlflow_files = {
        "mlflow/config.py": "# MLflow configuration\n",
    }
    
    for file, content in mlflow_files.items():
        create_file(file, content)
    
    print("Project structure generated successfully!")


if __name__ == "__main__":
    generate_project_structure()