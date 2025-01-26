### CI/CD Pipeline Report

#### **Objective**  
The objective of this pipeline is to understand the fundamentals of MLOps and implement a basic CI/CD pipeline for a simple machine learning project using GitHub Actions. The pipeline automates stages such as linting, testing, and model deployment.

---

### **Pipeline Stages**

1. **Code Checkout**  
   - **Description**: The pipeline starts by checking out the latest code from the GitHub repository using `actions/checkout@v3`.  
   - **Purpose**: Ensures the pipeline runs with the most up-to-date version of the code.

2. **Set Up Python**  
   - **Description**: Python version 3.12.4 is set up using `actions/setup-python@v3`.  
   - **Purpose**: Ensures the Python environment is consistent across different pipeline runs.

3. **Install Dependencies**  
   - **Description**: The pipeline installs necessary dependencies like `scikit-learn` using `pip install`.  
   - **Purpose**: Installs the required libraries for model training and testing.

4. **Linting**  
   - **Description**: The code is checked for style issues using `flake8`. This ensures that the code follows proper coding standards.  
   - **Purpose**: Ensures code quality and consistency by identifying basic syntax and style issues.

5. **Testing**  
   - **Description**: Unit tests are executed using Python's `unittest` framework to ensure the model works as expected.  
   - **Purpose**: Validates the functionality of the code and verifies that no changes break the existing implementation.

6. **Model Training and Saving**  
   - **Description**: The `model.py` script loads the Iris dataset, trains a Random Forest Classifier, evaluates its accuracy, and saves the model as `iris_model.pkl`.  
   - **Purpose**: Trains the machine learning model and saves it for future use or deployment.

7. **Deployment (Placeholder)**  
   - **Description**: A placeholder stage for model deployment. This stage can be extended in the future to deploy the model to a server or cloud platform.  
   - **Purpose**: Placeholder for deployment, indicating that the pipeline can be extended to automate deployment steps.
------

## Logs
- Successful pipeline runs can be found in the Actions tab on GitHub.

## Screenshots
![Pipeline Success](https://github.com/IYNESHDURAI/MLOPS-CICD-Pipeline/tree/main/Screenshots)

## Git Repository
[GitHub Repository](https://github.com/IYNESHDURAI/MLOPS-CICD-Pipeline)

---

### **Version Control and Collaboration**  
- **Branching**: Multiple branches are used to separate development and feature work.
- **Merging and Pull Requests**: Changes are merged to the `main` branch through pull requests, which are reviewed before being merged to ensure code quality and correctness.

---

This CI/CD pipeline ensures that every code push or pull request triggers the necessary stages of linting, testing, and model training, and sets the foundation for continuous integration and deployment practices in MLOps.
