# -*- coding: utf-8 -*-
from flask import render_template, session
from app import m_app
from utils.verify_code import generate_verify_code
from utils.email import Email
from utils.qr_code import generate_qrcode
from utils.logger import Logger
from controllers.user import User


@m_app.route('/')
def hello_world():
    res, img_base64 = generate_verify_code()
    session['res'] = res

    # email = Email('haner27@126.com', ['369685930@qq.com'], 'I LOVE YOU!', '韩能放', '告白')
    # email.add_attachment('code.jpg', 'good.jpg')
    # email.send_email()

    img_base64 = generate_qrcode('http://www.baidu.com')
    # logger = Logger('han', 'pay', 'pay.log')
    # logger.info('good qr_code!')

    # db
    # user = User.from_id(10)
    # user.set_property('name', 'yang')
    # user.save()
    # print user.id
    # print user.name
    # print user.age
    return render_template('index.html', title='Mocal', name='Hi!Mocal.', img_io=img_base64)

if __name__ == '__main__':
    m_app.run(debug=True, host='127.0.0.1', port=5000)