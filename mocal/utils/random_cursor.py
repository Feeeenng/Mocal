# -*- coding: utf-8 -*-
from flask import url_for
import random


def get_cursor_path():
    num = random.randint(1, 7)
    return url_for('static', filename='cursor/{0}.cur'.format(num))