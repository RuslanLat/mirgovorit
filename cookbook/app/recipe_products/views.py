from typing import List
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc

from app.recipe_products.schemes import (
    RecipeProductRequestSchema,
    RecipeProductResponseSchema,
    RecipeProductDeleteRequestSchema,
    RecipeProductUpdateRequestSchema,
    RecipeProductListResponseSchema,
)
from app.web.app import View
from app.web.utils import json_response
from app.recipe_products.models import RecipeProduct


class RecipeProductAddView(View):
    @request_schema(RecipeProductRequestSchema)
    @response_schema(RecipeProductResponseSchema, 200)
    @docs(
        tags=["recipe_products"],
        summary="Add recipe product add view",
        description="Add recipe product to database",
    )
    async def post(self) -> Response:
        """Функция добавляет к указанному рецепту указанный продукт с указанным весом.
        Если в рецепте уже есть такой продукт,
        то функция поменяет его вес в этом рецепте на указанный.
        """
        recipe_id: int = self.data["recipe_id"]
        product_id: int = self.data["product_id"]
        quantity: int = self.data["quantity"]

        recipe_product: RecipeProduct = await self.store.recipe_products.get_recipe_id_product_id(recipe_id=recipe_id, product_id=product_id)

        if not recipe_product:
            recipe_product: RecipeProduct = (
                await self.store.recipe_products.create_recipe_product(
                    recipe_id=recipe_id, product_id=product_id, quantity=quantity
                )
            )
            product = await self.store.products.update_product(product_id=product_id, quantity=1)
        else:
            recipe_product: RecipeProduct = (
                await self.store.recipe_products.update_recipe_product_by_id(
                    id=recipe_product.id, quantity=quantity
                )
            )

        return json_response(data=RecipeProductResponseSchema().dump(recipe_product))


class RecipeProductUpdateView(View):
    @request_schema(RecipeProductUpdateRequestSchema)
    @response_schema(RecipeProductResponseSchema, 200)
    @docs(
        tags=["recipe_products"],
        summary="Add recipe product update view",
        description="Update recipe product in database",
    )
    async def put(self) -> Response:
        recipe_id: int = self.data["recipe_id"]
        product_id: int = self.data["product_id"]
        quantity: int = self.data["quantity"]

        try:
            recipe_product: RecipeProduct = (
                await self.store.recipe_products.update_recipe_product(
                    recipe_id=recipe_id,
                    product_id=product_id,
                    quantity=quantity,
                )
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RecipeProductResponseSchema().dump(recipe_product))


class RecipeProductDeleteView(View):
    @request_schema(RecipeProductDeleteRequestSchema)
    @response_schema(RecipeProductResponseSchema, 200)
    @docs(
        tags=["recipe_products"],
        summary="Add recipe product delete view",
        description="Delete recipe product from database",
    )
    async def delete(self) -> Response:
        id: int = self.data["id"]

        recipe_product: RecipeProduct = await self.store.recipe_products.delete_recipe_product(
            id=id
        )

        product = await self.store.products.update_product(product_id=recipe_product.product_id, quantity=-1)

        return json_response(data=RecipeProductResponseSchema().dump(recipe_product))


class RecipeProductListView(View):
    @response_schema(RecipeProductListResponseSchema, 200)
    @docs(
        tags=["recipe_products"],
        summary="Add recipe products list view",
        description="Get list recipe products from database",
    )
    async def get(self) -> Response:
        recipe_products: List[
            RecipeProduct
        ] = await self.store.recipe_products.list_recipe_products()
        return json_response(
            RecipeProductListResponseSchema().dump({"recipe_products": recipe_products})
        )
