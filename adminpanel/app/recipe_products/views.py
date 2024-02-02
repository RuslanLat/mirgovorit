from flask_admin.contrib.sqla import ModelView


class RecipeProductView(ModelView):
    column_display_pk = True
    column_labels = {
        "id": "ID",
        "recipe": "Рецепт",
        "product": "Продукт",
        "recipe.title": "Рецепт",
        "product.title": "Продукт",
        "quantity": "Количество",
    }
    column_list = ["id", "recipe.title", "product.title", "quantity"]
    column_filters = ["recipe.title", "product.title", "quantity"]
    column_sortable_list = ["id", "recipe.title", "product.title", "quantity"]

    create_modal = True
    edit_modal = True
