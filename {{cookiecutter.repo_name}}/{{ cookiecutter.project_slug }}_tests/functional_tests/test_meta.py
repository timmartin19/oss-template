"""
Unit tests intended to help test the meta endpoints of
the application: e.g. `/version` and `/status`
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import ujson
from webtest import TestApp

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }}.manage import init_app


class TestMetaFunctional(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = init_app()
        cls.test_app = TestApp(app)

    def test_status(self):
        resp = self.test_app.get('/status')
        self.assertEqual(200, resp.status_code)

    def test_version(self):
        resp = self.test_app.get('/version')
        self.assertEqual(200, resp.status_code)
        data = ujson.loads(resp.body)
        self.assertEqual({{ cookiecutter.project_slug }}.__version__, data['version'])
