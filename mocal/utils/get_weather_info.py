# -*- coding: utf-8 -*-
import urllib
import hashlib
import json
import requests
from flask import current_app

sk = current_app.config['BAIDU_LBS_SK']
ak = current_app.config['BAIDU_LBS_AK']
host = current_app.config['BAIDU_LBS_API_HOST']
output = 'json'


def get_weather_api_sn(query_str, sk):
    # 对queryStr进行转码，safe内的保留字符不转换
    encoded_str = urllib.quote(query_str, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    raw_str = encoded_str + sk

    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    return hashlib.md5(urllib.quote_plus(raw_str)).hexdigest()


def get_weather_city_info(location):
    query_str = '/telematics/v3/weather?location=' + location + '&output=' + output + '&ak=' + ak
    sn = get_weather_api_sn(query_str, sk)
    url = host + query_str + '&sn=' + sn

    res = requests.get(url)
    code = res.status_code
    content = None
    if code == 200:
        success = True
        try:
            content = json.loads(res.content)
        except Exception, ex:
            success = False
    else:
        success = False

    return success, content


# if __name__ == '__main__':
#     print get_weather_city_info('凯里')
