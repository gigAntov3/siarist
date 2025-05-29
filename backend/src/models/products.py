from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
from schemas.products import ProductSchema

if TYPE_CHECKING:
    from models.categories import CategoryModel
    from models.basket import BasketModel
    from models.orders import OrderProductsModel


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int]
    tag: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped[CategoryModel] = relationship(back_populates="products")

    baskets: Mapped[list[BasketModel]] = relationship("BasketModel", back_populates="product", cascade="all, delete-orphan")

    order_products: Mapped[list[OrderProductsModel]] = relationship("OrderProductsModel", back_populates="product", cascade="all, delete-orphan")

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_read_model(self) -> ProductSchema:
        return ProductSchema(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            tag=self.tag,
            photo=self.photo,
            category_id=self.category_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
