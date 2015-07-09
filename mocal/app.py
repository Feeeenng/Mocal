# -*- coding: utf8 -*-

import os
import glob

from utils.logger import logger

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cache import Cache
from flask_restful import Api, Resource

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


# cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# config blueprint
def config_blueprint(application):
    views = 'views'
    register_blueprints = []

    for py_file in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views', '*.py')):
        view_name = os.path.basename(py_file)[:-3]
        if view_name == '__init__':
            continue

        instance = import_instance('.'.join([views, view_name, 'instance']))
        if instance:
            register_blueprints.append(instance)
            logger.info('{0} import instance succeed'.format(view_name))
        else:
            logger.error('{0} import instance failed'.format(view_name))

    for blue_print in register_blueprints:
        application.register_blueprint(blue_print)


def import_instance(instance_name):
    package = instance_name[:instance_name.rindex('.')]

    module = __import__(package, fromlist=['instance'])
    if hasattr(module, 'instance'):
        instance = getattr(module, 'instance')
        return instance

    return None

config_blueprint(app)


# get m_app
m_app = app