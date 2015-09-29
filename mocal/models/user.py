# -*- coding: utf8 -*-

from db import DatabaseObject
from flask_login import UserMixin


class UserDBObject(UserMixin, DatabaseObject):
    __tablename__ = 'user'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<User: %r>' % self.name
