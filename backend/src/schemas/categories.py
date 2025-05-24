from typing import List
from datetime import datetime
from pydantic import BaseModel


class CategoryAddSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AnswerCategoryAddSchema(BaseModel):
    ok: bool
    message: str
    category_id: int


class CategorySchema(CategoryAddSchema):
    id: int

    class Config:
        orm_mode = True

    
class AnswerCategorySchema(BaseModel):
    ok: bool
    message: str
    category: CategorySchema


class AnswerCategoriesSchema(BaseModel):
    ok: bool
    message: str
    categories: List[CategorySchema]