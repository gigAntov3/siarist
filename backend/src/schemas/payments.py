
from pydantic import BaseModel



class InputFreeKassaPaymentSchema(BaseModel):
    merchant_id: int
    amount: int
    merchant_order_id: int
    email: str
    order_id: int



class FreeKassaPaymentSchema(BaseModel):
    url: str