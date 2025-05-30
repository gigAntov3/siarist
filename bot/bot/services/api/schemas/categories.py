from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class AnswerCategories(BaseModel):
    ok: bool
    message: str
    categories: List[Category]


class AnswerCategory(BaseModel):
    ok: bool
    message: str
    category: Category