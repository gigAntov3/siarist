import time
import hmac
import hashlib
import requests
from fastapi import APIRouter, Query, HTTPException, Request, Depends

from utils.payments import FreeKassaClient, PallyClient
from schemas import AnswerSchema
from schemas.payments import (
    PaymentSchema, 
    FreeKassaResultSchema,
    PallyResultSchema
)

from services.orders import OrdersService
from services.telegram import TelegramService

from api.v1.dependencies.orders import orders_service
from api.v1.dependencies.telegram import telegram_service

router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)

FREEKASSA_SHOP_ID = 62587
FREEKASSA_API_KEY = "8e79422fb7bc7f93317f221af98348b5"

PALLY_SHOP_ID = "kd71ZWyv1K"
PALLY_API_KEY = "23212|1bUrTxfWReibMVjlqUdfYkBroGbDDmCuYzFYgw6L"


@router.get("/")
async def get_payment_link(
    method: str = Query(...),
    order_id: int = Query(...),
    amount: int = Query(...),
    currency: str = Query(..., min_length=3, max_length=3),
    email: str = Query(...),
    ip: str = Query(...),
) -> PaymentSchema:
    if method == "sbp":
        client = FreeKassaClient(FREEKASSA_SHOP_ID, FREEKASSA_API_KEY)

        payment = await client.create_payment(
            order_id=order_id,
            amount=amount,
            currency=currency,
            email=email,
            ip=ip
        )

    elif method == "card":
        client = PallyClient(PALLY_SHOP_ID, PALLY_API_KEY)

        payment = await client.create_payment(
            order_id=order_id,
            amount=amount,
            currency=currency,
        )

    return payment




@router.post("/freekassa")
async def freekassa_callback(
    request: Request,
    orders_service: OrdersService = Depends(orders_service),
    telegram_service: TelegramService = Depends(telegram_service),
):
    form = await request.form()
    body_data = dict(form)

    payment = FreeKassaResultSchema(
        order_id=body_data["us_order_id"],
        merchant_id=body_data["MERCHANT_ID"],
        merchant_order_id=body_data["MERCHANT_ORDER_ID"],
        amount=body_data["AMOUNT"],
        email=body_data["P_EMAIL"],
    )
    await orders_service.update_payment_status(payment.order_id, "success")

    order = await orders_service.get_order(payment.order_id)

    await telegram_service.send_payment_info_to_user(order)

    await telegram_service.send_order_to_admin(order)

    return AnswerSchema(ok=True, message="Payment success")



@router.post("/pally")
async def pally_callback(
    request: Request,
    orders_service: OrdersService = Depends(orders_service),
    telegram_service: TelegramService = Depends(telegram_service),
):
    form = await request.form()
    body_data = dict(form)

    payment = PallyResultSchema(
        status=body_data["Status"],
        order_id=int(body_data["InvId"]),
        commission=float(body_data["Commission"]),
        currency=body_data["Currency"],
        out_sum=float(body_data["OutSum"]),
        trs_id=body_data["TrsId"],
        signature=body_data["SignatureValue"],
    )
    await orders_service.update_payment_status(payment.order_id, "success")

    order = await orders_service.get_order(payment.order_id)

    if payment.status == "SUCCESS":
        await telegram_service.send_payment_info_to_user(order)
        await telegram_service.send_order_to_admin(order)

        return AnswerSchema(ok=True, message="Payment success")
    else:
        await orders_service.update_payment_status(payment.order_id, "failed")

        return AnswerSchema(ok=True, message="Payment failed")