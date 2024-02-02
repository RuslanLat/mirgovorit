import typing

from app.recipe_products.views import (
    RecipeProductAddView,
    RecipeProductUpdateView,
    RecipeProductDeleteView,
    RecipeProductListView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    app.router.add_view("/recipe.product.add", RecipeProductAddView)
    app.router.add_view("/recipe.product.update", RecipeProductUpdateView)
    app.router.add_view("/recipe.product.delete", RecipeProductDeleteView)
    app.router.add_view("/recipe.product.list", RecipeProductListView)
