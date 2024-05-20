"""
Написать сервис для коммуникации с внешним сервисом megasuperpay.com (выдуманный сервис) для выполнения оплаты с использованием кредитных карт
…сть несколько ограничений, необходимо их учесть:
1) реализовать 3 метода: 
	- авторизация платежа
	- оплата
	- возврат платежа
2) авторизация на сервисе делается через bearer с помощью токена "1234567890"
3) предусмотреть обработку ошибок через http status code
4) предусмотреть базовую валидацию данных

Все сигнатуры методов не описаны и могут быть произвольными, передача и получение параметров так же на усмотрение разработчика
"""

import logging
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from models import NewPayment, Payment, PaymentStatus, Refund
from payment_service import PaymentService

app = FastAPI()
payment_service = PaymentService()


@app.post("/payment")
async def create_payment(new_payment: NewPayment) -> Payment:
    try:
        payment: Payment = await payment_service.create_payment(new_payment)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])
    except Exception as err:
        logging.error(err)
        raise HTTPException(status_code=500, detail="Ошибка сервиса")
    return payment


@app.post("/payment/{payment_id}/refund")
async def create_refund(payment_id: uuid4) -> Refund:
    try:
        refund: Refund = await payment_service.create_refund(payment_id)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])
    except Exception as err:
        logging.error(err)
        raise HTTPException(status_code=500, detail="Ошибка сервиса")
    return refund


@app.get("/payment/{payment_id}/status")
async def payment_status_authorization(payment_id: uuid4) -> PaymentStatus:
    try:
        payment_status: PaymentStatus = (
            await payment_service.payment_status_authorization(payment_id)
        )
    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])
    except Exception as err:
        logging.error(err)
        raise HTTPException(status_code=500, detail="Ошибка сервиса")
    return payment_status


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
