# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash, jsonify
from flask_login import login_required, current_user
from mocal.constant import TOPIC_TYPES, CAN_CREATE
from mocal.models.message import Message
from mocal.models.topic import Topic, UserTopics
from mocal.models.user import User
from mocal.views import res, check_filed_type_and_length, privileges_required

instance = Blueprint('topic', __name__)


@instance.before_request
def before_request():
    pass


@instance.route('/topic', methods=['GET'])
@login_required
def topic_index():
    topic_id = request.args.get('topic_id', 0, int)
    topic = Topic.from_db(id=topic_id)
    if topic:
        if not topic.is_marked(current_user.id):
            return jsonify(success=False, errors='请先关注话题！')
        messages = Message.fetch(group=topic_id, page=1, count=10)
        creator = User.from_db(id=topic.creator_id)
        return render_template('topic/talk.html', messages=messages, topic=topic, creator_name=creator.nickname,
                               photo=creator.photo(256))
    flash('无法找到该话题')
    return redirect(url_for('main.index'))


@instance.route('/topics', methods=['GET'])
@login_required
def topics():
    name = request.args.get('name')
    page = request.args.get('page', 1, int)
    params = {
        'page': page,
        'count': 10
    }

    if name:
        params.update(name__contains=name)

    topics = Topic.fetch(**params)
    return render_template('topic/topics.html', topics=topics, get_user_name=get_user_name,
                           get_user_photo=get_user_photo, types=TOPIC_TYPES)


@instance.route('/topic/search', methods=['GET'])
def search():
    query = request.args.get('q')
    params = {}
    if query:
        params.update(name__contains=query)

    topics = Topic.fetch(**params)
    items = []
    for topic in topics:
        items.append({
            'name': topic.name,
            'type': topic.type_text,
            'desc': topic.desc,
            'html_url': 'http://www.baidu.com'
        })

    return jsonify({'items': items})

def get_user_name(uid):
    user = User.from_db(id=uid)
    return user.nickname


def get_user_photo(uid):
    user = User.from_db(id=uid)
    return user.photo


@instance.route('/topic/mark', methods=['POST'])
@login_required
def mark():
    res = request.get_json(force=True)
    topic_id = res.get('topic_id')
    ut = UserTopics.from_db(uid=current_user.id, tid=topic_id)
    if ut:
        if ut.deleted_at:
            ut.deleted_at = None  # 曾经关注过，后取消，再次关注
        else:
            ut.cancel()  # 取消关注
        ut.save()

    else:
        ut = UserTopics(uid=current_user.id, tid=topic_id)  # 首次关注
        ut.save(True)

    tp = Topic.from_id(topic_id)
    if tp:
        return jsonify(success=True, is_marked=tp.is_marked(current_user.id), members=tp.members)
    return jsonify(success=False)


@instance.route('/topic/is_marked', methods=['POST'])
@login_required
def is_marked():
    res = request.get_json(force=True)
    topic_id = res.get('topic_id')
    tp = Topic.from_db(id=topic_id)
    if tp:
        return jsonify(success=True, is_marked=tp.is_marked(current_user.id))
    return jsonify(success=False)


@instance.route('/topic/check_topic_name', methods=['GET'])
@login_required
def check_topic_name():
    topic_name = request.args.get('topic_name')
    user = Topic.from_db(name=topic_name, deleted_at=None)
    if not user:
        return res(data=False)
    return res(data=True)


@instance.route('/topic/add', methods=['POST'])
@login_required
@privileges_required(privileges=[CAN_CREATE])
def add():
    name = request.form.get('name')
    desc = request.form.get('desc')
    type = request.form.get('type', 0, int)

    # 参数检查
    for i in [
        (name, 'str', 1, 40),
        (desc, 'str', 0, 140),
    ]:
        is_checked, code = check_filed_type_and_length(*i)
        if not is_checked:
            return res(code=code)

    topic = Topic(name=name, type=type, desc=desc, creator_id=current_user.id)
    topic.save(True)
    return redirect(url_for('topic.topics'))