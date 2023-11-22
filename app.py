from flask import Flask
from blueprints.healthcheck.views import bp as healthcheck


def create_app():
    app = Flask(__name__)

    # blueprints
    app.register_blueprint(healthcheck, url_prefix='/healthcheck')

    return app




