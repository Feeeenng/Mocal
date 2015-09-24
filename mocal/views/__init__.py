# -*- coding: utf8 -*-

import re
import json
from flask import make_response
from mocal.error import Error

p = re.compile('([A-Z])')


def register_view(path, instance, methods):
    def decorator(cls):
        class_name = cls.__name__
        class_name = camel_to_underscore_line(class_name)
        instance.add_url_rule(path, view_func=cls.as_view(class_name), methods=methods)
        return cls

    return decorator


def camel_to_underscore_line(name):
    isCapitalized = False
    if str.isupper(name[0]):
        isCapitalized = True

    name = p.sub(r'_\g<1>', name).lower()

    if (isCapitalized and name.startswith('_')):
        name = name[1:]

    return name


def privilege_required():
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