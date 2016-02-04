# -*- coding: utf-8 -*-
import qiniu


def upload_to_qn(access_key, secret_key, bucket_name, data, key):
    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket_name)
    ret, info = qiniu.put_data(token, key, data)
    if ret is not None:
        print('All is OK')
    else:
        print(info)  # error message in info