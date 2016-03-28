# -*- coding: utf8 -*-

from db import DatabaseObject
from mocal.utils.datetime_display import now_lambda


class Topic(DatabaseObject):
    __tablename__ = 'topic'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<Topic: %r>' % self.id

    def is_marked(self, uid):
        ut = UserTopics.from_db(uid=uid, tid=self.id, deleted_at=None)
        if ut:
            return True
        return False


class UserTopics(DatabaseObject):
    __tablename__ = 'user_topics'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<UserTopics: %r>' % self.id

    def cancel(self):
        self.deleted_at = now_lambda()