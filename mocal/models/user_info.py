# -*- coding: utf8 -*-

from db import DatabaseObject, db
from mocal.utils.datetime_display import format_datetime


class UserInfo(DatabaseObject):
    __tablename__ = 'user_info'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 一对一， uselist=False
    user = db.relationship('User', backref=db.backref('user_info', lazy='select', uselist=False))

    def __repr__(self):
        return '<UserInfo: %r>' % self.id

    @property
    def birth(self):
        return format_datetime(self.birthday, '%Y-%m-%d') or '保密'