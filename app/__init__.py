from enum import unique
from operator import length_hint
import sqlite3
from unicodedata import name
from flask import Flask
from app.extentions import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.api.v1.models import models

    db.init_app(app)

    from app.api.v1 import app_v1

    app.register_blueprint(app_v1, url_prefix='/api/v1/')

    return app
