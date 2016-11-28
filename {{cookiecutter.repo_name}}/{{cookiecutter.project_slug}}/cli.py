"""
The cli command tool for this project.
This should include helpful, common commands for
the application.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import click

import {{ cookiecutter.project_slug }}


@click.group()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    pass


@main.command()
def version():
    """
    Displays the version of {{ cookiecutter.repo_name }}
    """
    click.echo({{ cookiecutter.project_slug }})


if __name__ == "__main__":
    main()
