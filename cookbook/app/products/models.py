from dataclasses import dataclass
from typing import Optional
from app.store.database.sqlalchemy_base import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

@dataclass
class Product:
    product_id: Optional[int]
    title: str
    quantity: int


class ProductModel(db):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    quantity = Column(Integer, default=0)
    recipeproduct = relationship("RecipeProductModel", back_populates="product")
