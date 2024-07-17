from setuptools import find_packages,setup
from typing import List

HYPHEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements

setup(
name='Udemy_ML_Project',
version='0.0.1',
author='Mani',
author_email='bm691959@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)