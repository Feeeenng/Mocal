# -*- coding: utf8 -*-

from db import DatabaseObject


class Upload(DatabaseObject):
    __tablename__ = 'upload'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<Upload: %r>' % self.id
