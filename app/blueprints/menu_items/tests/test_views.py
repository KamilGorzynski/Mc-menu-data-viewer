from app.blueprints.menu_items.tests.factories import ItemCategoryFactory, MenuItemFactory


def test_get_categories(app, client):
    with app.app_context():
        category_1 = ItemCategoryFactory()
        category_2 = ItemCategoryFactory()
        response = client.get('/menu_items/categories')
        assert response.status_code == 200
        assert response.json == {
            "item_categories": [
                {
                    "id": str(category_1.id),
                    "name": category_1.name,
                },
                {
                    "id": str(category_2.id),
                    "name": category_2.name,
                },

            ]
        }


def test_get_menu_items(app, client):
    with app.app_context():
        category = ItemCategoryFactory()
        menu_item = MenuItemFactory(category=category)
        response = client.get('/menu_items/menu_items')
        assert response.status_code == 200
        assert response.json == {
            'menu_items': [
                {
                    'calcium_daily_value': 100.0,
                    'calories': 100.0,
                    'calories_from_fat': 100.0,
                    'carbohydrates': 100.0,
                    'carbohydrates_daily_value': 100.0,
                    'category': {'id': str(category.id), 'name': category.name},
                    'cholesterol': 100.0,
                    'cholesterol_daily_value': 100.0,
                    'dietary_fiber': 100.0,
                    'dietary_fiber_daily_value': 100.0,
                    'id': str(menu_item.id),
                    'iron_daily_value': 100.0,
                    'name': 'menu-item-name-0',
                    'protein': 100.0,
                    'saturated_fat': 100.0,
                    'saturated_fat_daily_value': 100.0,
                    'serving_size': '3.9 oz (111 g)',
                    'sodium': 100.0,
                    'sodium_daily_value': 100.0,
                    'sugars': 100.0,
                    'total_fat': 100.0,
                    'total_fat_daily_value': 100.0,
                    'trans_fat': 100.0,
                    'vitamin_a_daily_value': 100.0,
                    'vitamin_c_daily_value': 100.0
                }
            ]
        }
