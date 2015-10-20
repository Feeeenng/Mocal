# -*- coding: utf-8 -*-
from flask import render_template, session, g, request, abort
from flask_login import current_user, login_required
from app import m_app, manager
from controllers.upload import Upload


@m_app.route('/')
def index():
    carousel_pics = Upload.fetch(page=1, count=3, category='carousel')
    return render_template('index.html', title='Mocal', carousel_pics=carousel_pics)


# emergency handler
@m_app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@m_app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@m_app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@m_app.before_request
def before_request():
    g.current_user = current_user

    # 防跨站攻击
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


@m_app.teardown_request
def teardown_request(exception):
    pass


if __name__ == '__main__':
    # manager.run()
    m_app.run(debug=True, port=5000)
