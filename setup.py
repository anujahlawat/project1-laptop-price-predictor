from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='e .'
def get_requirements(file_path:str)->List[str]:           #parameter of this fn is path of requirements.txt and it contains string and will return a list
    requirements=[]
    with open(file_path) as file_obj:                     #file path means "requirements.txt"
        requirements=file_obj.readlines()                 #while reading it will add new line terminator "\n" to the list, so we have replace it
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:                   #"-e ." in requirements.py is to launch setup.py, i need to remove it from here
            requirements.remove(HYPHEN_E_DOT)
return requirements

     


setup(

name='laptop price predictor',               #name of project
version='0.0.1',                             #version of ur application
author='Anuj Ahlawat',
author_email='anujahlawat0024@gmail.com',
packages=find_packages(),                      #it will find all the packages
#install_requires=['pandas','numpy','seaborn']  #whatever libraries i need, i will write it here and automatically it will do all the innstallations
#there are scenario where we need to install 100 packages and it is not possible to write all packages in 
#install_requires=['pandas','numpy'] in setup.py 
#so what we do is, we try to build a fn in setup.py
install_requires=get_requirements('requirements.txt')

)