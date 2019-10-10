#!/usr/bin/env python

from setuptools import find_packages, setup


tests_require = [
    'pytest>=5.0.0,<6.0.0',
]


extras_require = {
    "docs": [
        'bdc-readthedocs-theme @ git+git://github.com/brazil-data-cube/bdc-readthedocs-theme.git@test-pip#egg=bdc-readthedocs-theme',
        'Sphinx>=2.1.2',
    ],
    "tests": tests_require
}


setup(
    name='bdc-core',
    version='0.3',
    description='Brazilian Data Cube Core Package',
    author='Admin',
    author_email='admin@admin.com',
    license="MIT",
    packages=find_packages(),
    url='https://github.com/brazil-data-cube/',
    install_requires=[
        'Flask>=1.0.3',
        'flask-restplus>=0.12.1',
        'Flask-JWT>=0.3.2',
        'jsonschema==3.0.1',
    ],
    extras_require=extras_require,
    tests_require=tests_require
)
