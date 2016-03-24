# -*- coding: utf8 -*-

from db import DatabaseObject
from mocal.utils.datetime_display import format_datetime

class Topic(DatabaseObject):
    __tablename__ = 'topic'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<Topic: %r>' % self.id

    @property
    def created_ed_str(self):
        return format_datetime(self.created_at)