# -*- coding: utf-8 -*-
import qiniu


def upload_to_qn(access_key, secret_key, bucket_name, f, key):
    if not key:
        key = f.filename

    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key)
    mime_type = f.content_type
    params = None
    f.stream.seek(0, 2)
    content_length = f.tell()
    f.stream.seek(0)
    ret, info = qiniu.put_stream(token, key, f.stream, content_length, mime_type=mime_type, params=params)
    return ret


def make_download_url(domain, key):
    return 'http://{0}/{1}'.format(domain, key)