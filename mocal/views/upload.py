# -*- coding: utf8 -*-

import os

from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask.views import MethodView
from mocal.views import register_view
from mocal.forms.upload import UploadForm
from mocal.app import m_app

instance = Blueprint('upload', __name__)

UPLOAD_FOLDER = m_app.config['UPLOAD_FOLDER']
ALLOWED_FILES = ['jpg', 'png']


@register_view('/upload', instance, ['get', 'post'])
class User(MethodView):
    def get(self):
        form = UploadForm()
        return render_template('upload.html', form=form)

    def post(self):
        form = UploadForm()
        f = request.files['photo']
        if not f:
            flash('请上传文件！')
            return render_template('upload.html', form=form)

        if self.__is_allowed_file(f.filename):
            fname = secure_filename(f.filename)
            file_path = os.path.join(UPLOAD_FOLDER, fname)
            f.save(file_path)
            flash('上传成功！')
            return redirect(url_for('hello_world'))

        return render_template('upload.html', form=form)

    def __is_allowed_file(self, file_name):
        ext = os.path.splitext(file_name)[-1].strip('.')
        if ext.lower() not in ALLOWED_FILES:
            flash('上传失败，仅支持上传jpg和png格式文件！')
            return False
        return True
