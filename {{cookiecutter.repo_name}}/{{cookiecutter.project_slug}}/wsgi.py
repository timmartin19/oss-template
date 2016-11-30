"""
You probably don't need to touch this.  It's simply a mechanism
for wsgi to load the application.  The exception is if you
wish to add some WSGI middleware
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from {{ cookiecutter.project_slug }}.manage import init_app

# pylint: disable=invalid-name
app = init_app()
