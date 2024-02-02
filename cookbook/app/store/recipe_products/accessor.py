from typing import List, Optional
from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import joinedload
from app.recipe_products.models import RecipeProduct, RecipeProductModel
from app.base.base_accessor import BaseAccessor


class RecipeProductAccessor(BaseAccessor):
    async def create_recipe_product(
        self, recipe_id: int, product_id: int, quantity: int
    ) -> Optional[RecipeProduct]:
        new_recipe_product = RecipeProductModel(
            recipe_id=recipe_id, product_id=product_id, quantity=quantity
        )

        async with self.app.database.session.begin() as session:
            session.add(new_recipe_product)

        return RecipeProduct(
            id=new_recipe_product.id,
            recipe_id=new_recipe_product.recipe_id,
            product_id=new_recipe_product.product_id,
            quantity=new_recipe_product.quantity,
        )

    async def update_recipe_product(
        self,
        recipe_id: int,
        product_id: int,
        quantity: int,
    ) -> Optional[RecipeProduct]:
        query = (
            update(RecipeProductModel)
            .where(
                and_(
                    RecipeProductModel.recipe_id == recipe_id,
                    RecipeProductModel.product_id == product_id,
                )
            )
            .values(quantity=RecipeProductModel.quantity + quantity)
            .returning(RecipeProductModel)
        )

        async with self.app.database.session.begin() as session:
            recipe_product = await session.scalar(query)

        if not recipe_product:
            return None

        return RecipeProduct(
            id=recipe_product.id,
            recipe_id=recipe_product.recipe_id,
            product_id=recipe_product.product_id,
            quantity=recipe_product.quantity,
        )

    async def update_recipe_product_by_id(
        self,
        id: int,
        quantity: int,
    ) -> Optional[RecipeProduct]:
        query = (
            update(RecipeProductModel)
            .where(RecipeProductModel.id == id)
            .values(quantity=RecipeProductModel.quantity + quantity)
            .returning(RecipeProductModel)
        )

        async with self.app.database.session.begin() as session:
            recipe_product = await session.scalar(query)

        if not recipe_product:
            return None

        return RecipeProduct(
            id=recipe_product.id,
            recipe_id=recipe_product.recipe_id,
            product_id=recipe_product.product_id,
            quantity=recipe_product.quantity,
        )

    async def get_by_id(self, id: int) -> Optional[RecipeProduct]:
        query = select(RecipeProductModel).where(RecipeProductModel.id == id)

        async with self.app.database.session.begin() as session:
            recipe_product = await session.scalar(query)

        if not recipe_product:
            return None

        return RecipeProduct(
            id=recipe_product.id,
            recipe_id=recipe_product.recipe_id,
            product_id=recipe_product.product_id,
            quantity=recipe_product.quantity,
        )

    async def get_recipe_id_product_id(
        self, recipe_id: int, product_id: int
    ) -> Optional[RecipeProductModel]:
        query = select(RecipeProductModel).where(
            and_(
                RecipeProductModel.recipe_id == recipe_id,
                RecipeProductModel.product_id == product_id,
            )
        )

        async with self.app.database.session.begin() as session:
            recipe_product = await session.scalar(query)

        if not recipe_product:
            return None

        return RecipeProduct(
            id=recipe_product.id,
            recipe_id=recipe_product.recipe_id,
            product_id=recipe_product.product_id,
            quantity=recipe_product.quantity,
        )

    async def delete_recipe_product(self, id: int) -> Optional[RecipeProduct]:
        query = (
            delete(RecipeProductModel)
            .where(RecipeProductModel.id == id)
            .returning(RecipeProductModel)
        )

        async with self.app.database.session.begin() as session:
            recipe_product = await session.scalar(query)

        if not recipe_product:
            return None

        return RecipeProduct(
            id=recipe_product.id,
            recipe_id=recipe_product.recipe_id,
            product_id=recipe_product.product_id,
            quantity=recipe_product.quantity,
        )

    async def list_recipe_products(self) -> List[Optional[RecipeProductModel]]:
        query = select(RecipeProductModel)

        async with self.app.database.session() as session:
            recipe_products = await session.scalars(query)

        if not recipe_products:
            return []

        return [
            RecipeProduct(
                id=recipe_product.id,
                recipe_id=recipe_product.recipe_id,
                product_id=recipe_product.product_id,
                quantity=recipe_product.quantity,
            )
            for recipe_product in recipe_products.all()
        ]
