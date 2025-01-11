# setup.py file acts as an intial file to be called by machine after build similar to index.html
from setuptools import find_packages,setup
from typing import List

# -e should not be readwhle reading the packages list
HYPEN_DOT_E="-e ."
def get_requirements(filepath:str)->List[str]:
    '''
    this functions returns the list of requirements
    '''
    requirements=[]
    with open(filepath) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
        
    return requirements
# create setup() basically for metadata of application
setup(
    name="ml_etl",
    version="0.0.1",
    description="Intial ETL project",
    author="Nikhil",
    author_email="nikhilkudupudi@gmail.com",
    packages=find_packages(),# it will check for all the __init__.py files in all folders
    install_requires=get_requirements("requirements.txt")   #["pandas","numpy","matplotlib","seaborn"]
    )