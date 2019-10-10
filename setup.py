#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='bdc_core',
    version='0.3',
    description='Brazilian Data Cube Core Package',
    author='Admin',
    author_email='admin@admin.com',
    license="MIT",
    packages=find_packages(),
    url='https://github.com/brazil-data-cube/',
    install_requires=[
        'Flask==1.0.3',
        'flask-restplus==0.12.1',
        'jsonschema==3.0.1',
        'pytest==5.0.0',
        'Sphinx==2.1.2',
        'Sphinx==2.1.2',
        'Sphinx==2.1.2',
        'bdc_theme @ git+git://github.com/brazil-data-cube/bdc-readthedocs-theme.git',
        'pytest==5.0.0',
        'Werkzeug==0.14.1'
    ]
    
)
