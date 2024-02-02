import typing

from app.recipes.view import (
    RecipeAddView,
    RecipeUpdateView,
    RecipeDeleteView,
    RecipeListView,
    RecipeProductShowView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    app.router.add_view("/recipe.add", RecipeAddView)
    app.router.add_view("/recipe.update", RecipeUpdateView)
    app.router.add_view("/recipe.delete", RecipeDeleteView)
    app.router.add_view("/recipe.list", RecipeListView)
    app.router.add_view(r"/recipe.product.show/{product_id:\d+}/", RecipeProductShowView, name="recipe_product_show")
