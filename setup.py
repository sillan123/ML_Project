from setuptools import find_packages,setup 
from typing import List
E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    "return list of requirements"
    requirements=[]
    with open(file_path) as file_obj:
        file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements

    
setup(
    name='mlproject',
    version='0.0.1',
    author='Sillan',
    author_email='sillan.sahani6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)