""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from setuptools import find_packages, setup
import os


build_num = os.environ.get("BUILD_NUMBER", 1)

release_verion='1.0.0'

setup(
    name='fortisoar-connector-engine',
    packages=find_packages(include=['connectors', 'connectors.core', 'connectors.scripts', 'integrations']),
    version=f'{release_verion}-{build_num}',
    py_modules=['setupnovernormalize'],
    description='FortiSOAR Connector Engine Library',
    author='Fortinet',
    url='https://github.com/fortinet-fortisoar/fortisoar-connector-engine',
    license='MIT',
    install_requires=["requests", "markdown2", "pytest"],
    package_data={'connectors.scripts': ['config/*', ]}
)
