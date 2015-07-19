# -*- coding: utf8 -*-
from flask_wtf import Form
from wtforms import SubmitField, FileField


class UploadForm(Form):
    photo = FileField('设置头像')
    submit = SubmitField('Submit')
