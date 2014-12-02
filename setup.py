#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
        name = "pyfoo",
        version = "",
        description = 'Python wrapper around the Wufoo API',
        long_description = open('README.markdown').read(),
        author = '',
        author_email = '',
        keywords = 'python',
        classifiers = [
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python 2',
            'Programming Language :: Python 2.7',
            ],
        packages = find_packages(),
        include_package_data = True,
        )       
