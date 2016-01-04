# -*- coding: utf8 -*-
import os
import sys
import glob

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from flask_login import LoginManager

from config import config
from utils.logger import logger
from utils.csrf_token import generate_csrf_token
from utils.random_cursor import get_cursor_path

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
bootstrap = Bootstrap()
mail = Mail()
db = DataBase()
cache = Cache()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '用户需要登录后方可访问该页面'


def create_app(config_name):
    app = Flask(__name__)
    # 读配置文件
    app.config.from_object(config[config_name])

    # flask扩展
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    login_manager.init_app(app)

    # 防跨站式攻击
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.jinja_env.globals['get_cursor_path'] = get_cursor_path

    # 蓝图注册
    config_blueprint(app)
    return app