from app.blueprints.menu_items.tests.factories import ItemCategoryFactory


def test_example_model_creation(app, client):
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

