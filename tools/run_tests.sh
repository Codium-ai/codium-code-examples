#!/usr/bin/env bash
set -e
set -x

# -rP - display extra information on all non-passing tests. See:
#   https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags
# -n 4 - running tests in parallel. Assumes we installed pytest-xdist.
pipenv run pytest -rP -n 4
