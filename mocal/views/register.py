# -*- coding: utf8 -*-

from flask import Blueprint, render_template, session, flash, url_for, redirect
from flask.views import MethodView
from views import register_view
from forms.register import RegisterForm

instance = Blueprint('register', __name__)


@register_view('/register', instance, ['get', 'post'])
class User(MethodView):
    def get(self):
        form = RegisterForm()
        return render_template('register.html', form=form)

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            session['name'] = form.name.data
            flash('注册成功')
            return redirect(url_for('hello_world'))
        return render_template('register.html', form=form)