from setuptools import setup, find_packages

setup(
    name="bq_consumer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'google-cloud-bigquery>=3.0.0',
        'pandas>=1.0.0',
        'importlib-metadata>=4.0.0',
    ],
    author="Jonathan Govinda Medrano Salazar",
    description="Librería para consumir datos de BigQuery",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/findepdev/Arquitectura/_git/bq_consumer",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
