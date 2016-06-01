# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery
from config import config, Config


db = SQLAlchemy()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    celery.conf.update(app.config)

    from .trader_api import apis as apis_blueprint
    app.register_blueprint(apis_blueprint)

    return app
