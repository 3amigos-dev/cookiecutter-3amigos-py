#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

PYVER=3.9
OUTPUTDIR="${BASEDIR}/output"

cd "${BASEDIR}"
mkdir -p "${OUTPUTDIR}"
"python${PYVER}" -m cookiecutter -o "${OUTPUTDIR}" --no-input "${BASEDIR}"
