#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
`setuptools` Distribution for {{ cookiecutter.py_modulename }}
"""

# System  Imports
import codecs
import os
import re

# External Imports
from setuptools import find_packages, setup

PACKAGE_NAME = '{{ cookiecutter.py_modulename }}'


def load_readme(fname):
    """
    Read the contents of relative `README` file.
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with codecs.open(file_path, encoding='utf-8') as fobj:
        sub = (
            '(https://github.com/'
            '{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo }}'
            '/blob/master/\\g<1>)'
        )
        markdown_fixed = re.sub(
            '[(]([^)]*[.](?:md|rst))[)]',
            sub,
            fobj.read(),
        )
        rst_fixed = re.sub(
            '^[.][.] [_][`][^`]*[`][:] ([^)]*[.](?:md|rst))',
            sub,
            markdown_fixed
        )
        return rst_fixed


def read_version():
    """
    Read the contents of relative file.
    """
    file_path = os.path.join(
        os.path.dirname(__file__), PACKAGE_NAME, 'version.py'
    )
    regex = re.compile('__version__ = [\'\"]([^\'\"]*)[\'\"]')
    with codecs.open(file_path, encoding='utf-8') as fobj:
        for line in fobj:
            mobj = regex.match(line)
            if mobj:
                return mobj.group(1)
    raise Exception('Failed to read version')


setup(
    name=PACKAGE_NAME,
    version=read_version(),
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    maintainer='{{ cookiecutter.maintainer_name }}',
    maintainer_email='{{ cookiecutter.maintainer_email }}',
    packages=find_packages(exclude=['tests']),
    license='{{ cookiecutter.license }}',
    description=(
        '{{ cookiecutter.project_description }}'
    ),
    long_description=load_readme('README.md'),
    long_description_content_type='text/markdown',
    python_requires={% if cookiecutter.supports_pytwo == "yes" %}">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"{% else %}">=3.4"{% endif %},
    install_requires=[
        elem for elem in
        '{{ cookiecutter.app_requirements|replace('\n', '\\n') }}'.split('\n')
        if elem
    ],
    url='{{ cookiecutter.project_url }}',
    classifiers=[elem for elem in [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',{% if cookiecutter.supports_pytwo == "yes" %}
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',{% endif %}
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: {% if cookiecutter.license == "GPLv3+"%}GNU General Public License v3 (GPLv3){% else %}MIT{% elif cookiecutter.license == "MIT" %}MIT License{% endif %}',
    ] if elem],
)
