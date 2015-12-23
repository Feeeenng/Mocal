# -*- coding: utf8 -*-
from flask import Blueprint, render_template
from mocal.models.upload import Upload
from datetime import datetime, timedelta

instance = Blueprint('main', __name__)


@instance.route('/')
def index():
    # 轮播图
    carousel_pics = Upload.fetch(page=1, count=3, category='carousel')

    # 天气
    from mocal.utils.get_weather_info import get_weather_city_info
    success, weather_info = get_weather_city_info('北京')
    results = weather_info['results'][0]
    date = weather_info['date']
    dates = [(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=i)).strftime('%m月%d日')
             for i in [0, 1, 2, 3]]
    year = datetime.now().year
    return render_template('index.html', title='Mocal', carousel_pics=carousel_pics, index=results['index'],
                           current_city=results['currentCity'], weather_data=results['weather_data'], dates=dates,
                           year=year)
