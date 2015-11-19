# -*- coding: utf8 -*-

import json
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