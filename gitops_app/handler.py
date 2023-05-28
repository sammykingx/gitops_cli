""" This module evaluates user args and calls the corresponding
    action to execute.
"""
import sys

import gitops_app.actions as a

BEGIN: str = '\033[93m'
END: str = '\033[0m'


def handler(args):
    """resolvs the user args to the action module"""

    if args is None:
        sys.exit('{}No argument passed{}'.format(BEGIN, END))

    args = vars(args)

    excludes = ('version', 'help')

    gitops_actions = {
                        'create': a.create_repo,
                        'delete': a.delete_repo,
                        'fetch': a.fetch_repo,
                        'fork': a.fork_repo,
                        'issues': a.issues
            }

    sub_commands = {key: args.get(key) for key in args
                    if key not in excludes and key != 'action'}

    if args.get('action') in gitops_actions:
        print('{}calling appropriate handler{}'.format(BEGIN, END))
        gitops_actions.get(args.get('action'))(sub_commands)
