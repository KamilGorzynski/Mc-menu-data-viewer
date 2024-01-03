import pandas as pd
from flask import Blueprint, Response, request, jsonify
from app.blueprints.menu_items.models import MenuItem
from .helpers import create_menu_items
from werkzeug.exceptions import BadRequest
from app.blueprints.menu_items.serializers import MenuItemSchema

bp = Blueprint("menu_items", __name__)


@bp.route("/import", methods=["POST"])
def import_menu_items():
    if not (file := request.files.get("file")):
        raise BadRequest(description="File not provided")
    create_menu_items(pd.read_csv(file))
    return Response("Menu Items")


@bp.route("/", methods=["GET"])
def get_all_menu_items():
    return jsonify(
        {"menu_items": MenuItemSchema(many=True).dump(MenuItem.query.all())}
    )
