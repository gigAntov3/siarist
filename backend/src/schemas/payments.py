
from pydantic import BaseModel



class FreeKassaResultSchema(BaseModel):
    merchant_id: int
    amount: int
    merchant_order_id: int
    email: str
    order_id: int



class PaymentSchema(BaseModel):
    url: str






class PallyResultSchema(BaseModel):
    status: str
    order_id: str
    commission: float
    currency: str
    out_sum: float
    trs_id: str
    custom: str | None
    signature: str





class AnswerPallyCreateBillSchema(BaseModel):
    success: bool
    bill_id: str
    link_url: str
    link_page_url: str

    class Config:
        from_attributes = True


class AnswerPallyGetBillStatusSchema(BaseModel):
    success: bool
    id: str
    active: bool
    status: str
    type: str
    amount: int
    currency_in: str
    created_at: str
    success: bool

    class Config:
        from_attributes = True