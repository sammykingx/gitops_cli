"""gitops arguments initailizer"""

from argparse import ArgumentParser


NAME: str = 'gitops'
USAGE: str = ' gitops < SUB_COMMAND | OPTIONS >'

parser = ArgumentParser(NAME, USAGE)

parser.add_argument('-v', '--version',
                    dest='version',
                    action='version',
                    version='%(prog)s v0.1.1',
                    help='Display the current version')

sub_parser = parser.add_subparsers(dest='action')

create = sub_parser.add_parser('create',
                               help='creates a github repo')

delete = sub_parser.add_parser('delete',
                               help='deletes a repository')

fetch = sub_parser.add_parser('fetch',
                              help='list repo owned by user')

fork = sub_parser.add_parser('fork',
                             help='forks a github repository')

issues = sub_parser.add_parser('issues',
                               help='List issues in a repository')

create.add_argument('-d',
                    dest='description',
                    type=str,
                    metavar='descritption',
                    help='description for the repo')

create.add_argument('-n',
                    dest='name',
                    type=str,
                    metavar='name',
                    required=True,
                    help='name of repository')

create.add_argument('-p',
                    '--private',
                    action='store_true',
                    help='make repository private')

delete.add_argument('-u',
                    dest='owner',
                    type=str,
                    metavar='user',
                    required=True,
                    help='github user')

delete.add_argument('-r',
                    dest='repo',
                    type=str,
                    metavar='repo',
                    required=True,
                    help='name of repo')

# more options coming for fetch command

fork.add_argument('-o',
                  dest='owner',
                  required=True,
                  type=str,
                  metavar='owner',
                  help='The account owner of the repository')

fork.add_argument('-r',
                  dest='repo',
                  required=True,
                  type=str,
                  metavar='repo',
                  help='Name of repository to fork')

issues.add_argument('-o',
                    dest='owner',
                    type=str,
                    required=True,
                    metavar='owner',
                    help='owner of the repository')

issues.add_argument('-r',
                    dest='repo',
                    type=str,
                    required=True,
                    metavar='repo',
                    help='The name of the repository')

issues.add_argument('-s',
                    dest='state',
                    type=str,
                    choices=['all', 'closed', 'opened'],
                    default='all',
                    metavar='state',
                    help='Specify the state of issues to return')
