# -*- coding: utf8 -*-

import os
from cStringIO import StringIO
from datetime import datetime
from random import randint

from flask import Blueprint, flash, send_file, request, url_for
from flask_login import login_required

from mocal.views import res
from mocal.mongo_models.mocal_file import MocalFile
from mocal.utils.md5 import MD5
from mocal.utils.image_operate import ImgOperate
from mocal.constant import ALLOWED_FORMATS, ALLOWED_MAX_SIZE
from mocal.error import Error

instance = Blueprint('upload', __name__)


@instance.before_request
def before_request():
    # 防跨站攻击
    pass


@instance.route('/upload', methods=['POST'])
@login_required
def upload_file():
    f = request.files.get('file')
    if not is_allowed_format(f.filename):
        return res(code=Error.UPLOAD_FORMAT_LIMITATION)

    if not is_allowed_size(f):
        return res(code=Error.UPLOAD_SIZE_LIMITATION)

    # 获取文件内容MD5码
    ext = os.path.splitext(f.filename)[-1].strip('.')
    data = f.stream.read()
    md5 = MD5(data).md5_content
    file_name = get_unique_name(ext)
    content_type = f.content_type
    mc_f = MocalFile.objects(md5=md5).first()
    if not mc_f:
        # 上传文件到mongo
        mc_f = MocalFile()
        mc_f.ext = ext
        mc_f.filename = file_name
        mc_f.mimetype = content_type
        mc_f.md5 = md5
        mc_f.file_obj.put(data, content_type=content_type)
        mc_f.save()

    url = url_for('upload.show_file', file_id=mc_f.id)
    return res(data=dict(id=mc_f.id, name=file_name, url=url))


def is_allowed_format(file_name):
    ext = os.path.splitext(file_name)[-1].strip('.')
    if ext.lower() not in ALLOWED_FORMATS:
        flash('上传失败，仅支持上传jpg和png格式文件！')
        return False
    return True


def is_allowed_size(f):
    f.stream.seek(0, 2)
    content_length = f.tell()
    f.stream.seek(0)
    if content_length > ALLOWED_MAX_SIZE:
        return False
    return True


@instance.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    mf = MocalFile.objects.with_id(file_id)
    io = StringIO(mf.file_obj.read())
    return send_file(io, attachment_filename=mf.filename, as_attachment=True)


@instance.route('/file/<file_id>', methods=['GET'])
def show_file(file_id):
    size = request.args.get('size', 0, int)
    mf = MocalFile.objects.with_id(file_id)
    if size:
        img_op = ImgOperate(mf.file_obj)
        img_op.resize(size, size)
        io = img_op.save_io()
    else:
        img_op = ImgOperate(mf.file_obj)
        img_op.water_mark(img_op.im)
        io = img_op.save_io()
    return send_file(io, mimetype=mf.mimetype)  # 指定相关mimetype


def get_unique_name(ext):
    now = datetime.now()
    return '{0}{1}.{2}'.format(now.strftime('%Y%m%d%H%M%S'), randint(100, 999), ext)
