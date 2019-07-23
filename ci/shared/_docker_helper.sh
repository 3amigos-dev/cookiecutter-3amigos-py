#!/bin/bash

function docker_compose_run() {
    USEROPT="$(id -u):$(id -g)"
    FAILED=NO
    if ! docker-compose build ; then
        FAILED=YES
    fi
    if [ "${FAILED}" == "NO" ] ; then
        if ! docker-compose up -d ; then
            FAILED=YES
        fi
        if [ "${FAILED}" == "NO" ] ; then
            if ! docker-compose run --rm -u "${USEROPT}" "$@" ; then
                FAILED=YES
            fi
        fi
        if ! docker-compose down ; then
            FAILED=YES
        fi
    fi
    if [ "${FAILED}" != "NO" ] ; then
        return 1
    fi
}
