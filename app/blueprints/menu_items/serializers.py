from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.blueprints.menu_items.models import MenuItem, ItemCategory


class ItemCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ItemCategory
        load_instance = True


class MenuItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem
        load_instance = True

    category = fields.Nested(ItemCategorySchema)


class LightMenuItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuItem
        fields = ("id", "name")
