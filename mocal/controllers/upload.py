# -*- coding: utf8 -*-

from base import BaseController, controller_with_dbobject
from models.upload import UploadDBObject


@controller_with_dbobject(UploadDBObject)
class Upload(BaseController):
    def __init__(self, properties=None):
        super(Upload, self).__init__(properties)
