from flask import Flask
from app.blueprints.healthcheck.views import bp as healthcheck
from app.blueprints.menu_items.views import bp as menu_items
from app.blueprints.menu_items.models import db
from flask_migrate import Migrate
from flask import json
from werkzeug.exceptions import BadRequest


app = Flask(__name__)


@app.errorhandler(BadRequest)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


# provide config
app.config.from_object("app.config.Config")

# blueprints
app.register_blueprint(healthcheck, url_prefix="/healthcheck")
app.register_blueprint(menu_items, url_prefix="/menu_items")

# db
db.init_app(app)
Migrate(app, db)
