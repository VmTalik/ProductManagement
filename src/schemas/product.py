from pydantic import BaseModel, Field, ConfigDict, PositiveInt, conint, condecimal


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Название")
    description: str = Field(..., default=None, max_length=900, description="Описание")
    price: condecimal(gt=0, decimal_places=2) = Field(..., description="Цена")
    category_id: PositiveInt = Field(..., description=" Id категории")


class ProductCreate(ProductBase):
    pass


class ProductCreateResponse(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: PositiveInt


class ProductReadResponse(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: PositiveInt


class ProductUpdate(ProductBase):
    pass


class ProductUpdateResponse(ProductCreateResponse):
    pass


class ProductDelete(ProductBase):
    id: PositiveInt
