# -*- coding: utf8 -*-
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from db import DatabaseObject
from mocal import login_manager
from mocal.constant import VIP_USER, CAN_CREATE, CAN_DELETE, CAN_SELECT, CAN_UPDATE
from mocal.utils.md5 import MD5


@login_manager.user_loader
def load_user(uid):
    return User.from_id(int(uid))


class User(UserMixin, DatabaseObject):
    __tablename__ = 'user'
    __table_args__ = {'autoload': True, 'extend_existing': True}

    def __repr__(self):
        return '<User: %r>' % self.name

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

    def verify_password(self, password):
        md5 = MD5(password)
        return self.password == md5.add_salt(current_app.config.get('SALT'))

    @property
    def privileges_list(self):
        return self.privileges.split(',')  # todo

    def generate_confirmation_token(self, expiration=86400):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False

        self.confirmed = 1
        self.save()
        return True