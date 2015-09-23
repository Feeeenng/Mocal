# -*- coding: utf8 -*-

from db import DatabaseObject
from flask_login import UserMixin
from app import login_manager


class UserDBObject(UserMixin, DatabaseObject):
    __tablename__ = 'user'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<User: %r>' % self.name


@login_manager.user_loader
def load_user(uid):
    return UserDBObject.query.get(int(uid))