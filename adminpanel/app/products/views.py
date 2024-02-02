from flask_admin.contrib.sqla import ModelView

class ProductView(ModelView):
    column_display_pk = True
    column_labels = {
        "product_id": "ID продукта",
        "title": "Продукт",
        "quantity": "Количество",
    }
    column_descriptions = {
        "quantity": "Cколько раз было приготовлено блюдо с использованием этого продукта"
    }
    column_filters = ["title"]

    create_modal = True
    edit_modal = True