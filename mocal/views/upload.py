# -*- coding: utf8 -*-

import os
from cStringIO import StringIO
from urllib import urlopen
from datetime import datetime
from random import randint

from flask import Blueprint, render_template, flash, send_file, request, current_app
from flask_login import login_required

from mocal.views import res
from mocal.models.upload import Upload
from mocal.utils.md5 import MD5
from mocal.constant import ALLOWED_FORMATS, ALLOWED_MAX_SIZE
from mocal.utils.cloud_storage import upload_to_qn, make_download_url
from mocal.error import Error

instance = Blueprint('upload', __name__)


@instance.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    f = request.files['file']
    if not is_allowed_format(f.filename):
        return res(code=Error.UPLOAD_FORMAT_LIMITATION)

    if not is_allowed_size(f):
        return res(code=Error.UPLOAD_SIZE_LIMITATION)

    # 获取文件内容MD5码
    bucket_name = current_app.config.get('QINIU_BUCKET_NAME')
    ext = os.path.splitext(f.filename)[-1].strip('.')
    md5 = MD5(f.stream.read()).md5_content
    upload = Upload.from_db(md5=md5)
    if not upload:
        # 上传七牛
        ak = current_app.config.get('QINIU_AK')
        sk = current_app.config.get('QINIU_SK')
        key = get_unique_name(ext)
        ret = upload_to_qn(ak, sk, bucket_name, f, key)

        # 上传信息入库
        hash = ret['hash']
        key = ret['key']
        mimetype = f.content_type
        properties = {
            'key': key,
            'hash': hash,
            'ext': ext,
            'mimetype': mimetype,
            'md5': md5
        }
        upload = Upload(**properties)
        upload.save(add=True)

    flash('上传成功！')
    domain = current_app.config.get('QINIU_DOMAIN')
    url = make_download_url(domain, upload.key)
    return res(data=dict(id=upload.id, url=url, key=upload.key))


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


@instance.route('/download/<key>', methods=['GET'])
def download_file(key):
    domain = current_app.config.get('QINIU_DOMAIN')
    url = make_download_url(domain, key)
    io = StringIO(urlopen(url).read())
    return send_file(io, attachment_filename=key, as_attachment=True)


def get_unique_name(ext):
    now = datetime.now()
    return '{0}{1}.{2}'.format(now.strftime('%Y%m%d%H%M%S'), randint(100, 999), ext)