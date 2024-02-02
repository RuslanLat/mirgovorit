from dataclasses import dataclass
from typing import Optional
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db


@dataclass
class RecipeProduct:
    id: Optional[int]
    recipe_id: int
    product_id: int
    quantity: int


class RecipeProductModel(db):
    __tablename__ = "recipeproducts"
    __table_args__ = (
        UniqueConstraint("recipe_id", "product_id", name="idx_unique_recipe_product"),
    )
    id = Column(Integer, primary_key=True)
    recipe_id = Column(ForeignKey("recipes.recipe_id", ondelete="CASCADE"), nullable=False)
    product_id = Column(ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer)
    recipe = relationship("RecipeModel", back_populates="recipeproduct")
    product = relationship("ProductModel", back_populates="recipeproduct")
