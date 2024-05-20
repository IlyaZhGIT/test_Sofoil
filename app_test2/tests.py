import aiohttp
import asyncio


async def f():
    async with aiohttp.ClientSession() as session:
        payment_id = 1
        url = f"http://127.0.0.1:8000/payment/"
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json={"card_number": "4111111111111111", "amount": 1999}
            ) as response:
                r = await response.text()
                return r


async def main():
    r = await f()
    print(r)


asyncio.run(main())
