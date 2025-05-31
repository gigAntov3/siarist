from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas.orders import (
    OrderAddSchema,
    AnswerOrderAddSchema,
    AnswerOrdersSchema,
    AnswerOrderSchema,
)

from services.users import UsersService
from services.orders import OrdersService

from api.v1.dependencies.users import users_service
from api.v1.dependencies.orders import orders_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/")
async def add_order(
    order: OrderAddSchema, 
    orders_service: OrdersService = Depends(orders_service),
    user_service: UsersService = Depends(users_service)
) -> AnswerOrderAddSchema:
    order_id = await orders_service.add_order(order)

    if order.withdrawn_bonuses > 0:
        await user_service.decrease_balance(order.user_id, order.withdrawn_bonuses)

    await user_service.increase_purchases_count(order.user_id)

    await user_service.apply_purchase_bonuses(order.user_id)

    return AnswerOrderAddSchema(ok=True, message="Order added", order_id=order_id)


@router.get("/")
async def get_orders(
    orders_service: OrdersService = Depends(orders_service),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
) -> AnswerOrdersSchema:
    orders = await orders_service.get_orders(limit=limit, offset=offset)
    return AnswerOrdersSchema(
        ok=True, message="Orders retrieved successfully", orders=orders
    )


@router.get("/{order_id}")
async def get_order(
    order_id: int,
    orders_service: OrdersService = Depends(orders_service),
) -> AnswerOrderSchema:
    order = await orders_service.get_order(order_id)
    return AnswerOrderSchema(ok=True, message="Order retrieved successfully", order=order)



# https://pay.freekassa.net/?m=62587&oa=100&o=12345&s=dd862529168d6e8599e0d29ece40f718&currency=RUB


# K2fgAzooTocB9eT