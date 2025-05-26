from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

from schemas.basket import BasketSchema

if TYPE_CHECKING:
    from models.products import ProductModel


class BasketModel(Base):
    __tablename__ = "basket"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))  # добавляем внешний ключ на product
    product: Mapped[ProductModel] = relationship("ProductModel", back_populates="baskets")  # связываем с ProductModel
    
    quantity: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


    def to_read_model(self) -> BasketSchema:
        return BasketSchema(
            id=self.id,
            user_id=self.user_id,
            product=self.product.to_read_model(),
            quantity=self.quantity,
            created_at=self.created_at,
            updated_at=self.updated_at
        )