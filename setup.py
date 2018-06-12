#!/usr/bin/env python
from setuptools import setup, find_packages


requirements = [
    'numpy',
    'regex',
    'PyStemmer==1.3.0',
]

setup(
    name='tldry',
    version='0.3.0',
    author='Artem Vang',
    author_email='vangogius@gmail.com',
    url='https://github.com/vangaa/tldry',
    description='Automatic text summarizer based on textrank algorithm',
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
