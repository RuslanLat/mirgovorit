from aiohttp.web_app import Application


def setup_routes(app: Application):
    from app.products.routes import setup_routes as product_setup_routes
    from app.recipes.routes import setup_routes as recipe_setup_routes
    from app.recipe_products.routes import setup_routes as recipe_product_setup_routes
    from app.web import views

    product_setup_routes(app)
    recipe_setup_routes(app)
    recipe_product_setup_routes(app)
    app.router.add_get("/", views.index, name="home")
