#!/usr/bin/env python
import os
from subprocess import call

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def init_git_repo():
    call(['git', 'init'])
    call(['git', 'add', '.'])
    call(['git', 'commit', '-m', 'created project from github.com/timmartin19/cookiecutter-pypackage'])


if __name__ == '__main__':
    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    init_git_repo()

    #
    # if '{{ cookiecutter.init_open_source }}' == 'y':
    #     os.system('bin/init-open-source.sh')
