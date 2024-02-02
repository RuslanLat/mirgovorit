from flask_admin import Admin

from app.products.models import ProductModel
from app.products.views import ProductView
from app.recipes.models import RecipeModel
from app.recipes.views import RecipeView
from app.recipe_products.models import RecipeProductModel
from app.recipe_products.views import RecipeProductView
from app.store.database import db
from app.web.views import MyMainView


def setup_admin(app):
    admin = Admin(
        app,
        name="CookBook",
        template_mode="bootstrap3",
        index_view=MyMainView(),
        url="/",
    )
    admin.add_view(ProductView(ProductModel, db.session, name="Продукты"))
    admin.add_view(RecipeView(RecipeModel, db.session, name="Рецепты"))
    admin.add_view(
        RecipeProductView(RecipeProductModel, db.session, name="Ингредиенты рецепта")
    )
    