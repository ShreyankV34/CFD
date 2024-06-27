from setuptools import setup, find_packages

setup(
    name='cfd_tools',
    version='0.1.0',
    description='A package for detecting wakes and flow separation in CFD simulations',
    author='Delta34',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'vtk'
    ],
)
