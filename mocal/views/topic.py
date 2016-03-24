# -*- coding: utf8 -*-

from flask import Blueprint, render_template, url_for, request, redirect, session, flash, jsonify
from flask_login import login_required
from mocal.views import res
from mocal.models.message import Message
from mocal.models.topic import Topic
from mocal.models.user import User

instance = Blueprint('topic', __name__)


@instance.before_request
def before_request():
    pass


@instance.route('/topic', methods=['GET'])
@login_required
def topic_index():
    topic_id = 1
    messages = Message.fetch(group=topic_id, page=1, count=10)
    topic = Topic.from_db(id=topic_id)
    if topic:
        creator = User.from_db(id=topic.creator_id)
        return render_template('topic/talk.html', messages=messages, topic=topic, creator_name=creator.nickname,
                               photo=creator.photo(256))
    flash('无法找到该话题')
    return redirect(url_for('main.index'))

