from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.store.database.sqlalchemy_base import db
from app.products.models import Product


@dataclass
class Recipe:
    recipe_id: Optional[int]
    title: str


@dataclass
class RecipeProduct:
    recipe_id: Optional[int]
    title: str
    product: Optional[Product]
    quantity: int


class RecipeModel(db):
    __tablename__ = "recipes"
    recipe_id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    recipeproduct = relationship("RecipeProductModel", back_populates="recipe")
