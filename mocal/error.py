# -*- coding: utf-8 -*-


class Error:
    SUCCESS = 0
    PARAMS_REQUIRED = 1

    # login
    LOGIN_INFO_ERROR = 100
    LOGIN_CAPTCHA_ERROR = 101

    UNKNOWN = 999

    # error map
    error_map = {
        SUCCESS: '操作成功',
        PARAMS_REQUIRED: '登录接口参数缺失',
        LOGIN_INFO_ERROR: '用户名或密码错误',
        LOGIN_CAPTCHA_ERROR: '验证码错误',
        UNKNOWN: '未知错误'
    }

    # checked_success
    @classmethod
    def is_succeed(cls, code):
        return True if code == cls.SUCCESS else False