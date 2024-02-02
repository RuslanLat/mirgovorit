from marshmallow import Schema, fields


class ProductSchema(Schema):
    title = fields.Str(required=True)
    

class ProductRequestSchema(ProductSchema):
    quantity = fields.Int(required=True)


class ProductDeleteRequestSchema(ProductSchema):
    pass


class ProductResponseSchema(Schema):
    product_id = fields.Int(required=True)
    title = fields.Str(required=True)
    quantity = fields.Int(required=True)


class ProductUpdateRequestSchema(Schema):
    product_id = fields.Int(required=True)
    title = fields.Str()
    quantity = fields.Int()


class ProductCookUpdateRequestSchema(Schema):
    recipe_id = fields.Int(required=True)


class ProductListResponseSchema(Schema):
    products = fields.Nested(ProductResponseSchema, many=True)
