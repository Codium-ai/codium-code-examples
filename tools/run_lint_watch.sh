#!/usr/bin/env bash
set -e
set -x

## NOTES:
# Uses nodemon:
# npm install -g nodemon
# 

nodemon --ext py --exec "pipenv run flake8"
