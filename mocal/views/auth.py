# -*- coding: utf8 -*-

from datetime import datetime

from flask import Blueprint, render_template, url_for, request, redirect, session, flash, current_app
from flask.ext.login import current_user, login_user, logout_user, login_required

from mocal.views import res, check_filed_type_and_length
from mocal.models.user import User
from mocal.error import Error
from mocal.utils.md5 import MD5
from mocal.utils.email import Email
from mocal.third_lib.geetest import GeetestLib

instance = Blueprint('auth', __name__)


@instance.route('/login', methods=['GET', 'POST'])
def login():
    gt_id = current_app.config.get('GEETEST_ID')
    gt_key = current_app.config.get('GEETEST_KEY')
    if request.method == 'GET':
        return render_template('auth/login.html', msg='', email='', remember_me=False, gt=gt_id)

    email = request.form.get('email')
    password = request.form.get('password')
    remember_me = True if request.form.get('remember_me') else False
    geetest_challenge = request.form.get('geetest_challenge')
    geetest_validate = request.form.get('geetest_validate')
    geetest_seccode = request.form.get('geetest_seccode')

    # 验证码
    if not geetest_challenge or not geetest_validate or not geetest_seccode:
        return render_template('auth/login.html', msg=Error.error_map[Error.LOGIN_CAPTCHA_REQUIRED], email=email,
                               remember_me=remember_me, gt=gt_id)

    status = session['gt_server_status']
    gt = GeetestLib(gt_id, gt_key)
    result = gt.validate(status, geetest_challenge, geetest_validate, geetest_seccode)
    if result == 'success':
        result = True
    else:
        result = False
    if not result:
        return render_template('auth/login.html', msg=Error.error_map[Error.LOGIN_CAPTCHA_ERROR], email=email,
                               remember_me=remember_me, gt=gt_id)

    # 接口检查
    if not email or not password:
        return res(code=Error.PARAMS_REQUIRED)

    user = User.from_db(email=email)
    if not user or not user.verify_password(password):
        return render_template('auth/login.html', msg=Error.error_map[Error.LOGIN_INFO_ERROR], email=email,
                               remember_me=remember_me, gt=gt_id)

    # 登录
    login_user(user, remember=remember_me)

    # 清除session
    del session['gt_server_status']
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
    nickname = request.form.get('nickname')
    gender = request.form.get('gender')

    # 接口检查
    if not email or not password or not nickname or not gender:
        return res(code=Error.PARAMS_REQUIRED)

    # 参数检查
    for i in [
        (email, 'email'),
        (password, 'str', 6, 20),
        (nickname, 'str', 1, 10)
    ]:
        is_checked, code = check_filed_type_and_length(*i)
        if not is_checked:
            return res(code=code)

    user = User.from_db(email=email)
    if user:
        return res(code=Error.REGISTER_EMAIL_IS_EXISTED)

    user = User.from_db(nickname=nickname)
    if user:
        return res(code=Error.REGISTER_NICKNAME_IS_EXISTED)

    params = {
        'email': email,
        'password': MD5(password).add_salt(current_app.config.get('SALT')),
        'nickname': nickname,
        'gender': gender
    }

    user = User(**params)
    user.save(add=True)

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

    flash('{0}, 您的邮箱{1}注册完成！请检查登录您的邮箱查看邮件完成激活'.format(nickname, email))
    return redirect(url_for('auth.login'))


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
    gt_id = current_app.config.get('GEETEST_ID')
    gt_key = current_app.config.get('GEETEST_KEY')
    gt = GeetestLib(gt_id, gt_key)
    status, response_str = gt.pre_process()
    session['gt_server_status'] = status
    return response_str


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
