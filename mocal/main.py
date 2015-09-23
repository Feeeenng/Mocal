# -*- coding: utf-8 -*-
from flask import render_template, session, g
from flask_login import current_user
from app import m_app, manager
from controllers.upload import Upload


@m_app.route('/')
def index():
    carousel_pics = Upload.fetch(page=1, count=3, category='carousel')
    return render_template('index.html', title='Mocal', carousel_pics=carousel_pics)

# emergency handler
@m_app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@m_app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@m_app.before_request
def before_request():
    """每个请求前都执行"""
    g.current_user = current_user


@m_app.teardown_request
def teardown_request(exception):
    """每个请求结束时都执行"""
    pass

if __name__ == '__main__':
    m_app.run(debug=True)
