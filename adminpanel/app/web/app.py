from flask import Flask
from flask_babel import Babel

from app.web.config import setup_config
from app.web.admin import setup_admin
from app.store.database import db


babel = Babel()


def create_app(config_path):
    app = Flask(__name__)
    setup_config(app, config_path)
    db.init_app(app)
    babel.init_app(app)
    setup_admin(app)

    return app
