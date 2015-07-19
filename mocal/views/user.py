# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for
from flask.views import MethodView
from mocal.views import register_view

instance = Blueprint('user', __name__)


@register_view('/user', instance, ['get'])
class User(MethodView):
    def get(self):
        return render_template('index.html')
