# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for
from flask.views import MethodView
from views import register_view

instance = Blueprint('user', __name__)


@register_view('/login', instance, ['get', 'post'])
class Login(MethodView):
    def get(self):

        return render_template('login.html')
