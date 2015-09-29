# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from flask.views import MethodView
from views import register_view, res
from controllers.chat import ChatMsg
from error import Error

instance = Blueprint('chat', __name__)


@register_view('/chat_msg', instance, ['get', 'post'])
class ChatMsg(MethodView):
    def get(self):
        return

    def post(self):
        return

