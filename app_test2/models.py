import enum
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from pydantic import BaseModel, Field
from pydantic_extra_types.payment import PaymentCardNumber


class Status(enum.Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class PaymentStatus(BaseModel):
    status: Status


class NewPayment(BaseModel):
    card_number: PaymentCardNumber
    amount: Decimal = Field(..., gt=0)


class Payment(BaseModel):
    id: uuid4
    created_at: datetime
    amount: Decimal
    status: Status
    card_number: int


class NewRefund(BaseModel):
    payment_id: uuid4


class Refund(BaseModel):
    id: uuid4
    created_at: datetime
    amount: Decimal
    status: PaymentStatus
    card_number: int
