# -*- coding: utf-8 -*-
import datetime


def datetime_op(date_time):
    now = datetime.datetime.now()
    seconds = int((now - date_time).seconds)

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    if str(date_time)[:10] == str(today):
        # 一分钟内：刚刚
        if seconds < 60:
            return '刚刚'

        # 一小时内：多少分钟前
        elif seconds < 3600:
            return '{0}分钟前'.format(seconds / 60)

        # 一天内：多少小时
        else:
            return '{0}小时前'.format(seconds / 3600)

    elif str(date_time)[:10] == str(yesterday):
        return '昨天 ' + str(date_time)[11:]

    return str(date_time)

# date_time = datetime.datetime.now()
# print datetime_op(date_time)
