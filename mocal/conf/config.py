# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'h!a@n#n$e%n^g&f*a(n)g_m+o.c<a?l'

    # 邮箱配置
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'haner27'
    MAIL_PASSWORD = 'mqhaner27'
    MAIL_DEFAULT_SENDER = None
    MAIL_MAX_EMAILS = 25
    MAIL_ASCII_ATTACHMENTS = True

    # 上传文件夹
    UPLOAD_FOLDER = 'static/upload'

    # 加密salt
    SALT = '*^)h#a&n@#$;.'

    # 新浪sina
    SINA_APP_KEY = 3058213685
    SINA_SECRET = 'b46f30e6ca313fef81beba2360a70616'

    # 百度LBS
    BAIDU_LBS_SK = '7OqY0apBPyHMMkRMokabgvC8IrhhpLcF'
    BAIDU_LBS_AK = 'a7CxbjMO5TP5AdQvWEQzfZiT'
    BAIDU_LBS_API_HOST = 'http://api.map.baidu.com'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
