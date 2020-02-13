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


tests_require = [
    'check-manifest>=0.40',
    'coverage>=4.5',
    'coveralls>=1.8',
    'pytest>=5.0.0,<6.0.0',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pylint>=2.4,<3',
    'isort>4.3',
]

extras_require = {
    "docs": [
        'bdc-readthedocs-theme @ git+git://github.com/brazil-data-cube/bdc-readthedocs-theme.git#egg=bdc-readthedocs-theme',
        'Sphinx>=2.1.2',
    ],
    "tests": tests_require
}

extras_require['all'] = [req for exts, reqs in extras_require.items() for req in reqs]

install_require = [
    'Flask>=1.0.3,<2',
    'flask-restplus>=0.12.1,<1',
    'Flask-JWT>=0.3.2',
    'jsonschema>=3.0.1',
    'secure-smtplib==0.1.1',
    'Mako==1.1.1',
    # Temp workaround https://github.com/noirbizarre/flask-restplus/issues/777
    'Werkzeug==0.16.1'
]

here = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(here, 'bdc_core', 'version.py'))

g = {}
with open(os.path.join(here, 'bdc_core', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']


setup(
    name='bdc-core',
    version=version,
    description='Brazil Data Cube Core Package',
    author='Admin',
    author_email='admin@admin.com',
    license="MIT",
    packages=find_packages(),
    url='https://github.com/brazil-data-cube/',
    install_requires=install_require,
    extras_require=extras_require,
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
