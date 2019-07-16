#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

cp "${BASEDIR}/README.md" "${BASEDIR}/{{ cookiecutter.docker_application_dirname }}/README.md"
cp "${BASEDIR}/LICENSE" "${BASEDIR}/{{ cookiecutter.docker_application_dirname }}/LICENSE"

MAIN_MODULE="{{ cookiecutter.py_modulename }}"
MODULES=( "${MAIN_MODULE}" "tests" )
