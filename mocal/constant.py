# -*- coding: utf-8 -*-

# 权限
BASE = 0  # 基本权限
CAN_CREATE = 1  # 添加权限
CAN_DELETE = 2  # 删除权限
CAN_SELECT = 3  # 查看权限
CAN_UPDATE = 4  # 修改权限

PRIVILEGE_TEXT = {
    CAN_CREATE: '添加权限',
    CAN_DELETE: '删除权限',
    CAN_SELECT: '查看权限',
    CAN_UPDATE: '修改权限'
}


# 角色
USER = 111
VIP_USER = 333
ADMIN = 555

ROLE_TEXT = {
    USER: '普通用户',
    VIP_USER: '会员用户',
    ADMIN: '管理员'
}


# 加密salt
SALT = '*^)h#a&n@#$;.'
