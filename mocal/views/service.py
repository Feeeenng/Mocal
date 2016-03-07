# -*- coding: utf8 -*-

from flask import Blueprint, jsonify, request
from flask_login import login_required
from mocal.utils.datetime_display import get_days_by_year_and_month

instance = Blueprint('service', __name__)


@instance.before_request
@login_required
def before_request():
    # 防跨站攻击
    pass


@instance.route('/get_days', methods=['POST'])
def get_days():
    year = request.form.get('year', 0, int)
    month = request.form.get('month', 0, int)
    days = get_days_by_year_and_month(year, month)
    return jsonify(success=True, days=days)