import pandas as pd
from flask import Blueprint, Response, request
from app.blueprints.menu_items.models import MenuItem
from .helpers import create_menu_items
from werkzeug.exceptions import BadRequest

bp = Blueprint("menu_items", __name__)


@bp.route("/import", methods=["POST"])
def view():
    if not (file := request.files.get("file")):
        raise BadRequest(description="File not provided")
    create_menu_items(pd.read_csv(file))
    return Response("Menu Items")


@bp.route("/", methods=["GET"])
def view_2():
    examples = MenuItem.query.all()
    return ', '.join([example.name for example in examples])