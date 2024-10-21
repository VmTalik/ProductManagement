from .base import BaseCRUDRepository
from schemas import ProductCategoryCreate, ProductCategoryUpdate
from models import ProductCategory
from sqlalchemy import select, Result
from fastapi import HTTPException
from sqlalchemy.orm import selectinload


class ProductCategoryCRUDRepository(BaseCRUDRepository):
    async def create_product_category(self, product_create: ProductCategoryCreate) -> ProductCategory:
        product_category = ProductCategory(**product_create.model_dump())
        self.async_session.add(product_category)
        await self.async_session.commit()
        await self.async_session.refresh(product_category)
        return product_category

    async def get_product_categories_list(self, offset: int = 0, limit: int = 10):
        stmt = select(ProductCategory).offset(offset).limit(limit)
        result: Result = await self.async_session.execute(stmt)
        products_categories_list = result.scalars().all()
        return products_categories_list

    async def get_product_category_by_id(self, product_category_id: int) -> ProductCategory | None:
        stmt = (
            select(ProductCategory).where(ProductCategory.id == product_category_id)
            .options(selectinload(ProductCategory.product_list))
        )
        result = await self.async_session.execute(stmt)
        product_category = result.scalar_one_or_none()
        if not product_category:
            raise HTTPException(status_code=404, detail="Категория товаров не найдена!")
        return product_category

    async def update_product_category(
            self, product_category_id,
            product_update: ProductCategoryUpdate
    ) -> ProductCategory | None:
        product_category = await self.async_session.get(ProductCategory, product_category_id)
        if not product_category:
            raise HTTPException(status_code=404, detail="Обновление невозможно, категория товаров не найдена!")
        for name, value in product_update.model_dump().items():
            setattr(product_category, name, value)
        await self.async_session.commit()
        return product_category

    async def update_product_category_description(
            self,
            product_category_id: int,
            product_category_update: ProductCategoryUpdate
    ) -> ProductCategory | None:
        product_category = await self.async_session.get(ProductCategory, product_category_id)
        if not product_category:
            raise HTTPException(status_code=404, detail="Категория товаров не найдена!")
        product_description_update = product_category_update.description
        if product_description_update is not None:
            product_category.description = product_description_update
        await self.async_session.commit()
        return product_category

    async def delete_product_category(self, product_category_id) -> None:
        product_category = await self.async_session.get(ProductCategory, product_category_id)
        if not product_category:
            raise HTTPException(status_code=404, detail="Удаление невозможно, категория товаов не найдена!")
        await self.async_session.delete(product_category)
        await self.async_session.commit()
