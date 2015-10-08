# -*- coding: utf-8 -*-


class Error:
    SUCCESS = 0

    # login
    LOGIN_ACCOUNT_NOT_EXISTED = 100
    LOGIN_PASSWORD_ERROR = 101
    LOGIN_CAPTCHA_ERROR = 102

    UNKNOWN = 999

    # error map
    error_map = {
        SUCCESS: '操作成功',
        LOGIN_ACCOUNT_NOT_EXISTED: '用户名不存在',
        LOGIN_PASSWORD_ERROR: '密码错误',
        LOGIN_CAPTCHA_ERROR: '验证码错误',
        UNKNOWN: '未知错误'
    }

    # checked_success
    @classmethod
    def is_succeed(cls, code):
        return True if code == cls.SUCCESS else False