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

    # 加密salt
    SALT = '*^)h#a&n@#$;.'

    # 新浪sina
    SINA_APP_KEY = 3058213685
    SINA_SECRET = 'b46f30e6ca313fef81beba2360a70616'

    # 百度LBS
    BAIDU_LBS_SK = '7OqY0apBPyHMMkRMokabgvC8IrhhpLcF'
    BAIDU_LBS_AK = 'a7CxbjMO5TP5AdQvWEQzfZiT'
    BAIDU_LBS_API_HOST = 'http://api.map.baidu.com'

    # 极验
    GEETEST_ID = '37e833eb1a44d15dc6c1fd6656005136'
    GEETEST_KEY = '7a4584597e4f610f4a33eebc0c3bb90a'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'

    # mongo数据库名
    MONGO_DATABASE_NAME = 'mocal'
    MONGO_DATABASE_HOST = '127.0.0.1'
    MONGO_DATABASE_PORT = 27017
    MONGO_DATABASE_USERNAME = None
    MONGO_DATABASE_PASSWORD = None

    # 用户默认头像
    PHOTO_DEFAULT_MALE = '/file/MF20160229150302536?size=256'
    PHOTO_DEFAULT_FEMALE = '/file/MF20160229150458205?size=256'
    PHOTO_DEFAULT_SECRET = '/file/MF20160229151816258?size=256'


class ProductionConfig(Config):
    SERVER_NAME = 'mocal.cn'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'

    # mongo数据库名
    MONGO_DATABASE_NAME = 'mocal'
    MONGO_DATABASE_HOST = '127.0.0.1'
    MONGO_DATABASE_PORT = 27017
    MONGO_DATABASE_USERNAME = None
    MONGO_DATABASE_PASSWORD = None

    # 用户默认头像
    PHOTO_DEFAULT_MALE = '/file/MF20160303163649153?size=256'
    PHOTO_DEFAULT_FEMALE = '/file/MF20160303163537835?size=256'
    PHOTO_DEFAULT_SECRET = '/file/MF20160303163719570?size=256'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
