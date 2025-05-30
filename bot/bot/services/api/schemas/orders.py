from typing import List, Optional, Union, Dict, Any, Literal 

from datetime import datetime

from pydantic import BaseModel

from .users import User
from .products import Product


class OrderProduct(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: Product


class Order(BaseModel):
    id: int
    user: User
    order_products: List[OrderProduct]
    withdrawn_bonuses: int
    total_amount: int
    platform: str
    email: str
    password: str | None
    nickname: str
    status: str
    payment_method: str
    payment_status: str
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True


class AnswerOrder(BaseModel):
    ok: bool
    message: str
    order: Order