import asyncio

async def coroutine_add_one(n: int) -> int:
    return n + 1

def add_one(n: int) -> int:
    return n + 1

f_res = add_one(1)
c_res = coroutine_add_one(1)

print(f'Результат функции = {f_res}, тип результата {type(f_res)}')
print(f'Результат сопрограммы = {c_res}, тип результата {type(c_res)}')


res = asyncio.run(coroutine_add_one(1))
print(res)
