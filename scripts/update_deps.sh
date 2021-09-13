#!/usr/bin/env bash

# Assumes venv is activated.

# Turn on bash strict mode.
set -euxo pipefail

cookiecutter_dir=\{\{cookiecutter.repo\}\}

# Delete dep files.
rm -rf $cookiecutter_dir/requirements-*.txt

# Install dev dependencies.
pip install pip-tools

# Update the deps.
pip-compile $cookiecutter_dir/requirements.in \
-o $cookiecutter_dir/requirements.txt &&\

pip-compile $cookiecutter_dir/requirements-dev.in \
-o $cookiecutter_dir/requirements-dev.txt
