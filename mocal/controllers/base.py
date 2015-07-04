# -*- coding: utf8 -*-
from app import db


class BaseController(object):
    def __init__(self, properties=None):
        self.properties = properties

        if self.properties:
            for k, v in self.properties.items():
                if k.startswith('_'):
                    del self.properties[k]
                    continue
                setattr(self, k, v)

    @classmethod
    def set_dbobject_class(cls, dbobject, object_class):
        setattr(cls, 'dbobject', dbobject)
        setattr(cls, 'object_class', object_class)

    # get one
    @classmethod
    def from_id(cls, id):
        dbobject = cls.dbobject.query.filter_by(id=id).first()
        return None if not dbobject else cls.object_class(dbobject.__dict__)

    @classmethod
    def from_db(cls, **kwargs):
        dbobject = cls.dbobject.query.filter_by(**kwargs).first()
        return None if not dbobject else cls.object_class(dbobject.__dict__)

    # get more
    @classmethod
    def fetch(cls, **kwargs):
        dbobjects = cls.dbobject.query.filter_by(**kwargs).all()
        return [] if not dbobjects else [cls.object_class(dbobject.__dict__) for dbobject in dbobjects]

    # save
    def save(self, add=False):
        if add:
            db_obj = self.__class__.dbobject(**self.properties)
            db_obj.add()
            db.session.commit()
            self = self.__class__.object_class(db_obj.__dict__)
        else:
            db.session.commit()

    # get property
    def get_property(self, k):
        if hasattr(self, k):
            return getattr(self, k)
        return None

    # set property
    def set_property(self, k, v):
        if hasattr(self, k):
            setattr(self, k, v)
            self.__sync_attr_data(k, v)

    def set_properties(self, **kwargs):
        for k, v in kwargs.items():
            self.set_property(k, v)

    def json_data(self):
        return self.properties

    def __sync_attr_data(self, k, v):
        db_obj = self.__class__.dbobject.query.filter_by(id=self.id).first()
        setattr(db_obj, k, v)
        db_obj.add()


def controller_with_dbobject(dbobject_class):
    def _controller_with_dbobject(cls):
        cls.set_dbobject_class(dbobject_class, cls)
        return cls
    return _controller_with_dbobject