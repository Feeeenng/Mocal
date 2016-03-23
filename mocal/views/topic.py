# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from flask_login import login_required
from mocal.views import res

instance = Blueprint('topic', __name__)


@instance.before_request
def before_request():
    pass


@instance.route('/topic', methods=['GET'])
@login_required
def chat_msg():
    # todo: 加载话题基本信息和聊天记录
    return render_template('topic/talk.html')

