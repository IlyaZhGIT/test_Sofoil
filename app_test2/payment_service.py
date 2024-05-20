from uuid import uuid4

import aiohttp
from models import NewPayment, Payment, PaymentStatus, Refund


class PaymentService:
    # - авторизация платежа
    async def payment_status_authorization(self, payment_id: uuid4) -> PaymentStatus:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"megasuperpay.com/api/payment/{payment_id}/status",
                headers={"Authorization": "Bearer 1234567890"},
            ) as resp:
                self.check_http_status(resp.status)
                data = await resp.json()
                return PaymentStatus(**data)

    # - оплата
    async def create_payment(self, new_payment: NewPayment) -> Payment:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url="megasuperpay.com/api/payment",
                json=new_payment.model_dump(),
                headers={"Authorization": "Bearer 1234567890"},
            ) as resp:
                self.check_http_status(resp.status)
                data = await resp.json()
                return Payment(**data)

    # - возврат платежа
    async def create_refund(self, payment_id: uuid4) -> Refund:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"megasuperpay.com/api/payment/{payment_id}/refund",
                headers={"Authorization": "Bearer 1234567890"},
            ) as resp:
                self.check_http_status(resp.status)
                data = await resp.json()
                return Refund(**data)

    @staticmethod
    def check_http_status(http_status: int) -> None:
        if http_status == 201:
            return None
        elif http_status == 404:
            raise ValueError("Некорректные данные")
        elif http_status == 500:
            raise ValueError("Внешний сервис недоступен")
        else:
            raise ValueError("Неизвестная ошибка внешнего сервиса")
