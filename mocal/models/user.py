# -*- coding: utf8 -*-
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from db import DatabaseObject
from mocal import login_manager
from mocal.constant import VIP_USER, CAN_CREATE, CAN_DELETE, CAN_SELECT, CAN_UPDATE
from mocal.utils.md5 import MD5
from datetime import datetime
from mocal.utils.datetime_display import format_datetime


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

    def login(self):
        self.sign_in_at = datetime.now()

    def logout(self):
        self.sign_out_at = datetime.now()

    def photo(self, size=16):
        photo = '{0}?size={1}'.format(self.user_info.photo, size)
        return photo

    @property
    def gender_text_es(self):
        r = self.gender
        if self.gender == 'secret':
            r = 'spy'
        return r

    @property
    def last_login_at(self):
        return format_datetime(self.sign_in_at, '%Y-%m-%d') or '-'

    @property
    def gender_text(self):
        if self.gender == 'male':
            r = '男'
        elif self.gender == 'female':
            r = '女'
        elif self.gender == 'secret':
            r = '保密'
        else:
            r = ''
        return r

    @property
    def privileges_list(self):
        # 权限列表
        return map(lambda a: int(a), self.privileges.split(','))

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