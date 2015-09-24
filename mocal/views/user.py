# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash
from flask.views import MethodView
from mocal.views import register_view, res
from mocal.controllers.user import User
from mocal.error import Error
from flask.ext.login import login_user, logout_user

instance = Blueprint('user', __name__)


@register_view('/login', instance, ['get', 'post'])
class Login(MethodView):
    def get(self):
        return render_template('login.html', msg='')

    def post(self):
        req = request.values
        account = req.get('login_account')
        password = req.get('login_password')
        remember_me = True if req.get('remember_me') else None

        user = User.from_db(account=account)
        if not user:
            return render_template('login.html', msg=Error.error_map[Error.LOGIN_ACCOUNT_NOT_EXISTED])

        if not user.verify_password(password):
            return render_template('login.html', msg=Error.error_map[Error.LOGIN_PASSWORD_ERROR])

        # 登录
        login_user(user, remember=remember_me)
        return redirect(request.args.get('next') or url_for('index'))


@register_view('/register', instance, ['post'])
class Register(MethodView):
    def post(self):
        req = request.form
        account = req.get('register_account')
        password = req.get('register_password')
        password_confirm = req.get('password_confirm')
        nickname = req.get('nickname')
        email = req.get('email')

        return res(data=req)


@register_view('/check_account/<account>', instance, ['get'])
class CheckAccount(MethodView):
    def get(self, account):
        user = User.from_db(account=account)
        if not user:
            return res(data=False)
        return res(data=True)


@register_view('/check_nickname/<nickname>', instance, ['get'])
class CheckNickname(MethodView):
    def get(self, nickname):
        user = User.from_db(nickname=nickname)
        if not user:
            return res(data=False)
        return res(data=True)


@register_view('/check_email/<email>', instance, ['get'])
class CheckEmail(MethodView):
    def get(self, email):
        user = User.from_db(email=email)
        if not user:
            return res(data=False)
        return res(data=True)