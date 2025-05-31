import time
import hmac
import hashlib
import requests
from fastapi import APIRouter, Query, HTTPException, Request, Depends

from schemas import AnswerSchema
from schemas.payments import FreeKassaPaymentSchema, InputFreeKassaPaymentSchema

from services.orders import OrdersService
from services.telegram import TelegramService

from api.v1.dependencies.orders import orders_service
from api.v1.dependencies.telegram import telegram_service

router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)

API_KEY = "8e79422fb7bc7f93317f221af98348b5"
SHOP_ID = 62587
FREE_KASSA_API_URL = 'https://api.fk.life/v1/orders/create'


def build_payment_data(order_id: int, amount: int, currency: str, email: str, ip: str) -> dict:
    return {
        "shopId": SHOP_ID,
        "nonce": int(time.time()),
        "i": 6,
        "email": email,
        "ip": ip,
        "amount": amount,
        "currency": currency,
        "us_order_id": order_id
    }


def generate_signature(data: dict, api_key: str) -> str:
    sorted_items = dict(sorted(data.items()))
    sign_string = '|'.join(str(value) for value in sorted_items.values())
    return hmac.new(
        api_key.encode("utf-8"),
        sign_string.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def create_payment_request(data: dict) -> dict:
    response = requests.post(
        FREE_KASSA_API_URL,
        json=data,
        timeout=10
    )
    if response.ok:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail={'error': response.text})


@router.get("/", response_model=FreeKassaPaymentSchema)
async def get_payment_link(
    order_id: int = Query(...),
    amount: int = Query(...),
    currency: str = Query(..., min_length=3, max_length=3),
    email: str = Query(...),
    ip: str = Query(...),
) -> FreeKassaPaymentSchema:
    data = build_payment_data(order_id, amount, currency, email, ip)
    data["signature"] = generate_signature(data, API_KEY)
    result = create_payment_request(data)
    return FreeKassaPaymentSchema(url=result["location"])




@router.post("/")
async def debug(
    request: Request,
    orders_service: OrdersService = Depends(orders_service),
    telegram_service: TelegramService = Depends(telegram_service),
):
    form = await request.form()
    body_data = dict(form)

    payment = InputFreeKassaPaymentSchema(
        order_id=body_data["us_order_id"],
        merchant_id=body_data["MERCHANT_ID"],
        merchant_order_id=body_data["MERCHANT_ORDER_ID"],
        amount=body_data["AMOUNT"],
        email=body_data["P_EMAIL"],
    )

    order = await orders_service.get_order(payment.order_id)

    await orders_service.update_payment_status(payment.order_id, "success")

    await telegram_service.send_order_to_admin(order)

    return AnswerSchema(ok=True, message="Payment success")



    




# https://pay.freekassa.net/?m=62587&oa=1000&o=12345&s=0fdd58a59e26b136bbe164a4c6191c18&currency=RUB&us_order_id=16