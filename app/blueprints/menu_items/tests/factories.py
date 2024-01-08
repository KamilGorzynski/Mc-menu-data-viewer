import factory
from app.blueprints.menu_items.models import ItemCategory, MenuItem
from app.wsgi import db


class BaseFactory(factory.Factory):

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        instance = model_class(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance


class ItemCategoryFactory(BaseFactory):
    class Meta:
        model = ItemCategory

    name = factory.Sequence(lambda n: f"item-category-name-{n}")


class MenuItemFactory(BaseFactory):
    class Meta:
        model = MenuItem

    category = factory.SubFactory(ItemCategoryFactory)
    name = factory.Sequence(lambda n: f"menu-item-name-{n}")
    serving_size = "3.9 oz (111 g)"
    calories = 100
    calories_from_fat = 100
    total_fat = 100
    total_fat_daily_value = 100
    saturated_fat = 100
    saturated_fat_daily_value = 100
    trans_fat = 100
    cholesterol = 100
    cholesterol_daily_value = 100
    sodium = 100
    sodium_daily_value = 100
    carbohydrates = 100
    carbohydrates_daily_value = 100
    dietary_fiber = 100
    dietary_fiber_daily_value = 100
    sugars = 100
    protein = 100
    vitamin_a_daily_value = 100
    vitamin_c_daily_value = 100
    calcium_daily_value = 100
    iron_daily_value = 100
