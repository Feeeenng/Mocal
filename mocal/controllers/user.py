# -*- coding: utf8 -*-

from base import BaseController, controller_with_dbobject
from mocal.models.user import UserDBObject


@controller_with_dbobject(UserDBObject)
class User(BaseController):
    def __init__(self, properties=None):
        super(User, self).__init__(properties)
