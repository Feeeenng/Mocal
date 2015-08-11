# -*- coding: utf-8 -*-
from flask import render_template, session
from app import m_app
from mocal.controllers.upload import Upload


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

if __name__ == '__main__':
    m_app.run(debug=True, host='127.0.0.1', port=5000)
