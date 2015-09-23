# -*- coding: utf8 -*-

import os

from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask.views import MethodView
from flask_login import login_required
from views import register_view
from forms.upload import UploadForm
from controllers.upload import Upload
from utils.md5 import MD5

instance = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'static/upload'
ALLOWED_FILES = ['jpg', 'png', 'jpeg']


@register_view('/upload', instance, ['get', 'post'])
class UploadFile(MethodView):
    @login_required
    def get(self):
        form = UploadForm()
        return render_template('upload.html', form=form)

    @login_required
    def post(self):
        form = UploadForm()
        f = request.files['photo']
        if not f:
            flash('请上传文件！')
            return render_template('upload.html', form=form)

        category_dir = request.values.get('category_dir')
        if not category_dir:
            category_dir = 'normal'

        if self.__is_allowed_file(f.filename):
            fname = secure_filename(f.filename)
            file_path = os.path.join(UPLOAD_FOLDER, category_dir, fname)

            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))

            # 储存在upload文件夹
            f.save(file_path)

            # 获取文件内容MD5码
            with open(file_path) as fi:
                md5 = MD5(fi.read()).md5_content

            if not self.__check_md5(md5, category_dir):

                # 上传信息入库
                properties = {
                    'path': os.path.join(UPLOAD_FOLDER, category_dir, fname).lower(),
                    'type': os.path.splitext(f.filename)[-1].strip('.'),
                    'md5': md5,
                    'category': category_dir
                }
                self.__save_to_db(properties=properties)

            flash('上传成功！')
            return redirect(url_for('upload.upload_file'))

        return render_template('upload.html', form=form)

    def __is_allowed_file(self, file_name):
        ext = os.path.splitext(file_name)[-1].strip('.')
        if ext.lower() not in ALLOWED_FILES:
            flash('上传失败，仅支持上传jpg和png格式文件！')
            return False
        return True

    def __save_to_db(self, properties):
        upload = Upload(properties)
        upload.save(add=True)

    def __check_md5(self, md5, category):
        upload = Upload.from_db(md5=md5, category=category)
        if not upload:
            return False

        return True