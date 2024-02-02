import flask
from flask_admin import expose, AdminIndexView
from app.recipe_products.models import RecipeProductModel


class MyMainView(AdminIndexView):
    @expose("/")
    def admin_main(self):
        product_id = flask.request.args.get("product_id")

        recipes = (
            RecipeProductModel.query.where(
                (RecipeProductModel.product_id == product_id)
                & (RecipeProductModel.quantity < 10)
            )
            .join(RecipeProductModel.product)
            .join(RecipeProductModel.recipe)
            .all()
        )
        return self.render("admin/index.html", recipes=recipes)
