# -*- coding: utf8 -*-
from __future__ import unicode_literals
from mocal.mongo_models import *


@register_pre_save()
class MocalFile(MocalBase):
    filename = StringField(required=True)
    ext = StringField(required=True)
    md5 = StringField(required=True)
    mimetype = StringField(required=True)
    file_obj = FileField(required=True)

    meta = {
        'collection': 'mocal_file',
        'strict': False
    }
