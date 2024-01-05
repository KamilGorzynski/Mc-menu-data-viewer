from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.blueprints.menu_items.models import MenuItem, ItemCategory


class MenuItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem
        load_instance = True


class ItemCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ItemCategory
        load_instance = True
