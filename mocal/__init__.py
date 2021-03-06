# -*- coding: utf8 -*-
import os
import sys
import glob

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from flask_login import LoginManager
from flask_socketio import SocketIO

from mocal.conf.config import config
from utils.jinjia_env_func import generate_csrf_token, get_today_bg
from mongoengine import connect


# setting sys default encode. 用到FLASK-WTF 设置默认编码
reload(sys)
sys.setdefaultencoding('utf-8')


# 设置model自动加载数据库中对应表字段
class DataBase(SQLAlchemy):
    def init_app(self, app):
        SQLAlchemy.init_app(self, app)
        self.app = app
        self.Model.metadata.bind = self.engine


# 蓝图注册
def config_blueprint(application):
    views = 'views'
    register_blueprints = []
    x = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views', '*.py'))
    for py_file in x:
        view_name = os.path.basename(py_file)[:-3]
        if view_name == '__init__':
            continue

        instance = import_instance('.'.join([views, view_name, 'instance']))
        if instance:
            register_blueprints.append(instance)
        else:
            pass

    for blue_print in register_blueprints:
        application.register_blueprint(blue_print)


def import_instance(instance_name):
    package = instance_name[:instance_name.rindex('.')]

    module = __import__(package, fromlist=['instance'])
    if hasattr(module, 'instance'):
        instance = getattr(module, 'instance')
        return instance

    return None


# 初始化扩展包
mail = Mail()
db = DataBase()
cache = Cache()
socket_io = SocketIO()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '用户需要登录后方可访问该页面'


def create_app(config_name):
    app = Flask(__name__)
    # 读配置文件
    app.config.from_object(config[config_name])

    # flask扩展
    mail.init_app(app)
    db.init_app(app)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    login_manager.init_app(app)

    # mongo数据库初始化
    res = connect(app.config.get('MONGO_DATABASE_NAME'), host=app.config.get('MONGO_DATABASE_HOST'),
                  port=app.config.get('MONGO_DATABASE_PORT'), username=app.config.get('MONGO_DATABASE_USERNAME'),
                  password=app.config.get('MONGO_DATABASE_PASSWORD'))

    # 防跨站式攻击
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.jinja_env.globals['get_today_bg'] = get_today_bg

    # 蓝图注册
    config_blueprint(app)
    from mocal.events import chat
    socket_io.init_app(app)
    return app