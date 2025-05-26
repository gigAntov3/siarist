from typing import List
from datetime import datetime
from pydantic import BaseModel

from .products import ProductSchema


class BasketAddSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True


class AnswerBasketAddSchema(BaseModel):
    ok: bool
    message: str
    basket_id: int


class BasketSchema(BaseModel):
    id: int
    user_id: int
    product: ProductSchema
    quantity: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AnswerBasketSchema(BaseModel):
    ok: bool
    message: str
    basket: BasketSchema


class AnswerBasketsSchema(BaseModel):
    ok: bool
    message: str
    baskets: List[BasketSchema]



