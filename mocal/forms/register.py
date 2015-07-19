# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(Form):
    account = TextField('账号', validators=[DataRequired(message='账号不能为空'), Length(min=6, max=20, message='账号长度在6-20位之间')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码'), Length(min=6, max=20,message='密码长度在6-20位之间')])
    confirm = PasswordField('确认密码', validators=[DataRequired(message='请输入密码'), EqualTo('password', message='密码不一致')])
    name = TextField('昵称', validators=[DataRequired(message='起一个炫酷昵称吧'), Length(max=10, message='昵称在10位之内')])
    sex = SelectField('性别', validators=[DataRequired(message='别漏了性别哦，亲')], choices={'male': '男', 'female': '女'}.items())
    email = TextField('邮箱', validators=[Email(message='邮箱格式错误')])
    submit = SubmitField('Submit')
