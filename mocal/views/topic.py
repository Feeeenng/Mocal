# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash, jsonify
from flask_login import login_required, current_user
from mocal.views import res
from mocal.models.message import Message
from mocal.models.topic import Topic, UserTopics
from mocal.models.user import User

instance = Blueprint('topic', __name__)


@instance.before_request
@login_required
def before_request():
    pass


@instance.route('/topic', methods=['GET'])
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
def topics():
    page = request.args.get('page', 1, int)
    topics = Topic.fetch(page=page, count=8)
    return render_template('topic/topics.html', topics=topics, get_user_name=get_user_name, get_user_photo=get_user_photo)


def get_user_name(uid):
    user = User.from_db(id=uid)
    return user.nickname


def get_user_photo(uid):
    user = User.from_db(id=uid)
    return user.photo


@instance.route('/topic/mark', methods=['POST'])
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
def is_marked():
    res = request.get_json(force=True)
    topic_id = res.get('topic_id')
    tp = Topic.from_db(id=topic_id)
    if tp:
        return jsonify(success=True, is_marked=tp.is_marked(current_user.id))
    return jsonify(success=False)