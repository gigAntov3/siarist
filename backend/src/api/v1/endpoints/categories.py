from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas import AnswerSchema
from schemas.categories import (
    CategorySchema,
    AnswerCategorySchema,
    CategoryAddSchema,
    AnswerCategoryAddSchema,
    AnswerCategoriesSchema
)

from services.categories import CategoriesService

from api.v1.dependencies.categories import categories_service


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("")
async def add_category(
    category: CategoryAddSchema,
    categories_service: Annotated[CategoriesService, Depends(categories_service)]
) -> AnswerCategoryAddSchema:
    category_id = await categories_service.add_category(category)
    return AnswerCategoryAddSchema(ok=True, message="Category added successfully", category_id=category_id)


@router.get("")
async def get_categories(
    categories_service: Annotated[CategoriesService, Depends(categories_service)],
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
) -> AnswerCategoriesSchema:
    categories = await categories_service.get_categories(limit=limit, offset=offset)
    return AnswerCategoriesSchema(ok=True, message="Categories retrieved successfully", categories=categories)


@router.get("/{category_id}")
async def get_category(
    category_id: int,
    categories_service: Annotated[CategoriesService, Depends(categories_service)],
) -> AnswerCategorySchema:
    category = await categories_service.get_category(category_id)
    return AnswerCategorySchema(ok=True, message="Category retrieved successfully", category=category)


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    categories_service: Annotated[CategoriesService, Depends(categories_service)],
) -> AnswerSchema:
    await categories_service.delete_category(category_id)
    return AnswerSchema(ok=True, message="Category deleted successfully")
