from typing import List

from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(requirements_file_path: str) -> List[str]:
    """
    this function will return list of required python libraries
    :param requirements_file_path:
    :return:
    """

    with open(requirements_file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="comprehensive-mlops",
    version="0.0.1",
    author="Sahil Chachere",
    author_email="sahilchachere8@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt"),
)
