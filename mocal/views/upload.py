# -*- coding: utf8 -*-

import os

from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, flash, url_for, redirect, request, current_app
from flask_login import login_required

from mocal.forms.upload import UploadForm
from mocal.models.upload import Upload
from mocal.utils.md5 import MD5
from mocal.constant import ALLOWED_FILES

instance = Blueprint('upload', __name__)


@instance.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = UploadForm()
    if request.method == 'POST':
        f = request.files['photo']
        if not f:
            flash('请上传文件！')
            return render_template('upload.html', form=form)

        category_dir = request.values.get('category_dir')
        if not category_dir:
            category_dir = 'normal'

        if is_allowed_file(f.filename):
            fname = secure_filename(f.filename)
            file_path = os.path.join(current_app.config.get('UPLOAD_FOLDER'), category_dir, fname)

            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))

            # 储存在upload文件夹
            f.save(file_path)

            # 获取文件内容MD5码
            with open(file_path) as fi:
                md5 = MD5(fi.read()).md5_content

            if not check_md5(md5, category_dir):

                # 上传信息入库
                properties = {
                    'path': os.path.join(current_app.config.get('UPLOAD_FOLDER'), category_dir, fname).lower(),
                    'type': os.path.splitext(f.filename)[-1].strip('.'),
                    'md5': md5,
                    'category': category_dir
                }
                save_to_db(properties=properties)

            flash('上传成功！')
            return redirect(url_for('upload.upload_file'))

    return render_template('upload.html', form=form)


def is_allowed_file(file_name):
    ext = os.path.splitext(file_name)[-1].strip('.')
    if ext.lower() not in ALLOWED_FILES:
        flash('上传失败，仅支持上传jpg和png格式文件！')
        return False
    return True


def save_to_db(properties):
    upload = Upload(**properties)
    upload.save(add=True)


def check_md5(md5, category):
    upload = Upload.from_db(md5=md5, category=category)
    if not upload:
        return False

    return True