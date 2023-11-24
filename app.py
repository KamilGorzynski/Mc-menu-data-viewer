from flask import Flask
from blueprints.healthcheck.views import bp as healthcheck
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# provide config
app.config.from_object("config.Config")

# blueprints
app.register_blueprint(healthcheck, url_prefix="/healthcheck")

db = SQLAlchemy(app)

migrate = Migrate(app, db)
