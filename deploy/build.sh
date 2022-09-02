#!/usr/bin/env bash

# Usage: build.sh [<work-dir>]
cd ${1:-"."}

source .venv/bin/activate
make html
deactivate
