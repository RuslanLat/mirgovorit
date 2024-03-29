import typing

from app.store.database.database import Database

if typing.TYPE_CHECKING:
    from app.web.app import Application


class Store:
    def __init__(self, app: "Application"):
        from app.store.products.accessor import ProductAccessor
        from app.store.recipes.accessor import RecipeAccessor
        from app.store.recipe_products.accessor import RecipeProductAccessor

        self.products = ProductAccessor(app)
        self.recipes = RecipeAccessor(app)
        self.recipe_products = RecipeProductAccessor(app)


def setup_store(app: "Application"):
    app.database = Database(app)
    app.on_startup.append(app.database.connect)
    app.on_cleanup.append(app.database.disconnect)
    app.store = Store(app)
