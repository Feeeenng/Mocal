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


def get_days_by_year_and_month(year, month):
    leap_year = False
    days = 0
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_year = True

    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        if leap_year:
            days = 29
        else:
            days = 28
    else:
        pass

    return [d for d in xrange(1, days + 1)]


constellations = {
    0: u'未知',
    1: u'水瓶座',
    2: u'双鱼座',
    3: u'白羊座',
    4: u'金牛座',
    5: u'双子座',
    6: u'巨蟹座',
    7: u'狮子座',
    8: u'处女座',
    9: u'天秤座',
    10: u'天蝎座',
    11: u'射手座',
    12: u'魔羯座'
}


def get_constellation(month, day):
    dt = datetime.datetime(year=2016, month=month, day=day)
    if dt >= datetime.datetime(year=2016, month=1, day=21) and dt <= datetime.datetime(year=2016, month=2, day=19):
        return 1

    elif dt >= datetime.datetime(year=2016, month=2, day=20) and dt <= datetime.datetime(year=2016, month=3, day=20):
        return 2

    elif dt >= datetime.datetime(year=2016, month=3, day=21) and dt <= datetime.datetime(year=2016, month=4, day=20):
        return 3

    elif dt >= datetime.datetime(year=2016, month=4, day=21) and dt <= datetime.datetime(year=2016, month=5, day=21):
        return 4

    elif dt >= datetime.datetime(year=2016, month=5, day=22) and dt <= datetime.datetime(year=2016, month=6, day=21):
        return 5

    elif dt >= datetime.datetime(year=2016, month=6, day=22) and dt <= datetime.datetime(year=2016, month=7, day=22):
        return 6

    elif dt >= datetime.datetime(year=2016, month=7, day=23) and dt <= datetime.datetime(year=2016, month=8, day=23):
        return 7

    elif dt >= datetime.datetime(year=2016, month=8, day=24) and dt <= datetime.datetime(year=2016, month=9, day=23):
        return 8

    elif dt >= datetime.datetime(year=2016, month=9, day=24) and dt <= datetime.datetime(year=2016, month=10, day=23):
        return 9

    elif dt >= datetime.datetime(year=2016, month=10, day=24) and dt <= datetime.datetime(year=2016, month=11, day=22):
        return 10

    elif dt >= datetime.datetime(year=2016, month=11, day=23) and dt <= datetime.datetime(year=2016, month=12, day=21):
        return 11

    elif dt >= datetime.datetime(year=2016, month=12, day=22) and dt <= datetime.datetime(year=2016, month=1, day=20):
        return 12

    else:
        return 0
