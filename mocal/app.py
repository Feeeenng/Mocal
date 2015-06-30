# -*- coding: utf8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


app = Flask('mocal')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'
app.config['SECRET_KEY'] = 'you-never-guess'

# bootstrap
bootstrap = Bootstrap(app)

# db
class DataBase(SQLAlchemy):
    def __init__(self, app):
        SQLAlchemy.__init__(self, app)
        self.Model.metadata.bind = self.engine

db = DataBase(app)

# email
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = app.debug
app.config['MAIL_USERNAME'] = 'haner27'
app.config['MAIL_PASSWORD'] = 'mqhaner27'
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_EMAILS'] = 25 # 有些邮件服务器会限制一次连接中的发送邮件的上限。
app.config['MAIL_SUPPRESS_SEND'] = app.testing
app.config['MAIL_ASCII_ATTACHMENTS'] = True
mail = Mail(app) # 初始化mail

m_app = app