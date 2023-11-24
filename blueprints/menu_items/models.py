import uuid
from app import db

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

# Inicjalizacja obiektu Metadata
metadata = MetaData()

# Przypisanie metadanych do obiektu Base
Base.metadata = metadata

class ItemCategory(Base):
    __tablename__ = "item_category"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(128), unique=True, nullable=False)


class MenuItem(Base):
    __tablename__ = "menu_item"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # category_id = db.Column(
    #     db.Integer, db.ForeignKey("item_category.id"), nullable=False
    # )
    name = db.Column(db.String(128), unique=True, nullable=False)
    serving_size = db.Column(db.Float, default=0)
    # calories_from_fat = db.Column(db.Float, default=0)
    # total_fat = db.Column(db.Float, default=0)
    # total_fat_daily_value = db.Column(db.Float, default=0)
    # saturated_fat = db.Column(db.Float, default=0)
    # saturated_fat_daily_value = db.Column(db.Float, default=0)
    # trans_fat = db.Column(db.Float, default=0)
    # cholesterol = db.Column(db.Float, default=0)
    # cholesterol_daily_value = db.Column(db.Float, default=0)
    # sodium = db.Column(db.Float, default=0)
    # sodium_daily_value = db.Column(db.Float, default=0)
    # carbohydrates = db.Column(db.Float, default=0)
    # carbohydrates_daily_value = db.Column(db.Float, default=0)
    # dietary_fiber = db.Column(db.Float, default=0)
    # dietary_fiber_daily_value = db.Column(db.Float, default=0)
    # sugars = db.Column(db.Float, default=0)
    # protein = db.Column(db.Float, default=0)
    # vitamin_a = db.Column(db.Float, default=0)
    # vitamin_a_daily_value = db.Column(db.Float, default=0)
    # vitamin_c_daily_value = db.Column(db.Float, default=0)
    # calcium_daily_value = db.Column(db.Float, default=0)
    # iron_daily_value = db.Column(db.Float, default=0)
