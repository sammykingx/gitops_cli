#!/usr/bin/env bash

# Installation Script for gitops cli tool
#
# This script safely installs the application on the user terminal
# Also note that it asks for your github token during installation
# to enable the smooth running of the application when installed.
#
# Though the token can be skipped during installation (not advised)
# you can still save your token to $APP_PATH with name of file $APP_TOKEN
# The token is needed for authentication purpose by github.
#
# Author: Iyebhora Samuel (sammykingx)

APP_RUNNER="run.py"
APP="gitops_app"
APP_TOKEN="gitops_token"
TERMINAL_RUNNER="gitops.sh"

APP_BIN_DIR="/usr/local/bin"
APP_PATH="/opt/gitops_cli"
APP_WRAPPER="gitops"

CHECK="\033[0;35m"
GOOD="\033[0;32m"
START="\033[0;93m"
END="\033[00m"

echo -e "${START}checking ...${END}"

if [ -d "${APP_PATH}" ]
then
    echo -e "${CHECK}you have previously installed gitops...${END}"
    exit 1

elif [ "${EUID}" -ne 0 ]
then
    echo -e "${CHECK}Please run this script as root user${END}"
    exit 1
fi

echo -e "${GOOD}check completed${END}"

echo -e "${START}installing dependencies ...${END}"

apt-get install -y python3
apt-get install -y python3-pip
pip install -r requirements.txt

echo -e "${GOOD}dependencies succefully installed${END}"

echo -e "${START}installing binaries...${END}"

mkdir -p ${APP_PATH}

cp -r ${APP} ${APP_RUNNER} ${TERMINAL_RUNNER} ${APP_PATH}
chmod +x ${APP_PATH}/${TERMINAL_RUNNER}

read -rsp "Enter your github token (press ENTER to ignore): " TOKEN
echo -e "${TOKEN}" > ${APP_PATH}/${APP_TOKEN}

ln -s ${APP_PATH}/${TERMINAL_RUNNER} ${APP_BIN_DIR}/${APP_WRAPPER}

echo
echo -e "${GOOD}binaries succesfully installed${END}"
