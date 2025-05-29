from typing import List
from datetime import datetime
from pydantic import BaseModel

from .users import UserSchema
from .products import ProductSchema


class OrderProductsAddSchema(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True


class OrderProductsSchema(OrderProductsAddSchema):
    id: int
    product: ProductSchema | None
    quantity: int

    class Config:
        from_attributes = True


class OrderAddSchema(BaseModel):
    user_id: int

    order_products: List[OrderProductsAddSchema]

    withdrawn_bonuses: int | None
    total_amount: int

    platform: str
    email: str
    password: str | None
    nickname: str

    status: str
    payment_method: str
    payment_status: str | None
    
    class Config:
        orm_mode = True


class AnswerOrderAddSchema(BaseModel):
    ok: bool
    message: str
    order_id: int


class OrderSchema(BaseModel):
    id: int
    user: UserSchema
    order_products: List[OrderProductsSchema]
    withdrawn_bonuses: int | None
    total_amount: int

    platform: str
    email: str
    password: str | None
    nickname: str

    status: str
    payment_method: str
    payment_status: str | None

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AnswerOrderSchema(BaseModel):
    ok: bool
    message: str
    order: OrderSchema


class AnswerOrdersSchema(BaseModel):
    ok: bool
    message: str
    orders: List[OrderSchema]