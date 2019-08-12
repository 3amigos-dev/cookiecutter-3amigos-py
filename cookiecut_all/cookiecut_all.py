#!/usr/bin/env python
"""
Run cookiecutter over a series of directories applying updates into them.
"""
from __future__ import absolute_import, division, print_function

import os
import sys

import click
import plumbum

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

__version__ = "0.1"


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.argument("basedir")
@click.pass_context
def main(ctxt, basedir):
    """
    Main click group handler
    """
    if ctxt.invoked_subcommand is None:
        run_invocation(basedir)


@main.command()
@click.argument("basedir")
def invoke(basedir):
    """
    Primary command handler
    """
    run_invocation(basedir)


def run_invocation(basedir):
    """
    Execute the invocation
    """
    if not os.path.isdir(basedir):
        print("Not a directory: %s" % (basedir,))
        sys.exit(1)
    for subdir in os.listdir(basedir):
        subpath = os.path.join(basedir, subdir)
        jsonpath = os.path.join(subpath, "cookiecutter.json")
        if os.path.isfile(jsonpath):
            run_cut(subpath)


def run_cut(path):
    """
    Run cookiecutter on the target
    """
    cishpath = os.path.join(get_cookiecut_basedir(), "ci.sh")
    cish = plumbum.local[cishpath]
    _ = cish["cut_cookie", path] & plumbum.FG


def get_cookiecut_basedir():
    """
    Locate the current directory of this file
    """
    thisdir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
    basedir = os.path.dirname(thisdir)
    return basedir


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
# vim: set ft=python:
