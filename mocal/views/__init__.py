# -*- coding: utf8 -*-

import re
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