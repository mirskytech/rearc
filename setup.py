#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'antlr4-python3-runtime'
]

setup_requirements = [
    'pytest-runner',
    'setuptools-antlr'
]

test_requirements = [
    'pytest',
]

setup(
    name='rearc',
    version='0.1.0',
    description="Recompiler to turn linear GCodes (G0/G1) into arc GCodes (G2/G3)",
    long_description=readme + '\n\n' + history,
    author="Andrew Mirsky",
    author_email='andrew@mirsky.net',
    url='https://github.com/ajmirsky/rearc',
    packages=find_packages(include=['rearc']),
    entry_points={
        'console_scripts': [
            'rearc=rearc.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='rearc',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
