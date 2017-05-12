"""
Contains the SQLAlchemy database modules for
the application. See the `SQLAlchemy docs <http://sqlalchemy.org>`_
for more detail
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import RelationshipProperty{% if cookiecutter.user == 'y'%}, relationship
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Enum
from flask_user import UserMixin, SQLAlchemyAdapter, UserManager
import enum{% endif %}

LOG = logging.getLogger(__name__)
DB = SQLAlchemy()
MIGRATE = Migrate(db=DB)


class _Base(DB.Model):
    """
    A base model that includes common methods for
    all models (primarily pretty printing)
    """
    __abstract__ = True
    excluded_columns = frozenset()
    included_columns = frozenset()

    def __repr__(self):
        keys = {key.name: getattr(self, key.name) for key in inspect(self.__class__).primary_key}
        key_repr = ', '.join(['{0}="{1}"'.format(k, v) for k, v in keys.items()])
        return '<{0}: {1}>'.format(self.__class__.__name__, key_repr)

    def _included_column(self, column_name, column_val, explicit_exclude, explicit_include):
        if column_name in explicit_exclude:
            return False
        if column_name in explicit_include:
            return True
        if column_name in self.excluded_columns:
            return False
        if column_name in self.included_columns:
            return True
        return not isinstance(column_val.property, RelationshipProperty)

    def _get_col(self, column_name, column_value):
        val = getattr(self, column_name)
        if not isinstance(column_value.property, RelationshipProperty):
            return val
        try:
            return [model.to_dict() for model in val]
        except TypeError:
            return val.to_dict()

    def to_dict(self, ignored_cols=None, included_cols=None):
        resp = {}
        ignored_cols = ignored_cols or set()
        included_cols = included_cols or set()
        for column, value in self._sa_class_manager.items():
            if self._included_column(column, value, ignored_cols, included_cols):
                resp[column] = self._get_col(column, value)
        return resp


{% if cookiecutter.user == 'y' %}
class User(_Base, UserMixin):
    __tablename__ = 'users'
    excluded_columns = frozenset(['password'])

    id = Column(Integer, primary_key=True)

    # User authentication information
    password = Column(String(255), nullable=True, server_default='')

    # User email information
    email = Column(String(255), nullable=False, unique=True)
    confirmed_at = Column(DateTime())

    stripe_customer_id = Column(String(255), nullable=True)
    stripe_subscription_id = Column(String(255), nullable=True)
    stripe_subscription_active = Column(Boolean, default=False, nullable=False)

    # User information
    active = Column('is_active', Boolean(), nullable=False, server_default='0')
    first_name = Column(String(100), nullable=False, server_default='')
    last_name = Column(String(100), nullable=False, server_default='')

    oauth_providers = relationship(lambda: UserOauthProvider, backref='user', lazy='joined')


class OauthEnum(enum.Enum):
    facebook = 'facebook'
    google = 'google'


class UserOauthProvider(_Base):
    __tablename__ = 'user_oauth_provider'

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    provider = Column(Enum(OauthEnum), nullable=False, primary_key=True)


_DB_ADAPTER = SQLAlchemyAdapter(DB, User)
USER_MANAGER = UserManager(_DB_ADAPTER)
{% endif %}