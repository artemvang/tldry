#!/usr/bin/env python
from setuptools import setup, find_packages


requirements = [
    "numpy>=1.14.3",
    "PyStemmer==1.3.0",
    "regex>=2018.2.21",
]

setup(
    name="tldry",
    version="0.1.0",
    description="Automatic text summarizer using BM25 and textrank",
    install_requires=requirements,
    packages=find_packages('.', exclude='tests'),
)
