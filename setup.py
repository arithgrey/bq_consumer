from setuptools import setup, find_packages

setup(
    name="bq_consumer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-cloud-bigquery",
        "pandas"
    ],
    author="Jonathan Govinda Medrano Salazar",
    description="Librería para consumir datos de BigQuery",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arithgrey/bq_consumer",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
