from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'  # Corrected variable name

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)  # Remove the editable installation if present
    return requirements

setup(
    name='FaultDetection',
    version='0.0.1',
    author='imeran',
    author_email='md.a@pw.live',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
