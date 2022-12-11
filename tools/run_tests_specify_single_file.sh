#!/usr/bin/env bash
set -e
set -x

pipenv run pytest tests/test_sample_2.py
