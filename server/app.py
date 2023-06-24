#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:p@55word@localhost/flask_lab'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
