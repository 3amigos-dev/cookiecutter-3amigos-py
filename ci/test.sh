#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "${THISDIR}" )"

source "${BASEDIR}/ci/shared/_docker_helper.sh"

# Remove any old content
rm -rf "${BASEDIR}/output"

docker_compose_run app "/workspace/ci/in_docker/test.sh" "$@"

# Test produced cookie cutter output
"${BASEDIR}/output/otherpymodulenamegoeshere/ci.sh" test
