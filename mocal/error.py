# -*- coding: utf-8 -*-


class Error:
    SUCCESS = 0
    PARAMS_REQUIRED = 1

    # login
    LOGIN_INFO_ERROR = 100
    LOGIN_CAPTCHA_ERROR = 101

    # register
    REGISTER_DIFFERENT_PASSWORD = 200
    REGISTER_EMAIL_IS_EXISTED = 201
    REGISTER_NICKNAME_IS_EXISTED = 202
    REGISTER_EMAIL_FORMAT_ERROR = 203
    REGISTER_FIELD_LENGTH_BEYOND = 204
    REGISTER_FIELD_LENGTH_UNQUALIFIED = 205
    REGISTER_FIELD_TYPE_ERROR = 206
    REGISTER_FIELD_LIMIT_TYPE_NOT_EXISTED = 207

    UNKNOWN = 999

    # error map
    error_map = {
        SUCCESS: '操作成功',
        PARAMS_REQUIRED: '参数缺失',
        LOGIN_INFO_ERROR: '用户名或密码错误',
        LOGIN_CAPTCHA_ERROR: '验证码错误',
        REGISTER_DIFFERENT_PASSWORD: '密码不一致',
        REGISTER_EMAIL_IS_EXISTED: '邮箱已存在',
        REGISTER_NICKNAME_IS_EXISTED: '昵称已存在',
        REGISTER_EMAIL_FORMAT_ERROR: '邮箱格式错误',
        REGISTER_FIELD_LENGTH_BEYOND: '字段长度超出限制',
        REGISTER_FIELD_LENGTH_UNQUALIFIED: '字段长度未达到最低标准',
        REGISTER_FIELD_TYPE_ERROR: '字段类型错误',
        REGISTER_FIELD_LIMIT_TYPE_NOT_EXISTED: '字段的限制类型不存在',
        UNKNOWN: '未知错误'
    }

    # checked_success
    @classmethod
    def is_succeed(cls, code):
        return True if code == cls.SUCCESS else False