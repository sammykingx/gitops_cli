#!/usr/bin/env bash
#
# A wrapper script to enable the user run the command globally
#
# Author: Iyebhora Samuel (sammykingx)

WARNING='\033[93m'
RUNNER='/opt/gitops_cli/run.py'
END="\033[00m"

if [ "$#" = "0" ]; then
    echo -e "${WARNING}No arguments passed.${END}"
    echo "USAGE: gitops < ..ARGS >"
    exit 1
fi

${RUNNER} "$@"
