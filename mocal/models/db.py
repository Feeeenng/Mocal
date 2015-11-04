# -*- coding: utf8 -*-
import types
from datetime import datetime

from mocal import db


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

    def to_json(self, format='%Y-%m-%d %H:%M:%S'):
        d = {}
        for k, v in self.__dict__.items():
            if k.startswith('_'):
                continue

            if isinstance(v, datetime):
                d[k] = v.strftime(format)
            else:
                d[k] = v
        return d

       # todo: sql的binary, logger， pagenatiom

    @classmethod
    def from_id(cls, id):
        obj = cls.query.filter_by(id=id).first()
        return obj

    @classmethod
    def from_db(cls, **kwargs):
        if len(kwargs.items()) <= 0:
            return None

        expressions = cls.get_filter_params(**kwargs)
        obj = cls.query.filter(*expressions).first()
        return obj

    @classmethod
    def fetch(cls, page=0, count=0, **kwargs):
        if page == 0 and count == 0:
            expressions = cls.get_filter_params(**kwargs)
            objs = cls.query.filter(*expressions).all()
        else:
            expressions = cls.get_filter_params(**kwargs)
            objs = cls.query.filter_by(*expressions).order_by(db.desc('id')).paginate(page, count, False).items
        return objs

    @classmethod
    def get_filter_params(cls, **kwargs):
        expressions = []
        for k, v in kwargs.items():
            if '__' in k:
                key = k.split('__')[0]
                operate = k.split('__')[1]
                if hasattr(cls, key):
                    field = getattr(cls, key)
                    if operate == 'contains':
                        expressions.append(field.contains(v))
                    elif operate == 'gt':
                        expressions.append(field > v)
                    elif operate == 'gte':
                        expressions.append(field >= v)
                    elif operate == 'lt':
                        expressions.append(field < v)
                    elif operate == 'lte':
                        expressions.append(field <= v)
                    elif operate == 'not':
                        expressions.append(field != v)
                    elif operate == 'in':
                        expressions.append(field.in_(v))
                    elif operate == 'not_in':
                        expressions.append(field.notin_(v))
                    elif operate == 'binary':
                        expressions.append(db.compare(field == v))
                    else:
                        raise SyntaxError, '无操作符{0}'.format(operate)
                else:
                    raise SyntaxError, 'models {0}无{1}字段'.format(cls.__name__, key)
            else:
                if hasattr(cls, k):
                    field = getattr(cls, k)
                    expressions.append(field == v)
                else:
                    raise SyntaxError, 'models {0}无{1}字段'.format(cls.__name__, k)

        return expressions


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
