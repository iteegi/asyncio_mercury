import asyncio


async def delay(delay_sec: int) -> int:
    print(f'Заснуть на {delay_sec} сек')
    await asyncio.sleep(delay_sec)
    print(f'Сон в течении {delay_sec} сек закончился')

    return delay_sec
