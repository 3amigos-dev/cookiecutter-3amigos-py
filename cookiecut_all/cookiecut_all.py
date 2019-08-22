#!/usr/bin/env python
"""
Run cookiecutter over a series of directories applying updates into them.
"""
from __future__ import absolute_import, division, print_function

import json
import os
import sys

import click
import git
import plumbum

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

__version__ = "0.1"


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option(version=__version__)
@click.argument("basedir")
@click.option("update", "-u", nargs=2, multiple=True)
@click.pass_context
def main(ctxt, basedir, update):
    """
    Main click group handler
    """
    if ctxt.invoked_subcommand is None:
        run_invocation(basedir, update)


@main.command()
@click.argument("basedir")
@click.option("update", "-u", nargs=2, multiple=True)
def invoke(basedir, update):
    """
    Primary command handler
    """
    run_invocation(basedir, update)


def run_invocation(basedir, update):
    """
    Execute the invocation
    """
    if not os.path.isdir(basedir):
        print("Not a directory: %s" % (basedir,))
        sys.exit(1)
    for subdir in os.listdir(basedir):
        subpath = os.path.join(basedir, subdir)
        jsonpath = os.path.join(subpath, "cookiecutter.json")
        ignorepath = os.path.join(subpath, ".cut_all_ignore")
        if os.path.exists(ignorepath):
            print("Ignoring: %s" % (subpath,))
            continue
        if os.path.isfile(jsonpath):
            run_cut(subpath, update)


def run_cut(path, update):
    """
    Run cookiecutter on the target
    """
    cishpath = os.path.join(get_cookiecut_basedir(), "ci.sh")
    check_update(path, update)
    cish = plumbum.local[cishpath]
    _ = cish["cut_cookie", path] & plumbum.FG
    if git.Repo(path).is_dirty():
        print("Modifications exist in {}".format(path), file=sys.stderr)
        sys.exit(1)


def check_update(path, update):
    """
    Automatically record default values for missing keys
    """
    jsonpath = os.path.join(path, "cookiecutter.json")
    with open(jsonpath, "r", encoding="utf-8") as fobj:
        jsonobj = json.load(fobj)
    update = [(key, val) for key, val in update if key not in jsonobj]
    if update:
        with open(jsonpath, "r", encoding="utf-8") as fobj:
            lines = [line.rstrip("\r\n") for line in fobj]
        lines = (
            lines[:-1]
            + ['    "%s": "%s"' % (key, val) for key, val in update]
            + lines[-1:]
        )
        with open(jsonpath, "w", encoding="utf-8") as fobj:
            for line in lines:
                print(line, file=fobj)


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
