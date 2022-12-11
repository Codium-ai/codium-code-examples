#!/usr/bin/env bash
set -e
set -x

# Note - this (-n - running tests in parallel) assumes we installed pytest-xdist.
pipenv run pytest --ignore=tests/test_sample.py -n 4
