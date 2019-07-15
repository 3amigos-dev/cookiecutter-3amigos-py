#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

PYVER=3.7

cd "${BASEDIR}"
mkdir -p "${BASEDIR}/output"
"python${PYVER}" -m cookiecutter -o "${BASEDIR}/output" --no-input "${BASEDIR}"
