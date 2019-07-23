#!/bin/bash

function docker_compose_run() {
    USEROPT="$(id -u):$(id -g)"
    FAILED=NO
    docker-compose build
    docker-compose up -d
    if ! docker-compose run --rm -u "${USEROPT}" "$@" ; then
        FAILED=YES
    fi
    docker-compose down
    if [ "${FAILED}" != "NO" ] ; then
        return 1
    fi
}
