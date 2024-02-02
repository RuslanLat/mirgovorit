from app.store.database import db


class RecipeProductModel(db.Model):
    __tablename__ = "recipeproducts"
    __table_args__ = (
        db.UniqueConstraint(
            "recipe_id", "product_id", name="idx_unique_recipe_product"
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.ForeignKey("recipes.recipe_id", ondelete="CASCADE"), nullable=False
    )
    product_id = db.Column(
        db.ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    quantity = db.Column(db.Integer)
    recipe = db.relationship("RecipeModel")
    product = db.relationship("ProductModel")
