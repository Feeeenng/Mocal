# -*- coding: utf8 -*-

from mocal.app import db
from datetime import datetime

class DatabaseObject(db.Model):
    __abstract__ = True

    _reservedColumnName = ['id', 'created_at', 'updated_at']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now() if db else datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now() if db else datetime.now())

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def add(self):
        db.session.add(self)

