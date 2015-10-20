# -*- coding: utf-8 -*-

from flask_mail import Message
import os
import time
from mocal.app import mail
from mocal.utils.mimetype import get_mimetype


class Email(Message):
    def __init__(self, send_email, recipients, body, sender=None, subject=''):
        super(Email, self).__init__(subject=subject, sender=(sender or '匿名', send_email), recipients=recipients,
            date=time.time(), body=body)

    def add_attachment(self, file_path, send_file_name):
        filename = os.path.basename(file_path)
        mytype = get_mimetype(filename)

        with open(file_path, 'rb') as f:
            self.attach(u'{0}'.format(send_file_name or '未命名'), mytype, f.read())

    def send_email(self):
        mail.send(self)


# email = Email('haner27@126.com', ['369685930@qq.com'], 'I LOVE YOU!', '韩能放', '告白')
# email.add_attachment('code.jpg', 'good.jpg')
# email.send_email()

