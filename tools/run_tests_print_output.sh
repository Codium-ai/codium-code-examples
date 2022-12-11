#!/usr/bin/env bash
set -e
set -x

# `-sv` - convenince for allowing printing done during test run
pipenv run pytest -sv
