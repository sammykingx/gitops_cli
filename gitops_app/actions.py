"""This module contains all actions for gitops_cli app"""

import requests as req
import sys

from typing import Dict


TOKEN_PATH: str = '/opt/gitops_cli/gitops_token'
CREATE_REPO_END_POINT: str = 'https://api.github.com/user/repos'
DEL_REPO_END_POINT: str = 'https://api.github.com/repos'
FETCH_REPO_END_POINT: str = 'https://api.github.com/user/repos'
FORK_REPO_END_POINT: str = 'https://api.github.com/repos/{}/{}/forks'
ISSUES_END_POINT: str = 'https://api.github.com/repos/{}/{}/issues'

PAYLOAD = Dict[str, str]
TIMEOUT: int = 7

DISPLAY: str = '\033[36m'
ERROR: str = '\033[31m'
GOOD: str = '\033[32m'
WARNING: str = '\033[93m'
END: str = '\033[0m'

try:
    with open(TOKEN_PATH, 'r') as fd:
        TOKEN = fd.readline().rstrip('\n')

except FileNotFoundError as err:
    print('{}could not read your token from {}{}'
          .format(WARNING, TOKEN_PATH, END))

    sys.exit(1)


HEADERS: str = {'Accept': 'application/vnd.github+json',
                'Authorization': 'Bearer {}'.format(TOKEN),
                'X-Github-Api-Version': '2022-11-28'}


def checks(payload) -> PAYLOAD:
    """Checks if payload is empty"""
    if payload is None:
        sys.exit('{}no data to execute{}'.format(WARNING, END))


def create_repo(payload: PAYLOAD) -> None:
    "Creates a repository for the authenticated user"

    checks(payload)

    try:
        res = req.post(CREATE_REPO_END_POINT,
                       headers=HEADERS,
                       json=payload,
                       timeout=TIMEOUT)

    except res.Timeout:
        sys.exit('{}Server took too long to respond{}'
                 .format(WARNING, END))

    except req.ConnectionError:
        sys.exit('{}Could not establish a connection{}'
                 .format(WARNING, END))

    if res.status_code != 201:
        sys.exit('{}could not execute action: Status code {}{}'
                 .format(ERROR, res.status_code, END))

    print('{}Repository Successfully created{}'.format(GOOD, END))
    print('==> repo url {}'.format(res.json()['html_url']))


def delete_repo(payload: PAYLOAD) -> None:
    "Deletes a repository for the authenticated user"

    checks(payload)

    owner = payload.get('owner')
    repo = payload.get('repo')

    url = '{}/{}/{}'.format(DEL_REPO_END_POINT, owner, repo)

    try:
        res = req.delete(url, headers=HEADERS, timeout=TIMEOUT)

    except res.Timeout:
        sys.exit('{}Server took too long to respond{}'
                 .format(WARNING, END))

    except req.ConnectionError:
        sys.exit('{}Could not establish a connection{}'
                 .format(WARNING, END))

    if res.status_code != 204:
        sys.exit('{}could not execute action: Status code {}{}'
                 .format(ERROR, res.status_code, END))

    print('{}Repo Succesfully deleted for user {}{}'
          .format(GOOD, owner, END))


def fetch_repo(payload: PAYLOAD) -> None:
    """list available user repository from github"""

    checks(payload)

    owner = payload.get('user')
    repo = payload.get('repo')

    try:
        res = req.get(FETCH_REPO_END_POINT,
                      headers=HEADERS,
                      timeout=TIMEOUT)

    except res.Timeout:
        sys.exit('{}Server took too long to respond{}'
                 .format(WARNING, END))

    except req.ConnectionError:
        sys.exit('{}Could not establish a connection{}'
                 .format(WARNING, END))

    if res.status_code == 401:
        sys.exit('{}Authentication failed, check your token{}'
                 .format(WARNING, END))

    elif res.status_code != 200:
        sys.exit('{}Could not execute action: status code {}{}'
                 .format(ERROR, res.status_code, END))

    print('{}Sucessfull ...{}'.format(GOOD, END))

    for data in res.json():
        print('{}repo name: {}{}'
              .format(DISPLAY, data['name'], END))

        print('repo url: {}\n'.format(data['html_url']))


def fork_repo(payload: PAYLOAD) -> None:
    """forks repo from a gituser"""

    checks(payload)

    url = FORK_REPO_END_POINT.format(payload.get('owner'),
                                     payload.get('repo'))

    try:
        res = req.post(url, headers=HEADERS, timeout=TIMEOUT)

    except res.Timeout:
        sys.exit('{}Server took too long to respond{}'
                 .format(WARNING, END))

    except req.ConnectionError:
        sys.exit('{}Could not establish connection with server{}'
                 .format(ERROR, END))

    if res.status_code != 202:
        print('{}Could not perform action: status code {}{}'
              .format(ERROR, res.status_code, END))
        sys.exit(1)

    print('{}succesfully forked repo {}{}'
          .format(GOOD, payload.get('repo'), END))

    print('new url: {}'.format(res.json()['html_url']))


def issues(payload: PAYLOAD) -> None:
    """checks issues on a repository"""

    checks(payload)

    url = ISSUES_END_POINT.format(payload.get('owner'),
                                  payload.get('repo'))

    try:
        res = req.get(url, headers=HEADERS, timeout=TIMEOUT)

    except res.Timeout:
        sys.exit('{}Server took too long to respond{}'
                 .format(WARNING, END))
    except req.ConnectionError:
        sys.exit('{}Could not establish connection with server{}'
                 .format(ERROR, END))

    if res.status_code != 200:
        print('{}Could not execute action: Status code {}{}'
              .format(WARNING, res.status_code, END))

    print('{}Successfull!!{}'.format(GOOD, END))
