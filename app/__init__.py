from flask import Flask
from app.models import init_db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        init_db()
        from . import routes, tracking
        app.register_blueprint(routes.bp)
        app.register_blueprint(tracking.bp)

    return app
