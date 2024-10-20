from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
