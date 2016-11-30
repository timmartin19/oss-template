"""
Contains code that dictates the creation
of a Flask WSGI object.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from logging import config

from flask import Flask
from ultra_config import GlobalConfig
{% set blueprint = '{0}_BLUEPRINT'.format(cookiecutter.project_slug.upper()) %}
from {{ cookiecutter.project_slug }}.views import {{ blueprint }}
from {{ cookiecutter.project_slug }}.models import DB
from {{ cookiecutter.project_slug }} import default_settings

LOG = logging.getLogger(__name__)


def init_app(config_override=None):
    """
    Initializes a Flask application object

    :param dict config_override: Overrides for the configuration
    :return: A flask application object (which is a wsgi callable as well
    :rtype: Flask
    """
    app = Flask('{{ cookiecutter.project_slug }}')
    app = _load_configuration(app, overrides=config_override)
    _init_logging()
    app = _register_blueprints(app)
    app = _init_db(app)
    return app


def _init_db(app):
    """
    Initializes the database

    :rtype: Flask
    """
    DB.init_app(app)
    return app


def _register_blueprints(app):
    """
    Registers the necessary blueprints on the application

    :param Flask app:
    :return: The app with the registered blueprints
    :rtype: Flask
    """
    app.register_blueprint({{ blueprint }}, url_prefix='')
    return app


@GlobalConfig.inject(logging_conf='LOGGING_CONFIG')
def _init_logging(logging_conf=None):
    """
    Initializes the logging from the configuration
    See the `docs <https://docs.python.org/3.5/library/logging.config.html>`_

    :param dict logging_conf:
    :rtype: None
    """
    config.dictConfig(logging_conf)


def _load_configuration(app, overrides=None):
    """
    Loads the configuration into a GlobalConfiguration object.

    It uses and overrides configuration in the following manner:
    - default settings
    - env variable prefix (any environment variable starting with {{ cookiecutter.project_slug|upper }}
    - overrides

    :param Flask app: The application to load the configuration to
    :param dict overrides: Configuration to explicitly override
    :return:
    :rtype: Flask
    """
    required_parameters = [
        'SQLALCHEMY_DATABASE_URI'
    ]
    GlobalConfig.load(default_settings=default_settings,
                      env_var_prefix='{{ cookiecutter.project_slug|upper }}',
                      overrides=overrides,
                      required=required_parameters)
    app.config.update(GlobalConfig.config)
    app.debug = GlobalConfig.config['DEBUG']
    return app


if __name__ == '__main__':
    # pylint: disable=invalid-name
    {{ cookiecutter.project_slug }}_app = init_app({'DEBUG': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite://'})
    with {{ cookiecutter.project_slug }}_app.app_context():
        DB.create_all()
    {{ cookiecutter.project_slug }}_app.run('0.0.0.0', port=5000, debug=True)
