from typing import List, Optional
from sqlalchemy import (
    select,
    update,
    delete,
    and_
)
from sqlalchemy.orm import joinedload
from app.products.models import (
    Product,
    ProductModel,
)
from app.recipe_products.models import RecipeProductModel
from app.base.base_accessor import BaseAccessor


class ProductAccessor(BaseAccessor):
    async def create_product(self, title: str) -> Optional[Product]:
        new_product = ProductModel(title=title)

        async with self.app.database.session.begin() as session:
            session.add(new_product)

        return Product(
            product_id=new_product.product_id,
            title=new_product.title,
            quantity=new_product.quantity,
        )

    async def update_product(
        self,
        product_id: int,
        title: str = None,
        quantity: int = None,
    ) -> Optional[Product]:
        query = update(ProductModel).where(ProductModel.product_id == product_id)

        if title:
            query = query.values(title=title)
        if quantity is not None:
            query = query.values(quantity=ProductModel.quantity + quantity)

        query = query.returning(ProductModel)

        async with self.app.database.session.begin() as session:
            product = await session.scalar(query)

        if not product:
            return None

        return Product(
            product_id=product.product_id,
            title=product.title,
            quantity=product.quantity,
        )

    async def get_product_id(self, product_id: int) -> Optional[Product]:
        query = select(ProductModel).where(ProductModel.product_id == product_id)

        async with self.app.database.session.begin() as session:
            product = await session.scalar(query)

        if not product:
            return None

        return Product(
            product_id=product.product_id,
            title=product.title,
            quantity=product.quantity,
        )

    async def get_title(self, title: str) -> Optional[Product]:
        query = select(ProductModel).where(ProductModel.title == title)

        async with self.app.database.session.begin() as session:
            product = await session.scalar(query)

        if not product:
            return None

        return Product(
            product_id=product.product_id,
            title=product.title,
            quantity=product.quantity,
        )

    async def delete_product(self, title: str) -> Optional[Product]:
        query = (
            delete(ProductModel)
            .where(ProductModel.title == title)
            .returning(ProductModel)
        )

        async with self.app.database.session.begin() as session:
            product = await session.scalar(query)

        if not product:
            return None

        return Product(
            product_id=product.product_id,
            title=product.title,
            quantity=product.quantity,
        )

    async def list_products(self) -> List[Optional[Product]]:
        query = select(ProductModel)

        async with self.app.database.session() as session:
            products = await session.scalars(query)

        if not products:
            return []

        return [
            Product(
                product_id=product.product_id,
                title=product.title,
                quantity=product.quantity,
            )
            for product in products.all()
        ]

    async def update_cook_recipe(
        self,
        recipe_id: int,
    ) -> List[Optional[Product]]:
        query = (
            update(ProductModel)
            .where(
                and_(
                    RecipeProductModel.recipe_id == recipe_id,
                    ProductModel.product_id == RecipeProductModel.product_id,
                )
            )
            .values(quantity=ProductModel.quantity + 1)
            .returning(ProductModel)
        )

        async with self.app.database.session.begin() as session:
            products = await session.scalars(query)

        if not products:
            return []

        return [
            Product(
                product_id=product.product_id,
                title=product.title,
                quantity=product.quantity,
            )
            for product in products.all()
        ]
