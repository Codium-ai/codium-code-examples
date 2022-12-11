#!/usr/bin/env bash
set -e
set -x

isort . --sp .isort.cfg
# TODO: This configuration should move to a py-project file.
black . --config .black
flake8
