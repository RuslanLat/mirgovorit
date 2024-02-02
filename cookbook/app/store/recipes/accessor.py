from typing import List, Optional
from sqlalchemy import (
    select,
    update,
    delete,
    and_,
)
from sqlalchemy.orm import joinedload

from app.recipes.models import (
    Recipe,
    RecipeProduct,
    RecipeModel,
)
from app.products.models import Product
from app.recipe_products.models import RecipeProductModel
from app.base.base_accessor import BaseAccessor


class RecipeAccessor(BaseAccessor):
    async def create_recipe(self, title: int) -> Optional[Recipe]:
        new_recipe = RecipeModel(title=title)

        async with self.app.database.session.begin() as session:
            session.add(new_recipe)

        return Recipe(
            recipe_id=new_recipe.recipe_id,
            title=new_recipe.title,
        )

    async def get_by_recipe_id(self, recipe_id: int) -> Optional[Recipe]:
        query = select(RecipeModel).where(RecipeModel.recipe_id == recipe_id)

        async with self.app.database.session.begin() as session:
            recipe = await session.scalar(query)

        if not recipe:
            return None

        return Recipe(
            recipe_id=recipe.recipe_id,
            title=recipe.title,
        )

    async def get_by_title(self, title: str) -> Optional[Recipe]:
        query = select(RecipeModel).where(RecipeModel.title == title)

        async with self.app.database.session.begin() as session:
            recipe = await session.scalar(query)

        if not recipe:
            return None

        return Recipe(
            recipe_id=recipe.recipe_id,
            title=recipe.title,
        )

    async def update_recipe(self, recipe_id: int, title: str) -> Optional[Recipe]:
        query = (
            update(RecipeModel)
            .where(RecipeModel.recipe_id == recipe_id)
            .values(title=title)
            .returning(RecipeModel)
        )

        async with self.app.database.session.begin() as session:
            recipe = await session.scalar(query)

        if not recipe:
            return None

        return Recipe(
            recipe_id=recipe.recipe_id,
            title=recipe.title,
        )

    async def delete_recipe(self, title: str) -> Optional[Recipe]:
        query = (
            delete(RecipeModel).where(RecipeModel.title == title).returning(RecipeModel)
        )

        async with self.app.database.session.begin() as session:
            recipe = await session.scalar(query)

        if not recipe:
            return None

        return Recipe(
            recipe_id=recipe.recipe_id,
            title=recipe.title,
        )

    async def list_recipes(self) -> List[Optional[Recipe]]:
        query = select(RecipeModel)

        async with self.app.database.session() as session:
            recipes = await session.scalars(query)

        if not recipes:
            return []

        return [
            Recipe(
                recipe_id=recipe.recipe_id,
                title=recipe.title,
            )
            for recipe in recipes.all()
        ]

    async def list_recipes_by_product_id(
        self, product_id: int
    ) -> List[Optional[Recipe]]:
        query = (
            select(RecipeProductModel)
            .where(
                and_(
                    RecipeProductModel.product_id == product_id,
                    RecipeProductModel.recipe_id == RecipeModel.recipe_id,
                    RecipeProductModel.quantity <= 10,
                )
            )
            .options(joinedload(RecipeProductModel.recipe))
            .options(joinedload(RecipeProductModel.product))
        )

        async with self.app.database.session() as session:
            recipes = await session.scalars(query)

        if not recipes:
            return []


        return [
            RecipeProduct(
                recipe_id=recipe.recipe_id,
                title=recipe.recipe.title,
                product = Product(recipe.product.product_id, recipe.product.title, recipe.product.quantity),
                quantity=recipe.quantity,
            )
            for recipe in recipes.all()
        ]
