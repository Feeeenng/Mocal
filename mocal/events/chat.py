# -*- coding: utf-8 -*-
from mocal.utils.datetime_display import now_lambda, format_datetime
from flask_socketio import emit, join_room, leave_room
from mocal import socket_io
from mocal.models.user import User


@socket_io.on('join', namespace='/chat')
def join(data):
    uid = data['uid']
    user = User.from_db(id=uid)
    nickname = user.nickname
    group_id = data['group_id']
    now = now_lambda()
    now_str = format_datetime(now)
    join_room(group_id)
    # todo: 加群数据逻辑
    emit('status', {'msg': nickname + ' 加入群聊', 'datetime': now_str}, room=group_id)


@socket_io.on('text', namespace='/chat')
def text(data):
    uid = data['uid']
    user = User.from_db(id=uid)
    nickname = user.nickname
    group_id = data['group_id']
    msg = data['msg']
    now = now_lambda()
    now_str = format_datetime(now)
    # todo: 数据存储逻辑
    emit('message', {'nickname': nickname, 'msg': msg, 'datetime': now_str, 'uid': uid, 'photo':user.photo(256)}, room=group_id)


@socket_io.on('leave', namespace='/chat')
def leave(data):
    uid = data['uid']
    user = User.from_db(id=uid)
    nickname = user.nickname
    group_id = data['group_id']
    now = now_lambda()
    now_str = format_datetime(now)
    leave_room(group_id)
    # todo: 退群数据逻辑
    emit('status', {'msg': nickname + ' 退出群聊', 'datetime': now_str}, room=group_id)