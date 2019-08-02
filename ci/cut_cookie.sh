#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

# shellcheck source=/dev/null
source "${BASEDIR}/ci/shared/_docker_helper.sh"

if ! which git ; then
    echo 'git is missing! needed for this command' >&2
    exit 1
fi

RESET="NO"
POSITIONAL=()

##################################
# Parsing Command line arguments
#################################
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -r|--reset)
    shift # past argument
    RESET="YES"
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

OUTPUTDIR="${1}"
if [ -d "${OUTPUTDIR}" ] ; then
    cd "${OUTPUTDIR}" 
    # Fix relative links
    OUTPUTDIR=$(pwd)
    rm -f "${BASEDIR}/target_cookiecutter.json"
    if [ -e "${OUTPUTDIR}/cookiecutter.json" ] ; then
        cp "${OUTPUTDIR}/cookiecutter.json" "${BASEDIR}/target_cookiecutter.json"
    fi
    function finish_target() {
        if [ -e "${BASEDIR}/target_cookiecutter.json" ] ; then
            mv "${BASEDIR}/target_cookiecutter.json" "${OUTPUTDIR}/cookiecutter.json"
        fi
    }
    trap finish_target EXIT
    git checkout -- cookiecutter.json
    if [ "${RESET}" == "YES" ] ; then
        git checkout -- .
        git clean -f -d
    fi
    if [ "$(git status -s | wc -l)" -ne 0 ] ; then
        set +x
        echo '-----------'
        echo '-----------'
        echo '-----------'
        echo 'Modified Files exist in target - aborting!' >&2
        git status -s >&2
        echo '-----------'
        echo '-----------'
        echo '-----------'
        exit 1
    fi
    if [ -e "${BASEDIR}/target_cookiecutter.json" ] ; then
        mv "${BASEDIR}/target_cookiecutter.json" "${OUTPUTDIR}/cookiecutter.json"
    fi
    find . -maxdepth 1 -mindepth 1 -a ! -ipath ./.git -a ! -ipath ./hooks -a ! -ipath ./cookiecutter.json -exec rm -rf \{\} \;
fi
if [ -e "${OUTPUTDIR}/cookiecutter.json" ] ; then
    cp "${BASEDIR}/cookiecutter.json" "${BASEDIR}/orig_cookiecutter.json"
    cp "${OUTPUTDIR}/cookiecutter.json" "${BASEDIR}"
fi
function finish() {
    if [ -e "${BASEDIR}/orig_cookiecutter.json" ] ; then
        mv "${BASEDIR}/orig_cookiecutter.json" "${BASEDIR}/cookiecutter.json" 
    fi
}
trap finish EXIT

# Remove any old content
rm -rf "${BASEDIR}/output"

cd "${BASEDIR}"
if ! docker_compose_run app "/workspace/ci/in_docker/cut_cookie.sh" ; then
    echo 'Cookie Template Failed! Restoring...'
    cd "${OUTPUTDIR}"
    git checkout -- .
    exit 1
fi
cd "${BASEDIR}/output/"*
find . -maxdepth 1 -mindepth 1 -exec cp -r \{\} "${OUTPUTDIR}" \;
if [ -e "${OUTPUTDIR}/hooks/post_gen_project.sh" ] ; then
    "${OUTPUTDIR}/hooks/post_gen_project.sh"
fi
