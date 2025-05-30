from typing import List, Optional, Union, Dict, Any, Literal 

from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    tag: str
    photo: str
    category_id: int
    created_at: datetime
    updated_at: datetime


class AnswerProduct(BaseModel):
    ok: bool
    message: str
    product: Product


class AnswerProductAdd(BaseModel):
    ok: bool
    message: str
    product_id: int


class AnswerProducts(BaseModel):
    ok: bool
    message: str
    products: List[Product]