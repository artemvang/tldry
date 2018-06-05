#!/usr/bin/env python
from setuptools import setup, find_packages


requirements = [
    'numpy>=1.14.3',
    'PyStemmer==1.3.0',
    'regex>=2018.2.21',
]

setup(
    name='tldry',
    version='0.1.1',
    author='Artem Vang',
    author_email='vangogius@gmail.com',
    url='https://github.com/vangaa/tldry',
    description='Automatic text summarizer using BM25 and textrank',
    license='MIT License',
    install_requires=requirements,
    packages=find_packages('.', exclude='tests'),
    classifiers=(
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: CPython',
    )
)
