from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from schemas.users import UserSchema
from schemas.orders import OrderProductsSchema, OrderSchema

from database import Base
from schemas.products import ProductSchema

if TYPE_CHECKING:
    from models.users import UserModel
    from models.products import ProductModel


class OrderProductsModel(Base):
    __tablename__ = "order_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product = relationship("ProductModel", back_populates="order_products")

    quantity: Mapped[int]

    order = relationship("OrderModel", back_populates="order_products")
    product = relationship("ProductModel", back_populates="order_products")


class OrderModel(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    withdrawn_bonuses: Mapped[int] = mapped_column(default=0)
    total_amount: Mapped[int]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="orders")

    order_products: Mapped[list[OrderProductsModel]] = relationship(back_populates="order")

    platform: Mapped[str]
    email: Mapped[str]
    password: Mapped[str] = mapped_column(nullable=True)
    nickname: Mapped[str]

    status: Mapped[str] = mapped_column(default="new")
    payment_method: Mapped[str] = mapped_column(nullable=False)
    payment_status: Mapped[str] = mapped_column(default="pending")

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


    def to_read_model(self) -> OrderSchema:
        return OrderSchema(
            id=self.id,
            user=UserSchema.from_orm(self.user),  # возвращаем объект пользователя
            order_products=[
                OrderProductsSchema(
                    id=products.id,
                    product_id=products.product_id,
                    product=ProductSchema.from_orm(products.product) if products.product else None,
                    quantity=products.quantity
                )
                for products in self.order_products
            ],
            withdrawn_bonuses=self.withdrawn_bonuses,
            total_amount=self.total_amount,
            platform=self.platform,
            email=self.email,
            password=self.password,
            nickname=self.nickname,
            status=self.status,
            payment_method=self.payment_method,
            payment_status=self.payment_status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )