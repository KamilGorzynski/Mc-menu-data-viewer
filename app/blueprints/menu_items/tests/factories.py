import factory
from app.blueprints.menu_items.models import ItemCategory
from app.wsgi import db


class ItemCategoryFactory(factory.Factory):
    class Meta:
        model = ItemCategory

    name = factory.Sequence(lambda n: f"item-category-name-{n}")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        instance = model_class(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

