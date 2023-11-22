from flask import Blueprint, Response

bp = Blueprint('healthcheck', __name__)


@bp.route("/")
def view():
    return Response("OK")
