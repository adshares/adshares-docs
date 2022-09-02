#!/usr/bin/env bash

# Usage: build.sh [<work-dir>]
cd ${1:-"."}

make html
