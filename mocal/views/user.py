# -*- coding: utf8 -*-

from datetime import datetime

from flask import Blueprint, request, render_template, abort, session, redirect, url_for, flash
from flask_login import login_required, current_user
from mocal.error import Error

from mocal.views import res
from mocal.utils.datetime_display import get_days_by_year_and_month, constellations
from mocal.models.user import User

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
    now = datetime.now()
    years = [y for y in xrange(now.year, now.year - 120, -1)]
    months = [m for m in xrange(1, 13)]
    user_info = current_user.user_info

    if request.method == 'GET':

        photo_default = user_info.photo
        desc = user_info.desc or ''

        year = user_info.year
        month = user_info.month
        day = user_info.day
        days = []
        if year and month:
            days = get_days_by_year_and_month(year, month)

        constellation = user_info.constellation or 0

        return render_template('user/user_info.html', photo_default=photo_default, user=current_user, months=months,
                               years=years, days=days, year=year, month=month, day=day, constellation=constellation,
                               constellations=constellations.items(), desc=desc, desc_count=len(desc))

    photo = request.form.get('photo')
    nickname = request.form.get('nickname')
    desc = request.form.get('desc')
    gender = request.form.get('gender')
    year = request.form.get('year', 0, int)
    month = request.form.get('month', 0, int)
    day = request.form.get('day', 0, int)
    constellation = request.form.get('constellation', 0, int)

    # 参数检查
    if not nickname and not photo:
        return res(code=Error.PARAMS_REQUIRED)

    current_user.nickname = nickname
    current_user.user_info.photo = photo
    current_user.user_info.desc = desc
    current_user.gender = gender
    if year in [0] + years:
        current_user.user_info.year = year

    if month in [0] + months:
        current_user.user_info.month = month

    if day in [x for x in xrange(0, 32)]:
        current_user.user_info.day = day

    if year and month and day:
        current_user.user_info.birthday = datetime(year=year, month=month, day=day)
    else:
        current_user.user_info.birthday = None

    if constellation in [x for x in xrange(0, 13)]:
        current_user.user_info.constellation = constellation

    current_user.save()

    flash('个人信息修改完毕！')
    return redirect(url_for('user.user_info'))


@instance.route('/users', methods=['GET', 'POST'])
def user_list():
    if request.method == 'GET':
        page = request.args.get('page', 1, int)
        params = {
            'page': page,
            'count': 10,
            'deleted_at': None
        }

        users = User.fetch(**params)

    return render_template('user/users.html', users=users)

