from marshmallow import Schema, fields


class RecipeSchema(Schema):
    title = fields.Str(required=True)


class RecipeRequestSchema(RecipeSchema):
    pass


class RecipeResponseSchema(Schema):
    recipe_id = fields.Int(required=True)
    title = fields.Str(required=True)


class RecipeUpdateRequestSchema(RecipeResponseSchema):
    pass


class RecipeListResponseSchema(Schema):
    recipes = fields.Nested(RecipeResponseSchema, many=True)
