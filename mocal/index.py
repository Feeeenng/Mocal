# -*- coding: utf-8 -*-
from flask import render_template, session
from app import m_app
from utils.verify_code import generate_verify_code
from utils.email import Email


@m_app.route('/')
def hello_world():
    res, img_base64 = generate_verify_code()
    session['res'] = res

    # email = Email('haner27@126.com', ['369685930@qq.com'], 'I LOVE YOU!', '韩能放', '告白')
    # email.add_attachment('code.jpg', 'good.jpg')
    # email.send_email()

    return render_template('index.html', title='Mocal', name='Hi!Mocal.', img_io=img_base64)

if __name__ == '__main__':
    m_app.run(debug=True, host='127.0.0.1', port=5000)
