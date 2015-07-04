# -*- coding: utf8 -*-

from db import DatabaseObject


class UserDBObject(DatabaseObject):
    __tablename__ = 'user'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<User: %r>' % self.name
