# -*- coding: utf8 -*-

from datetime import datetime

from flask import Blueprint, request, render_template, abort, session, redirect, url_for, flash
from flask_login import login_required, current_user

from mocal.utils.datetime_display import get_days_by_year_and_month, constellations

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
        user_info = current_user.user_info
        photo_default = user_info.photo
        desc = user_info.desc

        now = datetime.now()
        years = [y for y in xrange(now.year, now.year - 120, -1)]
        months = [m for m in xrange(1, 13)]

        year = user_info.year
        month = user_info.month
        day = user_info.day
        days = []
        if year and month:
            days = get_days_by_year_and_month(year, month)

        constellation = user_info.constellation or 0

        return render_template('user/user_info.html', photo_default=photo_default, user=current_user, months=months,
                               years=years, days=days, year=year, month=month, day=day, constellation=constellation,
                               constellations=constellations.items(), desc=desc)

    photo = request.form.get('photo')
    nickname = request.form.get('nickname')
    desc = request.form.get('desc')
    gender = request.form.get('gender')
    year = request.form.get('year', 0, int)
    month = request.form.get('month', 0, int)
    day = request.form.get('day', 0, int)
    constellation = request.form.get('constellation', 0, int)

    current_user.nickname = nickname
    current_user.gender = gender
    current_user.user_info.photo = photo
    current_user.user_info.desc = desc
    current_user.user_info.year = year
    current_user.user_info.month = month
    current_user.user_info.day = day

    if year and month and day:
        current_user.user_info.birthday = datetime(year=year, month=month, day=day)
    else:
        current_user.user_info.birthday = None

    current_user.user_info.constellation = constellation
    current_user.save()

    flash('个人信息修改完毕！')
    return redirect(url_for('user.user_info'))



