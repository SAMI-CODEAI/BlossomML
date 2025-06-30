from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-8",
    version="0.1",
    author="Samiksha",
    packages=find_packages(),
    install_requires=requirements,
    description="An MLOps project for experimenting with deployment and packaging",
    python_requires='>=3.7',
)