import os
from pathlib import PATH

from src.logger import loggging

MODULE_NAME = "comprehensive-mlops"

import nox
from nox import session

nox.options.reuse_exisiting_virtualenvs = True
nox.options.error_on_missing_interpreters = True

nox.options.sessions = ["format"]
VERSION = os.getenv("version_number", "0.1.0") #to be utilised by CI

PYTHON_VERSIONS: list[str] = ["3.12"]

PROJECT_DIR = PATH(__file__).parent
MODULE_DIR = PROJECT_DIR/MODULE_NAME
REQUIREMENTS_DIR = PROJECT_DIR/"requirements"



@nox.session(venv_backend="virtualenv", python=PYTHON_VERSIONS[-1])
def format(session: Session) -> None:
    session.install("-r", str(REQUIREMENTS_DIR/"format-requirements.txt"))
    session.run("black", ".", "--check")
    session.run("isort", ".", "--check")