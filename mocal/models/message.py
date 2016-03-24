# -*- coding: utf8 -*-

from db import DatabaseObject

TEXT = 1
IMAGE = 2
MSG_TYPE = [
    (TEXT, '文本'),
    (IMAGE, '图片')
]
MSG_TYPE_DICT = dict(MSG_TYPE)


class Message(DatabaseObject):
    __tablename__ = 'message'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<Message: %r>' % self.id