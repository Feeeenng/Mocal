# -*- coding: utf8 -*-
from __future__ import unicode_literals
from datetime import datetime
import random
from mocal.utils.string_utils import get_upper_letter
from mongoengine import *
from mongoengine import signals


def create_document_id(class_name, id_prefix=None):
    remain_str = '{0}{1}'.format(datetime.now().strftime('%Y%m%d%H%M%S'), str(random.randint(100, 999)))
    if id_prefix:
        id = '{0}{1}'.format(id_prefix.upper(), remain_str)
    else:
        name = get_upper_letter(class_name)
        id = '{0}{1}'.format(name, remain_str)
    return id


def register_pre_save(id_prefix=None):
    def _decorate(clazz):
        if id_prefix:
            clazz.id_prefix = id_prefix
        signals.pre_save.connect(clazz.pre_save, sender=clazz)
        return clazz
    return _decorate


class MocalBase(Document):
    id = StringField(primary_key=True)
    created_at = DateTimeField(default=None)
    updated_at = DateTimeField(default=None)
    deleted_at = DateTimeField(default=None)

    meta = {
        'abstract': True,
        'strict': False
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if not document.id:
            id_prefix = None
            if hasattr(cls, 'id_prefix'):
                id_prefix = getattr(cls, 'id_prefix')

            document.id = create_document_id(cls.__name__, id_prefix)
            document._created = True
            document.created_at = datetime.now()
        document.updated_at = datetime.now() if document.id and document.updated_at else document.created_at
