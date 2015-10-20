# -*- coding: utf-8 -*-
from pypinyin import pinyin, TONE2


def sort_by_initials(words):  # 汉字按声母排序
    # 解析汉字为拼音（带音调），并拼接起来成为一个独立的字符串
    d = {}  # 映射关系
    for word in words:
        x = unicode(word, 'utf-8')
        pinyin_decorated = pinyin(x, style=TONE2)
        pinyin_decorated = map(lambda a: a[0], pinyin_decorated)
        d[word] = ''.join(pinyin_decorated)

    dict_items = d.items()  # 将字典转变成[(k1,v1), (k2, v2)...] 这种形式的元组数组

    # 排序
    sorted_dict_items = sorted(dict_items, key=lambda x: x[1])  # 按元组数组的value进行排序

    return map(lambda a: unicode(a[0], 'utf-8'), sorted_dict_items)  # 取出排好序的元祖数组的key



# l = '广州, 深圳, 北京, 长沙, 上海, 武汉, 成都, 南京, 重庆, 济南, 南宁, 西安, 天津, 合肥, 东莞, 厦门, ' \
#     '昆明, 岳阳, 海口, 长春, 徐州, 德阳, 南昌, 沈阳, 太原, 兰州, 太仓, 杭州, 芜湖, 佛山, 肇庆, 福州, ' \
#     '安顺, 大连, 扬州, 北海, 乌鲁木齐, 青岛, 贵阳'
#
# s = l.split(', ')
# for i in sort_by_initials(s):
#     print i
