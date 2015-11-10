# -*- coding: utf-8 -*-
from flask import render_template, session, g, request, abort
from flask_login import current_user
from flask_script import Manager, Server

from mocal import create_app
'''
development: 开发环境
production: 生产环境
default: 默认开发环境
'''
mocal = create_app('development')


# 每个请求开始前的操作
@mocal.before_request
def before_request():
    g.current_user = current_user

    # 防跨站攻击
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


# 每个请求结束后的操作
@mocal.teardown_request
def teardown_request(exception):
    pass


manager = Manager(mocal)
manager.add_command("runserver", Server(threaded=True))

if __name__ == '__main__':
    # manager.run()
    mocal.run(port=80, debug=True)
