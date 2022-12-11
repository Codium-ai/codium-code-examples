#!/usr/bin/env bash
set -e
set -x

pipenv run isort --profile black --skip *.lock $1
pipenv run black $1
