# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash, jsonify
from flask_login import login_required, current_user
from mocal.views import res
from mocal.models.message import Message
from mocal.models.topic import Topic, UserTopics
from mocal.models.user import User

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
        if not topic.is_marked(uid=current_user.id):
            ut = UserTopics(uid=current_user.id, tid=topic_id)
            ut.save(add=True)
        else:
            ut = UserTopics.from_db(uid=current_user.id, tid=topic_id)
            ut.deleted_at = None
            ut.save()

        messages = Message.fetch(group=topic_id, page=1, count=10)
        creator = User.from_db(id=topic.creator_id)
        return render_template('topic/talk.html', messages=messages, topic=topic, creator_name=creator.nickname,
                               photo=creator.photo(256))
    flash('无法找到该话题')
    return redirect(url_for('main.index'))


@instance.route('/topics', methods=['GET'])
@login_required
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