from fastapi import APIRouter, Depends, Query

from typing import Annotated

from schemas.orders import (
    OrderAddSchema,
    AnswerOrderAddSchema,
    AnswerOrdersSchema,
    AnswerOrderSchema,
)

from services.orders import OrdersService

from api.v1.dependencies.orders import orders_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/")
async def add_order(
    order: OrderAddSchema, 
    orders_service: OrdersService = Depends(orders_service)
) -> AnswerOrderAddSchema:
    order_id = await orders_service.add_order(order)
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