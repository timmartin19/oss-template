"""
The view in MVC
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from flask import Blueprint, Response
from status_checker import StatusChecker
import ujson

import {{ cookiecutter.project_slug }}

{% set blueprint = '{0}_BLUEPRINT'.format(cookiecutter.project_slug.upper()) %}
LOG = logging.getLogger(__name__)
{{ blueprint }} = Blueprint('{{ cookiecutter.project_slug|lower }}', __name__)


def _check_database():
    """
    Checks if the database is available

    :return: Return a dictionary with at least
        a key 'available' corresponding to a boolean
    :rtype: dict{str:object}
    """
    # TODO: Test the connection and ensure the database is running and reachable
    return {'available': True}

_STATUS_CHECKER = StatusChecker(database=_check_database)


@{{ blueprint }}.route('/status', methods=['GET'])
def status():
    """
    Gets the status of this service and its dependencies
    """
    status_dict = _STATUS_CHECKER.status()
    status_code = 200 if status_dict['failure_count'] == 0 else 500
    return Response(ujson.dumps(status_dict), status=status_code, content_type='application/json')


@{{ blueprint }}.route('/version', methods=['GET'])
def version():
    """
    Gets the version of this service
    """
    version_info = {'version': {{ cookiecutter.project_slug }}.__version__}
    return Response(ujson.dumps(version_info), status=200, content_type='application/json')
