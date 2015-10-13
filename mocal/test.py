# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)

p = {
    1: '北京',
    2: '贵州'
}

c = {
    1: {
        11: '朝阳区',
        12: '海淀区'
    },
    2: {
        21: '贵阳',
        22: '凯里'
    }
}

@app.route('/')
def index():
    return render_template('test.html', p=p)


@app.route('/select_city', methods=['POST'])
def select():
    pid = request.values['pid']
    if pid:
        cities = c[int(pid)]
    else:
        cities = []
    return json.dumps(dict(cities=cities))


if __name__ == '__main__':
    app.run(debug=True)