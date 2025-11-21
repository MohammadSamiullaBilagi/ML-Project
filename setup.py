from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the requirements list from a requirements.txt file.
    '''
    requirements = []
    HYPHEN_E_DOT = '-e .'  # Typically represents editable installs in requirements

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Strip newline and whitespace characters from each requirement
        requirements = [req.strip() for req in requirements]

        # Remove editable installs if present that is -e . in requirements.txt
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="sami",
    author_email="mdsamiulla2002@gmail.com",
    packages=find_packages(),  #this find packages will find how many folders have __init__.py so it cosiders that folder as package and builds it, ex: src
    install_requires=get_requirements('Requirements.txt'), #function reads the file and install dependencies

)