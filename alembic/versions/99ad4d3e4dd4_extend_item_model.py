"""extend_item_model

Revision ID: 99ad4d3e4dd4
Revises: 8dc9e856961d
Create Date: 2024-01-03 11:13:09.884978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ad4d3e4dd4'
down_revision = '8dc9e856961d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu_item', sa.Column('category_id', sa.UUID(), nullable=False))
    op.add_column('menu_item', sa.Column('calories', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('calories_from_fat', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('total_fat', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('total_fat_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('saturated_fat', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('saturated_fat_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('trans_fat', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('cholesterol', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('cholesterol_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('sodium', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('sodium_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('carbohydrates', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('carbohydrates_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('dietary_fiber', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('dietary_fiber_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('sugars', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('protein', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('vitamin_a_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('vitamin_c_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('calcium_daily_value', sa.Float(), nullable=True))
    op.add_column('menu_item', sa.Column('iron_daily_value', sa.Float(), nullable=True))
    op.create_foreign_key(None, 'menu_item', 'item_category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'menu_item', type_='foreignkey')
    op.drop_column('menu_item', 'iron_daily_value')
    op.drop_column('menu_item', 'calcium_daily_value')
    op.drop_column('menu_item', 'vitamin_c_daily_value')
    op.drop_column('menu_item', 'vitamin_a_daily_value')
    op.drop_column('menu_item', 'protein')
    op.drop_column('menu_item', 'sugars')
    op.drop_column('menu_item', 'dietary_fiber_daily_value')
    op.drop_column('menu_item', 'dietary_fiber')
    op.drop_column('menu_item', 'carbohydrates_daily_value')
    op.drop_column('menu_item', 'carbohydrates')
    op.drop_column('menu_item', 'sodium_daily_value')
    op.drop_column('menu_item', 'sodium')
    op.drop_column('menu_item', 'cholesterol_daily_value')
    op.drop_column('menu_item', 'cholesterol')
    op.drop_column('menu_item', 'trans_fat')
    op.drop_column('menu_item', 'saturated_fat_daily_value')
    op.drop_column('menu_item', 'saturated_fat')
    op.drop_column('menu_item', 'total_fat_daily_value')
    op.drop_column('menu_item', 'total_fat')
    op.drop_column('menu_item', 'calories_from_fat')
    op.drop_column('menu_item', 'calories')
    op.drop_column('menu_item', 'category_id')
    # ### end Alembic commands ###
