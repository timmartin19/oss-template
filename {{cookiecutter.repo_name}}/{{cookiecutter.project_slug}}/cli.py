"""
The cli command tool for this project.
This should include helpful, common commands for
the application.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

import click
import flask
import sqlalchemy

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }}.wsgi import app

LOG = logging.getLogger(__name__)


@app.cli.command()
def version():
    """
    Displays the version of {{ cookiecutter.repo_name }}
    """
    click.echo('{{ cookiecutter.project_slug}} version: {0}'.format({{ cookiecutter.project_slug }}.__version__))
    click.echo('Flask version: {0}'.format(flask.__version__))
    click.echo('SQLAlchemy version: {0}'.format(sqlalchemy.__version__))
