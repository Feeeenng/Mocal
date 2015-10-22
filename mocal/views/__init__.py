# -*- coding: utf8 -*-

import json

from flask import make_response

from mocal.error import Error


def privileges_required():
    pass


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