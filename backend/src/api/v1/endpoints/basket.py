from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas import AnswerSchema
from schemas.basket import (
    BasketSchema,
    AnswerBasketSchema,
    BasketAddSchema,
    AnswerBasketAddSchema,
    AnswerBasketsSchema,
)

from services.basket import BasketService

from api.v1.dependencies.basket import basket_service


router = APIRouter(
    prefix="/basket",
    tags=["Basket"],
)


@router.post("")
async def add_basket(
    basket: BasketAddSchema,
    basket_service: Annotated[BasketService, Depends(basket_service)]
) -> AnswerBasketAddSchema:
    basket_id = await basket_service.add_basket(basket)
    return AnswerBasketAddSchema(ok=True, message="Category added successfully", basket_id=basket_id)


@router.get("/{basket_id}")
async def get_basket(
    basket_id: int,
    basket_service: Annotated[BasketService, Depends(basket_service)]
) -> AnswerBasketSchema:
    basket = await basket_service.get_basket(basket_id)
    return AnswerBasketSchema(ok=True, message="Category retrieved successfully", basket=basket)


@router.get("")
async def get_baskets(
    basket_service: Annotated[BasketService, Depends(basket_service)],
) -> AnswerBasketsSchema:
    baskets = await basket_service.get_baskets()
    return AnswerBasketsSchema(ok=True, message="Categories retrieved successfully", baskets=baskets)


@router.post("/{basket_id}/increase")
async def increase_quantity(
    basket_id: int,
    basket_service: Annotated[BasketService, Depends(basket_service)]
) -> AnswerSchema:
    is_increased = await basket_service.increase_quantity(basket_id)

    if not is_increased:
        return AnswerSchema(ok=False, message="Quantity increase failed")
    
    return AnswerSchema(ok=True, message="Quantity increased successfully")


@router.post("/{basket_id}/decrease")
async def decrease_quantity(
    basket_id: int,
    basket_service: Annotated[BasketService, Depends(basket_service)]
) -> AnswerSchema:
    is_decreased = await basket_service.decrease_quantity(basket_id)

    if not is_decreased:
        return AnswerSchema(ok=False, message="Quantity decrease failed")
    
    return AnswerSchema(ok=True, message="Quantity decreased successfully")


@router.delete("/")
async def delete_baskets(
    basket_service: Annotated[BasketService, Depends(basket_service)],
    user_id: int = Query(None, ge=1),
) -> AnswerSchema:
    await basket_service.delete_baskets()
    return AnswerSchema(ok=True, message="Baskets deleted successfully")


@router.delete("/{basket_id}")
async def delete_basket(
    basket_id: int,
    basket_service: Annotated[BasketService, Depends(basket_service)],
) -> AnswerSchema:
    await basket_service.delete_basket(basket_id)
    return AnswerSchema(ok=True, message="Basket deleted successfully")
