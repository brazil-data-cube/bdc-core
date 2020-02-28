#!/usr/bin/env python

#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

import os
from setuptools import find_packages, setup

readme = open('README.rst').read()

history = open('CHANGES.rst').read()

docs_require = [
    'Sphinx>=2.1',
    'bdc-readthedocs-theme @ git+git://github.com/brazil-data-cube/bdc-readthedocs-theme.git#egg=bdc-readthedocs-theme',
]

tests_require = [
    'check-manifest>=0.40',
    'coverage>=4.5',
    'coveralls>=1.8',
    'pydocstyle>=4.0',
    'pytest>=5.0.0,<6.0.0',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pylint>=2.4,<3',
    'isort>4.3',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = [req for exts, reqs in extras_require.items() for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

install_require = [
    'Flask>=1.0.3,<2',
    'flask-restplus>=0.12.1,<1',
    'Flask-JWT>=0.3.2',
    'jsonschema>=3.0.1',
    'secure-smtplib==0.1.1',
    'Mako==1.1.1',
    'Werkzeug>=0.16.1,<1', # Temp workaround https://github.com/noirbizarre/flask-restplus/issues/777
]

packages = find_packages()

with open(os.path.join('bdc_core', 'version.py'), 'rt') as fp:
    g = {}
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='bdc-core',
    version=version,
    description='Brazil Data Cube Core Package',
    long_description=readme + '\n\n' + history,
    keywords='JSON Schema Validation, OAuth2 decorator',
    license="MIT",
    author='INPE',
    author_email='gribeiro@dpi.inpe.br',
    url='https://github.com/brazil-data-cube/bdc-core',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={},
    extras_require=extras_require,
    install_requires=install_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
