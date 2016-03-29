# -*- coding: utf-8 -*-
from flask import g, request
from flask_login import current_user
from mocal import create_app, socket_io


'''
development: 开发环境
production: 生产环境
default: 默认开发环境
'''


mocal_app = create_app('development')


# 每个请求开始前的操作
@mocal_app.before_request
def before_request():
    g.current_user = current_user


# 每个请求结束后的操作
@mocal_app.teardown_request
def teardown_request(exception):
    pass


@socket_io.on_error_default
def default_error_handler(e):
    print request.event["message"]
    print request.event["args"]
    print e


if __name__ == '__main__':
    socket_io.run(mocal_app)