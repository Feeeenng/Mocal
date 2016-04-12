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

# 上传文件格式设置
ALLOWED_FORMATS = ['jpg', 'png', 'jpeg', 'gif']

# 上传文件大小上线
ALLOWED_MAX_SIZE = 10 * 1024 ** 2  # 10M

# 话题类型
UNCATEGORIZED = 0
GAME = 1
TECHNOLOGY = 2
ECONOMY = 3
SOCIETY = 4
MUSIC = 5
MOVIE = 6
MILITARY = 7
SOCIAL = 8
NEWS = 9
OTHERS = 100
TOPIC_TYPES = [
    (UNCATEGORIZED, '未分类'),
    (GAME, '游戏'),
    (TECHNOLOGY, '科技'),
    (ECONOMY, '经济'),
    (SOCIETY, '社会现象'),
    (MUSIC, '音乐'),
    (MOVIE, '电影'),
    (MILITARY, '军事'),
    (SOCIAL, '交友'),
    (NEWS, '新闻'),
    (OTHERS, '其他')
]
TOPIC_TYPES_DICT = dict(TOPIC_TYPES)