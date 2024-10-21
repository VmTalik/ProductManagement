from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product


class ProductCategory(Base):
    __tablename__ = "product_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    product_list: Mapped[list["Product"]] = relationship(back_populates="category")
