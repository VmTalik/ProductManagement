from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, PositiveInt, conint
from .product import ProductReadResponse
from models import Product

class ProductCategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=80, description="Название")
    description: Optional[str] = Field(default=None, max_length=800, description="Описание")


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryCreateResponse(ProductCategoryBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: PositiveInt


class ProductCategoryReadResponse(ProductCategoryBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: PositiveInt
    product_list: List[Product]


class ProductCategoryUpdate(ProductCategoryBase):
    pass


class ProductCategoryUpdateResponse(ProductCategoryCreateResponse):
    pass


class ProductCategoryDelete(ProductCategoryBase):
    id: PositiveInt
