#!/bin/bash

# automatically update dependencies and run the tests
# assumes venv is activated

# set command echo
set -euxo pipefail

# install cookiecutter
pip install cookiecutter

# create concrete project from cookie cutter
cookiecutter https://github.com/rednafi/fastapi-nano.git --no-input

# install dependencies
cd fastapi-nano &&\
pip install -r requirements-dev.txt &&\
pip install -r requirements.txt &&\
cd ..

# upgrade dependencies
cd fastapi-nano && \
pip-compile --upgrade requirements-dev.txt && \
pip-compile --upgrade requirements.txt && \
cd ..

# sync venv according to the upgraded dependencies
cd fastapi-nano && \
pip-sync requirements-dev.txt requirements.txt &&
cd ..

# run the tests
pytest fastapi-nano

# copy dependencies
cp fastapi-nano/requirements.txt  \{\{cookiecutter.repo\}\}/ && \
cp fastapi-nano/requirements-dev.txt \{\{cookiecutter.repo\}\}/

# cleanup
rm -rf fastapi-nano

# turn off command echo
set +x
