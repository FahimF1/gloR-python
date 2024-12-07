from setuptools import setup, find_packages

setup(
    name='gloR',
    version='0.1.0',
    description='Python package for labor redistribution optimization',
    author='Fahim Karim',
    author_email='polash.fahim@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'matplotlib>=3.0.0'
    ],
)
