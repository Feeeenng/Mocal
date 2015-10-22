# -*- coding: utf8 -*-

from db import DatabaseObject


class ChatMsg(DatabaseObject):
    __tablename__ = 'chat_msg'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<ChatMsg: %r>' % self.id