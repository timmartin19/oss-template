from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from {{ cookiecutter.project_slug }}.manage import init_app

app = init_app()
