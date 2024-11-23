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