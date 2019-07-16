#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

source "${BASEDIR}/ci/shared/_docker_helper.sh"

docker_compose_run {{ cookiecutter.docker_application_tagname }} "/{{ cookiecutter.docker_workspace_dirname }}/ci/in_docker/news.sh" "$@"
