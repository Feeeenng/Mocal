# -*- coding: utf-8 -*-
from flask import session
from uuid import uuid4
from md5 import MD5


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']


def some_random_string():
    return unicode(uuid4())