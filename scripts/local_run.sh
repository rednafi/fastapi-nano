#!/usr/bin/env bash

# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

target_folder=\{\{cookiecutter.repo\}\}

# Delete dep files.
rm -rf $target_folder/requirements-*.txt

# Install dev dependencies.
pip install pip-tools

# Update the deps.
pip-compile $target_folder/requirements.in -o $target_folder/requirements.txt &&\
pip-compile $target_folder/requirements-dev.in -o $target_folder/requirements-dev.txt
