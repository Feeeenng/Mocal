# -*- coding: utf8 -*-

from base import BaseController, controller_with_dbobject
from mocal.models.user import UserDBObject
from mocal.constant import VIP_USER, CAN_CREATE, CAN_DELETE, CAN_SELECT, CAN_UPDATE
from mocal.utils.md5 import MD5
from mocal.constant import SALT


@controller_with_dbobject(UserDBObject)
class User(BaseController):
    def __init__(self, properties=None):
        super(User, self).__init__(properties)

    def to_be_vip(self):
        self.set_property('role', VIP_USER)
        self.save()

    def could_create(self):
        return True if CAN_CREATE in self.privileges_list else False

    def could_delete(self):
        return True if CAN_DELETE in self.privileges_list else False

    def could_select(self):
        return True if CAN_SELECT in self.privileges_list else False

    def could_update(self):
        return True if CAN_UPDATE in self.privileges_list else False

    @property
    def password_encrypted(self):
        md5 = MD5(self.password)
        return md5.add_salt(SALT)

    def verify_password(self, password):
        md5 = MD5(password)
        return True if self.password_encrypted == md5.add_salt(SALT) else False

    @property
    def privileges_list(self):
        return self.privileges.split(',')