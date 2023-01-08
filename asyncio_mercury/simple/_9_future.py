import asyncio
from asyncio import Future

# my_future = Future()
# print(my_future.done())
# my_future.set_result(42)
# print(my_future.done())
# print(my_future.result())

def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)

async def main():
    future = make_request()
    print(future.done())
    value = await future
    print(future.done())
    print(value)

asyncio.run(main())