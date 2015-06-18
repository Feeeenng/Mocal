# -*- coding: utf8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask('mocal')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:haner27@127.0.0.1:3306/mocal?charset=utf8'
app.config['SECRET_KEY'] = 'you-never-guess'

bootstrap = Bootstrap(app)

class DataBase(SQLAlchemy):
    def __init__(self, app):
        SQLAlchemy.__init__(self, app)
        self.Model.metadata.bind = self.engine

db = DataBase(app)
m_app = app