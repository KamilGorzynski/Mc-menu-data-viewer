import uuid
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ItemCategory(db.Model):
    __tablename__ = "item_category"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), unique=True, nullable=False)


class MenuItem(db.Model):
    __tablename__ = "menu_item"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID, ForeignKey("item_category.id"), nullable=False)
    category = relationship("ItemCategory", backref=backref("category", uselist=False))
    name = Column(String(128), unique=True, nullable=False)
    serving_size = Column(String(128), default="-")
    calories = Column(Float, default=0)
    calories_from_fat = Column(Float, default=0)
    total_fat = Column(Float, default=0)
    total_fat_daily_value = Column(Float, default=0)
    saturated_fat = Column(Float, default=0)
    saturated_fat_daily_value = Column(Float, default=0)
    trans_fat = Column(Float, default=0)
    cholesterol = Column(Float, default=0)
    cholesterol_daily_value = Column(Float, default=0)
    sodium = Column(Float, default=0)
    sodium_daily_value = Column(Float, default=0)
    carbohydrates = Column(Float, default=0)
    carbohydrates_daily_value = Column(Float, default=0)
    dietary_fiber = Column(Float, default=0)
    dietary_fiber_daily_value = Column(Float, default=0)
    sugars = Column(Float, default=0)
    protein = Column(Float, default=0)
    vitamin_a_daily_value = Column(Float, default=0)
    vitamin_c_daily_value = Column(Float, default=0)
    calcium_daily_value = Column(Float, default=0)
    iron_daily_value = Column(Float, default=0)
