#!/usr/bin/env bash
set -e

rm Pipfile.lock || True  && pipenv lock --clear && pipenv install --dev
