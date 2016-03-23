# -*- coding: utf-8 -*-
from flask import session, url_for
from uuid import uuid4
from mocal.utils.datetime_display import weekday


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']


def some_random_string():
    return unicode(uuid4())


def get_today_bg():
    return url_for('static', filename='image/background/bg{0}.jpg'.format(weekday()), _external=True)