# -*- coding: utf8 -*-

from flask import Blueprint, request, render_template, abort, session, current_app
from flask_login import login_required, current_user

instance = Blueprint('user', __name__)


@instance.before_request
@login_required
def before_request():
    # 防跨站攻击
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


@instance.route('/user_info', methods=['GET', 'POST'])
def user_info():
    if request.method == 'GET':
        gender = current_user.gender
        if gender == 'male':
            photo_default = current_app.config.get('PHOTO_DEFAULT_MALE')
        elif gender == 'female':
            photo_default = current_app.config.get('PHOTO_DEFAULT_FEMALE')
        else:
            photo_default = current_app.config.get('PHOTO_DEFAULT_SECRET')

        return render_template('user/user_info.html', photo_default=photo_default)