from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

DB = SQLAlchemy()


class _Base(DB.Model):
    __abstract__ = True

    def __repr__(self):
        keys = {key.name: self.getattr(key.name) for key in inspect(self.__class__).primary_key}
        key_repr = ', '.join(['{0}="{1}'.format(k, v) for k, v in keys.items()])
        return '<{0}: {1}>'.format(self.__class__.__name__, key_repr)
