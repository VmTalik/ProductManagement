from .base import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Text, String, DECIMAL, ForeignKey
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .product_category import ProductCategory


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(12, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("product_categories.id"))
    category: Mapped["ProductCategory"] = relationship(back_populates="product_list")
