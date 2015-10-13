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

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def get_usermixin_attr(cls, dbobject):
        obj_dict = {}
        obj_dict.update(dbobject.__dict__)

        class_name = dbobject.__class__.__name__
        if class_name == 'UserDBObject':
            obj_dict['is_authenticated'] = dbobject.is_authenticated
            obj_dict['is_active'] = dbobject.is_active
            obj_dict['is_anonymous'] = dbobject.is_anonymous

        return obj_dict


    @classmethod
    def set_dbobject_class(cls, dbobject, object_class):
        setattr(cls, 'dbobject', dbobject)
        setattr(cls, 'object_class', object_class)

    # get one
    @classmethod
    def from_id(cls, id):
        dbobject = cls.dbobject.query.filter_by(id=id).first()
        return None if not dbobject else cls.object_class(cls.get_usermixin_attr(dbobject))

    @classmethod
    def from_db(cls, **kwargs):
        dbobject = cls.dbobject.query.filter_by(**kwargs).first()
        return None if not dbobject else cls.object_class(cls.get_usermixin_attr(dbobject))

    # get more
    @classmethod
    def fetch(cls, page=0, count=0, **kwargs):
        if page == 0 and count == 0:
            dbobjects = cls.dbobject.query.filter_by(**kwargs).all()
        else:
            dbobjects = cls.dbobject.query.filter_by(**kwargs).order_by(db.desc('id')).paginate(page, count, False).items

        return [] if not dbobjects else [cls.object_class(cls.get_usermixin_attr(dbobject)) for dbobject in dbobjects]

    # save
    def save(self, add=False):
        if add:
            db_obj = self.__class__.dbobject(**self.properties)
            db_obj.add()
            db.session.flush()  # 主要是这里，写入数据库，但是不提交
            item_id = db_obj.id  # 获取自增ID
            db.session.commit()

            self.properties = db_obj.__dict__
            for k, v in self.properties.items():
                if k.startswith('_'):
                    del self.properties[k]
                    continue
                setattr(self, k, v)

            return item_id

        else:
            db.session.commit()

            return True

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
        setattr(db_obj, 'updated_at', db.func.now())
        db_obj.add()


def controller_with_dbobject(dbobject_class):
    def _controller_with_dbobject(cls):
        cls.set_dbobject_class(dbobject_class, cls)
        return cls
    return _controller_with_dbobject