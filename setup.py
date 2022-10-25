from setuptools import find_packages, setup
from typing import List

setup(

    name ="sensor",
    version="0.0.1",
    author="Ritesh",
    author_email= "sil.ritzzz@gmail.com",
    packages= find_packages(),
    install_requires=["pymongo[srv]==4.3.2"],
)