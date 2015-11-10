# -*- coding: utf-8 -*-

from flask import current_app
from http_request import request

sina_app_key = current_app.config['SINA_APP_KEY']
SINA_SHORTEN_URL_CREATE_API = 'http://api.t.sina.com.cn/short_url/shorten.json'
SINA_SHORTEN_URL_EXPAND_API = 'http://api.t.sina.com.cn/short_url/expand.json'


def get_shorten_url(url):
    api_request_url = SINA_SHORTEN_URL_CREATE_API + '?source={0}&url_long={1}'.format(sina_app_key, url)
    code, results = request(api_request_url, 'GET')
    url_short = None
    url_long = None
    if code:
        result = results[0]
        url_short = result.get('url_short', None)
        url_long = result.get('url_long', None)

    return url_short


def get_long_url(url):
    api_request_url = SINA_SHORTEN_URL_EXPAND_API + '?source={0}&url_short={1}'.format(sina_app_key, url)
    code, results = request(api_request_url, 'GET')
    url_short = None
    url_long = None
    if code:
        result = results[0]
        url_short = result.get('url_short', None)
        url_long = result.get('url_long', None)

    return url_long


# todo： 数据库建立软链接对应表
