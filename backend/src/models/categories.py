from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
from schemas.categories import CategorySchema

if TYPE_CHECKING:
    from models.products import ProductModel


class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    products: Mapped[list[ProductModel]] = relationship(back_populates="category", cascade="all, delete-orphan")

    def to_read_model(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
        )
