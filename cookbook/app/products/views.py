from typing import List, Optional
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_exceptions import HTTPConflict
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.products.models import Product
from app.products.schemes import (
    ProductSchema,
    ProductRequestSchema,
    ProductResponseSchema,
    ProductDeleteRequestSchema,
    ProductUpdateRequestSchema,
    ProductCookUpdateRequestSchema,
    ProductListResponseSchema,
)
from app.web.app import View
from app.web.utils import json_response


class ProductAddView(View):
    @request_schema(ProductSchema)
    @response_schema(ProductResponseSchema)
    @docs(
        tags=["products"],
        summary="Add product add view",
        description="Add product to database",
    )
    async def post(self):
        title: str = self.data["title"]

        try:
            product = await self.store.products.create_product(
                title=title,
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=ProductResponseSchema().dump(product))


class ProductUpdateView(View):
    @request_schema(ProductUpdateRequestSchema)
    @response_schema(ProductResponseSchema, 200)
    @docs(
        tags=["products"],
        summary="Add product update view",
        description="Update product in database",
    )
    async def patch(self) -> Response:
        product_id: int = self.data["product_id"]
        title: str = self.data.get("title")
        quantity: int = self.data.get("quantity")

        try:
            product: Product = await self.store.products.update_product(
                product_id=product_id,
                title=title,
                quantity=quantity,
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=ProductResponseSchema().dump(product))


class ProductCookUpdateView(View):
    @request_schema(ProductCookUpdateRequestSchema)
    @response_schema(ProductListResponseSchema, 200)
    @docs(
        tags=["products"],
        summary="Add product cook update view",
        description="Update product cook in database",
    )
    async def put(self) -> Response:
        """Функция увеличивает на единицу количество приготовленных блюд
        для каждого продукта, входящего в указанный рецепт.
        """
        recipe_id: int = self.data["recipe_id"]

        try:
            products: Optional[List[Product]] = await self.store.products.update_cook_recipe(
                recipe_id=recipe_id,
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(ProductListResponseSchema().dump({"products": products}))
    

class ProductDeleteView(View):
    @request_schema(ProductDeleteRequestSchema)
    @response_schema(ProductResponseSchema, 200)
    @docs(
        tags=["products"],
        summary="Add product delete view",
        description="Delete product from database",
    )
    async def delete(self) -> Response:
        title: str = self.data["title"]

        product: Product = await self.store.products.delete_product(title=title)

        return json_response(data=ProductResponseSchema().dump(product))


class ProductListView(View):
    @response_schema(ProductListResponseSchema, 200)
    @docs(
        tags=["products"],
        summary="Add products list view",
        description="Get list products from database",
    )
    async def get(self):
        products: Optional[List[Product]] = await self.store.products.list_products()
        return json_response(ProductListResponseSchema().dump({"products": products}))
