# -*- coding: utf-8 -*-

import time
from threading import Thread

from flask_mail import Message

from mocal import mail
from mocal.manager import mocal as app
from mocal.utils.mimetype import get_mimetype


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


class Email(Message):
    def __init__(self, send_email, recipients, sender=None, subject='', body=None, html=None):
        super(Email, self).__init__(subject=subject, sender=(sender or '匿名', send_email), recipients=recipients,
            date=time.time(), body=body, html=html)

    def add_attachment(self, file_path, send_file_name):
        mytype = get_mimetype(file_path)

        with open(file_path, 'rb') as f:
            self.attach(u'{0}'.format(send_file_name or '未命名'), mytype, f.read())

    @async
    def send_email(self):
        with app.app_context():
            mail.send(self)


# email = Email('haner27@126.com', ['369685930@qq.com'], '韩能放', 'I LOVE YOU!', '告白')
# email.add_attachment('code.jpg', 'good.jpg')
# email.send_email()

