# -*- coding: utf8 -*-

from mocal import db
from datetime import datetime


class DatabaseObject(db.Model):
    __abstract__ = True

    _reservedColumnName = ['id', 'created_at', 'updated_at']

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now() if db else datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now() if db else datetime.now())

    def __init__(self, **kwargs):
        db.Model.__init__(self)
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def save(self, add=False):
        if add:
            db.session.add(self)
            db.session.commit()
            return self.id

        setattr(self, 'updated_at', db.func.now())
        db.session.add(self)
        db.session.commit()
        return None

    def to_json(self):
        pass
       # todo: 完成这个， sql的binary, db.bindparam(), like

    @classmethod
    def from_id(cls, id):
        obj = cls.query.filter_by(id=id).first()
        return obj

    @classmethod
    def from_db(cls, **kwargs):
        if len(kwargs.items()) <= 0:
            return None

        obj = cls.query.filter_by(**kwargs).first()
        return obj

    @classmethod
    def fetch(cls, page=0, count=0, **kwargs):
        if page == 0 and count == 0:
            objs = cls.query.filter_by(**kwargs).all()
        else:
            objs = cls.query.filter_by(**kwargs).order_by(db.desc('id')).paginate(page, count, False).items

        return objs

    # get property
    def get_property(self, k):
        if hasattr(self, k):
            return getattr(self, k)
        return None

    # set property
    def set_property(self, k, v):
        if hasattr(self, k):
            setattr(self, k, v)

    def set_properties(self, **kwargs):
        for k, v in kwargs.items():
            self.set_property(k, v)
