# -*- coding: utf8 -*-
from flask import Blueprint, render_template, url_for, request, redirect, session, flash, current_app
from flask.ext.login import current_user, login_user, logout_user, login_required

from mocal.views import res, check_filed_type_and_length
from mocal.models.user import User
from mocal.error import Error
from mocal.utils.md5 import MD5
from mocal.utils.verify_code import generate_verify_code
from mocal.utils.email import Email

instance = Blueprint('auth', __name__)


@instance.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html', msg='', email='', remember_me='')

    email = request.form.get('email')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    remember_me = True if request.form.get('remember_me') else False

    # 接口检查
    if not email or not password or not captcha:
        return res(code=Error.PARAMS_REQUIRED)

    if int(captcha) != session.get('verify_code'):
        return render_template('auth/login.html', msg=Error.error_map[Error.LOGIN_CAPTCHA_ERROR], email=email, remember_me=remember_me)

    user = User.from_db(email=email)
    if not user or not user.verify_password(password):
        return render_template('auth/login.html', msg=Error.error_map[Error.LOGIN_INFO_ERROR], email=email, remember_me=remember_me)

    # 登录
    login_user(user, remember=remember_me)

    # 清除session
    del session['verify_code']
    return redirect(request.args.get('next') or url_for('main.index'))


@instance.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@instance.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')

    email = request.form.get('email')
    password = request.form.get('password')
    password_confirm = request.form.get('password_confirm')
    nickname = request.form.get('nickname')
    sex = request.form.get('sex')
    birthday = request.form.get('birthday')

    # 接口检查
    if not email or not password or not password_confirm or not nickname or not sex:
        return res(code=Error.PARAMS_REQUIRED)

    is_checked, code = check_filed_type_and_length(email, 'email', min_size=8, max_size=30)
    if not is_checked:
        return res(code=code)

    user = User.from_db(email=email)
    if not user:
        return res(code=Error.REGISTER_EMAIL_IS_EXISTED)

    user = User.from_db(nickname=nickname)
    if not user:
        return res(code=Error.REGISTER_NICKNAME_IS_EXISTED)

    if password != password_confirm:
        return res(code=Error.REGISTER_DIFFERENT_PASSWORD)

    params = {
        'email': email,
        'password': MD5(password).add_salt(current_app.config.get('SALT')),
        'password_confirm': password_confirm,
        'nickname': nickname,
        'sex': sex,
        'birthday': birthday
    }

    user = User(**params)
    uid = user.save(add=True)

    # generate confirm token
    token = user.generate_confirmation_token()

    # get confirm url
    confirm_url = url_for('auth.confirm', token=token, _external=True)
    html = render_template(
        'email/email_activate.html',
        confirm_url=confirm_url)

    # send activate email
    email = Email(send_email='haner27@126.com', recipients=[user.email], sender='Mocal', subject='账户邮件确认', html=html)
    email.send_email()

    results = {
        'uid': uid
    }
    return res(data=results)


@instance.route('/email_confirm/<token>', methods=['GET'])
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))

    user = User.from_id(current_user.id)
    if user.confirm(token):
        flash('恭喜你！你的账户邮箱验证成功！')
    else:
        flash('账户邮箱验证链接无效或是已经过期！')
    return redirect(url_for('main.index'))


@instance.route('/check_nickname/<nickname>', methods=['GET'])
def check_nickname(nickname):
    user = User.from_db(nickname=nickname, status=1)
    if not user:
        return res(data=False)
    return res(data=True)


@instance.route('/check_email/<email>', methods=['GET'])
def check_email(email):
    user = User.from_db(email=email, status=1)
    if not user:
        return res(data=False)
    return res(data=True)


@instance.route('/check_verify_code/<code>', methods=['GET'])
def check_verify_code(code):
    if code and session.get('verify_code') == int(code):
        return res(data=True)
    return res(data=False)


@instance.route('/change_verify_code', methods=['GET'])
def change_verify_code():
    results, img_base64 = generate_verify_code()
    session['verify_code'] = results
    return res(data=img_base64)


@instance.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'GET':
        return render_template('auth/change_password.html')

    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')
    confirm_new_password = request.form.get('confirm_new_password', '')
    if current_user.verify_password(old_password):
        if new_password != confirm_new_password:
            flash('重置的密码不一致！')
        else:
            current_user.password = MD5(new_password).add_salt(current_app.config.get('SALT'))
            current_user.save()
            flash('重置密码的成功！')
            return redirect(url_for('main.index'))
    else:
        flash('原密码错误！')
    return render_template('auth/change_password.html')
