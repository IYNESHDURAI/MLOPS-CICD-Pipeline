# MLOps CI/CD Pipeline

## Overview
This project implements a simple CI/CD pipeline for training and testing a machine learning model (Iris classification).

## CI/CD Workflow
The pipeline includes:
- **Linting:** Ensures code quality using `flake8`.
- **Unit Testing:** Verifies the ML model with `unittest`.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the model: `python model.py`
3. Run tests: `python -m unittest discover tests`

## CI/CD Pipeline
- The pipeline runs on every `push` or `pull_request` to the `main` branch.
