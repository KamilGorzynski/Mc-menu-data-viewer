import pandas as pd
from flask import Blueprint, Response, request, jsonify
from app.blueprints.menu_items.models import MenuItem, ItemCategory, db
from .helpers import create_menu_items
from werkzeug.exceptions import BadRequest
from app.blueprints.menu_items.serializers import MenuItemSchema, ItemCategorySchema, LightMenuItemSchema

bp = Blueprint("menu_items", __name__)


@bp.route("/import", methods=["POST"])
def import_menu_items():
    if not (file := request.files.get("file")):
        raise BadRequest(description="File not provided")
    create_menu_items(pd.read_csv(file))
    # TODO handle when records are not created
    return Response("Menu Items")


@bp.route("/menu_items", methods=["GET"])
def get_all_menu_items():
    return jsonify(
        {"menu_items": MenuItemSchema(many=True).dump(MenuItem.query.all())}
    )


@bp.route("/light_menu_items", methods=["GET"])
def get_light_menu_items():
    queryset = db.paginate(db.select(MenuItem))
    return jsonify(
        {"light_menu_items": LightMenuItemSchema(many=True).dump(queryset)}
    )


@bp.route("/categories", methods=["GET"])
def get_all_categories():
    queryset = ItemCategory.query.order_by(ItemCategory.name).all()
    return jsonify(
        {"item_categories": ItemCategorySchema(many=True).dump(queryset)}
    )
