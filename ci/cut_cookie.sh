#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

source "${BASEDIR}/ci/shared/_docker_helper.sh"

if ! which git ; then
    echo 'git is missing! needed for this command' >&2
    exit 1
fi

OUTPUTDIR="${1}"
if [ -d "${OUTPUTDIR}" ] ; then
    cd "${OUTPUTDIR}" 
    if [ $(git status -s | wc -l) -ne 0 ] ; then
        echo 'Modified Files exist in target - aborting!' >&2
        exit 1
    fi
    find . -maxdepth 1 -mindepth 1 -a ! -ipath ./.git -a ! -ipath ./cookiecutter.json -exec rm -rf \{\} \;
fi
if [ -e "${OUTPUTDIR}/cookiecutter.json" ] ; then
    cp "${BASEDIR}/cookiecutter.json" "${BASEDIR}/orig_cookiecutter.json"
    cp "${OUTPUTDIR}/cookiecutter.json" "${BASEDIR}"
fi

# Remove any old content
rm -rf "${BASEDIR}/output"

cd "${BASEDIR}"
docker_compose_run app "/workspace/ci/in_docker/cut_cookie.sh"
cd "${BASEDIR}/output/"*
find . -maxdepth 1 -mindepth 1 -exec cp -r \{\} "${OUTPUTDIR}" \;
if [ -e "${OUTPUTDIR}/orig_cookiecutter.json" ] ; then
    mv "${BASEDIR}/orig_cookiecutter.json" "${BASEDIR}/cookiecutter.json" 
fi
