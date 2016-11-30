"""
Default settings for the application.  All top level module
attributes will be loaded as configuration
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {  # default logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '{{ cookiecutter.project_slug }}': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'flask': {
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        },
        'sqlalchemy': {
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        }
    }
}

DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
