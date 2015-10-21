# -*- coding: utf8 -*-
from flask import Blueprint, render_template, url_for, request, redirect, session, flash, current_app, abort
from flask.views import MethodView
from flask.ext.login import current_user, login_user, logout_user, login_required

from mocal.views import register_view, res
from mocal.controllers.user import User
from mocal.error import Error
from mocal.utils.md5 import MD5
from mocal.utils.verify_code import generate_verify_code
from mocal.utils.email import Email
from mocal.constant import SALT

instance = Blueprint('user', __name__)


@register_view('/login', instance, ['get', 'post'])
class Login(MethodView):
    def get(self):
        return render_template('login.html', msg='', account='', show_captcha=False)

    def post(self):
        req = request.values
        account = req.get('login_account')
        password = req.get('login_password')
        remember_me = True if req.get('remember_me') else None

        session['check_captcha'] = False

        if session.get('check_captcha'):
            captcha = req.get('captcha')
            if int(captcha) != session.get('verify_code'):
                return render_template('login.html', msg=Error.error_map[Error.LOGIN_CAPTCHA_ERROR], remember_me=remember_me, account=account, show_captcha=session.get('show_captcha'))

        user = User.from_db(account=account)
        if not user:
            session['login_failed_count'] = 1
            session['check_captcha'] = True
            return render_template('login.html', msg=Error.error_map[Error.LOGIN_ACCOUNT_NOT_EXISTED], remember_me=remember_me, account=account, show_captcha=True)

        if not user.verify_password(password):
            session['login_failed_count'] = 1
            session['check_captcha'] = True
            return render_template('login.html', msg=Error.error_map[Error.LOGIN_PASSWORD_ERROR], remember_me=remember_me, account=account, show_captcha=True)

        # 登录
        login_user(user, remember=remember_me)

        # 清除session
        session['verify_code'] = 0
        session['login_failed_count'] = 0
        session['check_captcha'] = False

        return redirect(request.args.get('next') or url_for('index'))


@register_view('/logout', instance, ['get'])
class Logout(MethodView):
    @login_required
    def get(self):
        logout_user()
        return redirect(url_for('index'))


@register_view('/register', instance, ['post'])
class Register(MethodView):
    def post(self):
        req = request.form
        account = req.get('register_account')
        password = MD5(req.get('register_password')).add_salt(SALT)
        password_confirm = req.get('password_confirm')
        nickname = req.get('nickname')
        email = req.get('email')

        params = {
            'account': account,
            'password': password,
            'password_confirm': password_confirm,
            'nickname': nickname,
            'email': email
        }

        user = User(params)
        uid = user.save(add=True)

        # generate confirm token
        token = user.generate_confirmation_token()

        # get confirm url
        confirm_url = url_for('user.confirm', token=token, _external=True)
        html = render_template(
            'email_activate.html',
            confirm_url=confirm_url)

        # send activate email
        email = Email(send_email='haner27@126.com', recipients=[user.email], sender='Mocal', subject='账户邮件确认', html=html)
        email.send_email()

        results = {
            'uid': uid
        }
        return res(data=results)


@register_view('/email_confirm/<token>', instance, ['get'])
class Confirm(MethodView):
    @login_required
    def get(self, token):
        if current_user.confirmed:
            return redirect(url_for('index'))

        user = User.from_id(current_user.id)
        if user.confirm(token):
            flash('恭喜你！你的账户邮箱验证成功！')
        else:
            flash('账户邮箱验证链接无效或是已经过期！')
        return redirect(url_for('index'))


@register_view('/check_account/<account>', instance, ['get'])
class CheckAccount(MethodView):
    def get(self, account):
        user = User.from_db(account=account, status=1)
        if not user:
            return res(data=False)
        return res(data=True)


@register_view('/check_nickname/<nickname>', instance, ['get'])
class CheckNickname(MethodView):
    def get(self, nickname):
        user = User.from_db(nickname=nickname, status=1)
        if not user:
            return res(data=False)
        return res(data=True)


@register_view('/check_email/<email>', instance, ['get'])
class CheckEmail(MethodView):
    def get(self, email):
        user = User.from_db(email=email, status=1)
        if not user:
            return res(data=False)
        return res(data=True)


@register_view('/check_verify_code/<code>', instance, ['get'])
class CheckVerifyCode(MethodView):
    def get(self, code):
        if code and session.get('verify_code') == int(code):
            return res(data=True)
        return res(data=False)


@register_view('/change_verify_code', instance, ['get'])
class ChangeVerifyCode(MethodView):
    def get(self):
        results, img_base64 = generate_verify_code()
        session['verify_code'] = results
        return res(data=img_base64)

