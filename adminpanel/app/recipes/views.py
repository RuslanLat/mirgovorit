from flask_admin.contrib.sqla import ModelView
from flask import flash
from wtforms.validators import ValidationError
from .models import RecipeModel


class RecipeView(ModelView):
    column_display_pk = True
    column_labels = {
        "recipe_id": "ID рецепта",
        "title": "Рецепт",
    }

    column_filters = ["title"]

    create_modal = True
    edit_modal = True