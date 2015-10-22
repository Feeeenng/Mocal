# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from mocal.views import res

instance = Blueprint('chat', __name__)


@instance.route('/chat_msg', methods=['GET', 'POST'])
def chat_msg():
    return res(data='good')

