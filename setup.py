from setuptools import setup, find_packages

setup(
    name='mosplot',
    version='0.1.0',
    description='A python tool for making plots of mosfet parameters.',
    author='Mohamed Watfa',
    author_email='medwatt@hotmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy'
    ],
)
