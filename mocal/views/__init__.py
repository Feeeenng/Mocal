# -*- coding: utf8 -*-

import re
import json
import datetime
from functools import wraps

from flask import make_response, jsonify
from flask_login import current_user

from mocal.error import Error


def privileges_required(privileges=list()):
    def wrapper(f):
        @wraps(f)
        def decorated_view(*args, **kwargs):
            # 检查权限
            privilege_ok = False if privileges else True

            for privilege in privileges:
                if privilege in current_user.privileges:
                    privilege_ok = True
                    break

            # 检查权限通过
            if privilege_ok:
                return f(*args, **kwargs)

            return jsonify(success=False, info='您没有这个权限', error='您没有这个权限')
        return decorated_view
    return wrapper


def roles_required():
    pass


def res(code=Error.SUCCESS, data=None, msg=None):
    result = {
        'code': code,
    }
    if Error.is_succeed(code):
        result['result'] = True
        result['detail'] = data
        response = make_response(json.dumps(result))
    else:
        result['result'] = False
        if msg:
            result['msg'] = msg
        else:
            result['msg'] = Error.error_map[code]
        response = make_response(json.dumps(result))

    return response


def check_email_format(subject):
    regex = ur"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    match = re.search(regex, subject)
    if not match:
        return False
    else:
        return True


def check_filed_type_and_length(filed, limit_type, min_size=0, max_size=1000):
    if limit_type in ['str', 'email']:
        if isinstance(filed, basestring):

            if limit_type == 'email':
                if not check_email_format(filed):
                    return False, Error.REGISTER_EMAIL_FORMAT_ERROR

            if len(filed) > max_size:
                return False, Error.REGISTER_FIELD_LENGTH_BEYOND
            else:
                if len(filed) < min_size:
                    return False, Error.REGISTER_FIELD_LENGTH_UNQUALIFIED
                else:
                    return True, Error.SUCCESS
        else:
                return False, Error.REGISTER_FIELD_TYPE_ERROR

    elif limit_type in ['int']:
        if isinstance(filed, basestring):
            if not filed.isdigit():
                return False, Error.REGISTER_FIELD_TYPE_ERROR
            else:
                if int(filed) > max_size:
                    return False, Error.REGISTER_FIELD_LENGTH_BEYOND
                else:
                    if int(filed) < min_size:
                        return False, Error.REGISTER_FIELD_LENGTH_UNQUALIFIED
                    else:
                        return True, Error.SUCCESS
        else:
            if isinstance(filed, int):
                if filed > max_size:
                    return False, Error.REGISTER_FIELD_LENGTH_BEYOND
                else:
                    if filed < min_size:
                        return False, Error.REGISTER_FIELD_LENGTH_UNQUALIFIED
                    else:
                        return True, Error.SUCCESS
            else:
                return False, Error.REGISTER_FIELD_TYPE_ERROR

    elif limit_type in ['datetime']:
        if not isinstance(filed, datetime.datetime):
            return False, Error.REGISTER_FIELD_TYPE_ERROR
        return True, Error.SUCCESS

    else:
        return False, Error.REGISTER_FIELD_LIMIT_TYPE_NOT_EXISTED
