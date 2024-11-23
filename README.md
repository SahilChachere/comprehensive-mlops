# comprehensive-mlops (Project under development)
`Description:` Project `comprehensive-mlops` is an end-to-end MLOps initiative encompassing various stages, including `Data Ingestion, Data Transformation, Model Development, Model Evaluation, and Model Deployment.` Leveraging tools such as GitHub Actions for CI/CD and deploying on AWS cloud, this project ensures a seamless and automated machine learning lifecycle.  
## A. IDE & Virtual Environment Configuration
### A.1 Pycharm
1. Go to ``File -> Settings -> Tools -> Terminal -> Application Settings``
2. Replace the value in Shell path with ``cmd.exe "/K" C:\path\to\Anaconda3\Scripts\activate.bat``
![img.png](images/pycharm_conda_config.png)
```commandline
conda create -p venv python==3.11

conda activate venv/
```

## B. Project Setup for Pypi
`` See setup.py, requirements.txt files and src directory residing in root.``

## C. Code Quality
**1** `Sort Imports:` Utilizes the `isort` Python package to automatically sort imports in .py files, ensuring they are organized and well-ordered. Run the `isort .` command to organize and sort imports within your project files.\
**2** `Flake8:` Combines pyflakes, pycodestyle, and mccabe to check for style and quality issues in your code.\
**3** `Black:` A code formatter that automatically formats your Python code to adhere to the PEP 8 style guide. Run the `python -m black .` command to execute.