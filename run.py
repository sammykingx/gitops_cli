#!/usr/bin/env python3

"""The application entry point"""

from gitops_app import parser
from gitops_app.handler import handler


def main() -> None:
    args = parser.parse_args()

    handler(args)


if __name__ == '__main__':
    main()
