#!/usr/bin/env python

"""
Install distmetric package. 
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="distmetric",
    version="0.0.2",
    description="A package for calculating phylogenetic tree distances",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
    	"pandas",
    	"numpy",
    	"toytree",
        "toyplot",
    ],
)

