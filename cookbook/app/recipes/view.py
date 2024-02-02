from typing import List
from aiohttp.web import HTTPConflict
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp.web_response import Response
from sqlalchemy import exc
import aiohttp_jinja2

from app.recipes.schemes import (
    RecipeRequestSchema,
    RecipeResponseSchema,
    RecipeUpdateRequestSchema,
    RecipeListResponseSchema,
)
from app.web.app import View
from app.web.utils import json_response
from app.recipes.models import Recipe


class RecipeAddView(View):
    @request_schema(RecipeRequestSchema)
    @response_schema(RecipeResponseSchema, 200)
    @docs(
        tags=["recipes"],
        summary="Add recipe add view",
        description="Add recipe to database",
    )
    async def post(self) -> Response:
        title: str = self.data["title"]

        try:
            recipe: Recipe = await self.store.recipes.create_recipe(title=title)
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RecipeResponseSchema().dump(recipe))


class RecipeUpdateView(View):
    @request_schema(RecipeUpdateRequestSchema)
    @response_schema(RecipeResponseSchema, 200)
    @docs(
        tags=["recipes"],
        summary="Add recipe update view",
        description="Update recipe in database",
    )
    async def put(self) -> Response:
        recipe_id: int = self.data["recipe_id"]
        title: str = self.data["title"]

        try:
            recipe: Recipe = await self.store.recipes.update_recipe(
                recipe_id=recipe_id, title=title
            )
        except exc.IntegrityError as e:
            if "23505" in e.orig.pgcode:
                raise HTTPConflict

        return json_response(data=RecipeResponseSchema().dump(recipe))


class RecipeDeleteView(View):
    @request_schema(RecipeRequestSchema)
    @response_schema(RecipeResponseSchema, 200)
    @docs(
        tags=["recipes"],
        summary="Add recipe delete view",
        description="Delete recipe from database",
    )
    async def delete(self) -> Response:
        title: str = self.data["title"]

        recipe: Recipe = await self.store.recipes.delete_recipe(title=title)

        return json_response(data=RecipeResponseSchema().dump(recipe))


class RecipeListView(View):
    @response_schema(RecipeListResponseSchema, 200)
    @docs(
        tags=["recipes"],
        summary="Add recipes list view",
        description="Get list recipes from database",
    )
    async def get(self) -> Response:
        recipes: List[Recipe] = await self.store.recipes.list_recipes()
        return json_response(RecipeListResponseSchema().dump({"recipes": recipes}))

class RecipeProductShowView(View):
    async def get(self):
        """Функция возвращает HTML страницу, на которой размещена таблица.
        В таблице отображены id и названия всех рецептов,
        в которых указанный продукт отсутствует,
        или присутствует в количестве меньше 10 грамм
        """

        product_id: int = self.request.match_info["product_id"]

        recipes = await self.store.recipes.list_recipes_by_product_id(product_id=int(product_id))
        
        context = {
            "title": "Рецепты продуктов",
            "recipes": recipes
        }

        response = await aiohttp_jinja2.render_template_async(
            "index.html", self.request, context=context
        )

        return response