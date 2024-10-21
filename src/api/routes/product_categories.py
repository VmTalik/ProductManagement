from fastapi import APIRouter, status, Depends
from schemas import (
    ProductCategoryCreate,
    ProductCategoryCreateResponse,
    ProductCategoryReadResponse,
    ProductCategoryReadWithProductListResponse,
    ProductCategoryUpdate,
    ProductCategoryFieldUpdate,
    ProductCategoryUpdateResponse
)
from crud import ProductCategoryCRUDRepository
from api.dependencies import get_repository

router = APIRouter(prefix="/product_categories", tags=["ProductCategories"])


@router.post("/", response_model=ProductCategoryCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
        product_category_create: ProductCategoryCreate,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))
):
    return await product_category_repo.create_product_category(product_create=product_category_create)


@router.get("/", response_model=list[ProductCategoryReadResponse], status_code=status.HTTP_200_OK)
async def get_product_categories_list(
        offset: int = 0,
        limit: int = 10,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))
):
    return await product_category_repo.get_product_categories_list(offset=offset, limit=limit)


@router.get("/{id}", response_model=ProductCategoryReadWithProductListResponse, status_code=status.HTTP_200_OK)
async def get_product_category_by_id(
        id: int,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))
):
    return await product_category_repo.get_product_category_by_id(product_category_id=id)


@router.put("/{id}", response_model=ProductCategoryUpdateResponse, status_code=status.HTTP_200_OK)
async def update_product_category(
        id: int,
        product_category_update: ProductCategoryUpdate,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))
):
    return await product_category_repo.update_product_category(product_category_id=id,
                                                               product_category_update=product_category_update)


@router.patch("/{id}", response_model=ProductCategoryUpdateResponse, status_code=status.HTTP_200_OK)
async def update_product_category_field(
        id: int,
        product_category_field_update: ProductCategoryFieldUpdate,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))

):
    return await (
        product_category_repo
        .update_product_category_field(
            product_category_id=id,
            product_category_field_update=product_category_field_update
        ))


@router.delete("/{id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        id: int,
        product_category_repo: ProductCategoryCRUDRepository = Depends(
            get_repository(repo_type=ProductCategoryCRUDRepository))
):
    await product_category_repo.delete_product_category(product_category_id=id)
