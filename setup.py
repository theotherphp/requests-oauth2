#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.2.1'

setup(
    name='requests-oauth2',
    version=version,
    description='Open Authentication 2 support to Python-requests HTTP library.',
    long_description=open('README.md').read(),
    author='Miguel Araujo',
    author_email='miguel.araujo.perez@gmail.com',
    url='http://github.com/maraujop/requests-oauth2',
    packages=find_packages(),
    install_requires=['requests', ],
    license='BSD',
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    keywords=['requests', 'python-requests', 'OAuth', 'open authentication'],
    zip_safe=False,
)
