#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py

import os
import re
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='weejee',
    license='TBD',
    description='weejee: a board game collection oracle',
    long_description='TBD',
    author='Jason Walker',
    author_email='jason@onetrue.name',
    url='TBD',
    
    packages=['weejee'],
#    package_dir={'weejee': 'src/weejee'},
    package_data={'': ['LICENSE'] },
    include_package_data=True,
    
    scripts=[
        'bin/dump',
        'bin/scores',
        'bin/stats'
    ],
    
    install_requires=[
        'boardgamegeek2'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],

    zip_safe=False,
    classifiers=(),
    extras_require={},
)