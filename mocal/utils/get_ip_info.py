# -*- coding: utf-8 -*-

import requests
import json


def get_ip_city_by_ip(ip_address):
    if ip_address == '127.0.0.1':
        city = '北京市'  # 默认
    else:
        res = get_ip_info(ip_address).get('data')
        city = res.get('city')
    return city


def get_ip_info(ip_address):
    data = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip_address)
    res = json.loads(data.content)
    print res
    return res
