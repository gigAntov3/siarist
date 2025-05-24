from typing import List
from datetime import datetime
from pydantic import BaseModel


class ProductAddSchema(BaseModel):
    name: str
    description: str | None
    price: int
    tag: str | None
    category_id: int

    class Config:
        orm_mode = True


class AnswerProductAddSchema(BaseModel):
    ok: bool
    message: str
    product_id: int

    class Config:
        orm_mode = True


class ProductSchema(ProductAddSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AnswerProductSchema(BaseModel):
    ok: bool
    message: str
    product: ProductSchema

    class Config:
        orm_mode = True


class AnswerProductsSchema(BaseModel):
    ok: bool
    message: str
    products: List[ProductSchema]

    class Config:
        orm_mode = True


class ProductUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    tag: str | None = None
    category_id: int | None = None


class AnswerProductUpdateSchema(BaseModel):
    ok: bool
    message: str

    
class AnswerProductDeleteSchema(BaseModel):
    ok: bool
    message: str