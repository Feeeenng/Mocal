# -*- coding: utf8 -*-

from db import DatabaseObject, db


class UserInfo(DatabaseObject):
    __tablename__ = 'user_info'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 一对一， uselist=False
    user = db.relationship('User', backref=db.backref('user_info', lazy='select', uselist=False))

    def __repr__(self):
        return '<UserInfo: %r>' % self.id
