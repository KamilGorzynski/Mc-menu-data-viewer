import uuid

from . import const
from sqlalchemy.exc import IntegrityError
from app.blueprints.menu_items.models import MenuItem, ItemCategory
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# TODO move to env
session = Session(create_engine("postgresql://postgres:postgres@db:5432/mc_menu_db"))


def create_menu_categories(menu_items_df):
    category_list = []
    category_dict = {}
    for category_name in (
        menu_items_df[const.CATEGORY_COLUMN_NAME].drop_duplicates().to_list()
    ):
        category_obj = ItemCategory(id=str(uuid.uuid4()), name=category_name)
        category_list.append(category_obj)
        category_dict[category_name] = category_obj
    try:
        session.bulk_save_objects(category_list)
        session.commit()
    except IntegrityError as err:
        print("No records created")
        session.rollback()
    return category_dict


def create_menu_items(menu_items_df):
    renamed_menu_items_df = menu_items_df.rename(columns=const.COLUMNS_NAMES_MAP)
    menu_categories_dict = create_menu_categories(menu_items_df)
    menu_items_df_list = []
    for _, menu_item in renamed_menu_items_df.iterrows():
        # TODO add mashmallow serializer
        category_id = menu_categories_dict[menu_item["category"]]
        menu_item.drop("category", inplace=True)
        menu_items_df_list.append(
            MenuItem(
                **{
                    **menu_item.to_dict(),
                    "category_id": str(category_id.id)
                    ,
                }
            )
        )
    try:
        session.bulk_save_objects(menu_items_df_list)
        session.commit()
    except IntegrityError as err:
        print("<<<<<<<<<<<<<<<", err)
        print("No records created")
        session.rollback()
