from marshmallow import Schema, fields


class RecipeProductSchema(Schema):
    recipe_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)


class RecipeProductRequestSchema(RecipeProductSchema):
    pass


class RecipeProductDeleteRequestSchema(Schema):
    id = fields.Int(required=True)


class RecipeProductResponseSchema(Schema):
    id = fields.Int(required=True)
    recipe_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)


class RecipeProductUpdateRequestSchema(RecipeProductSchema):
    recipe_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)


class RecipeProductListResponseSchema(Schema):
    recipe_products = fields.Nested(RecipeProductResponseSchema, many=True)
