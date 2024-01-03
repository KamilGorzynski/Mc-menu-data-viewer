from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.blueprints.menu_items.models import MenuItem


class MenuItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem
        load_instance = True

