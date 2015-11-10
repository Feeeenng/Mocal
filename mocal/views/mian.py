# -*- coding: utf8 -*-
from flask import Blueprint, render_template
from mocal.models.upload import Upload

instance = Blueprint('main', __name__)


@instance.route('/')
def index():
    carousel_pics = Upload.fetch(page=1, count=3, category='carousel')
    from mocal.utils.create_sina_shorten_url import get_shorten_url, get_long_url
    s = get_shorten_url('http://www.baidu.com')
    print s
    print get_long_url(s)
    return render_template('index.html', title='Mocal', carousel_pics=carousel_pics)