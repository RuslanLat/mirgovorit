"""add models

Revision ID: cd7eacf3e879
Revises: 
Create Date: 2024-01-30 10:16:47.193149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd7eacf3e879'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('product_id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('recipes',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('recipe_id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('recipeproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.recipe_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('recipe_id', 'product_id', name='idx_unique_recipe_product')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipeproducts')
    op.drop_table('recipes')
    op.drop_table('products')
    # ### end Alembic commands ###
