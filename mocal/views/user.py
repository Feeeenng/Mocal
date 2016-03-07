# -*- coding: utf8 -*-

from datetime import datetime

from flask import Blueprint, request, render_template, abort, session, current_app
from flask_login import login_required, current_user

from mocal.utils.datetime_display import get_days_by_year_and_month

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

        created_at = current_user.created_at
        now = datetime.now()
        years = [y for y in xrange(now.year, now.year - 120, -1)]
        months = [m for m in xrange(1, 13)]

        year = created_at.year
        month = created_at.month
        day = created_at.day

        days = get_days_by_year_and_month(year, month)
        return render_template('user/user_info.html', photo_default=photo_default, user=current_user, months=months,
                               years=years, days=days, year=year, month=month, day=day)