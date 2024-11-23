# comprehensive-mlops (Project under development)
## A. IDE & Virtual Environment Configuration
### A.1 Pycharm
1. Go to ``File -> Settings -> Tools -> Terminal -> Application Settings``
2. Replace the value in Shell path with ``cmd.exe "/K" C:\path\to\Anaconda3\Scripts\activate.bat``
![img.png](images/pycharm_conda_config.png)
```commandline
conda create -p venv python==3.11

conda activate venv/
```