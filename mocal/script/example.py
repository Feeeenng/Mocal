# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mocal.models.user import User


user = User.from_db(nickname='Mocal')
user.nickname = '韩能放'
user.save()
print 'Done!'
