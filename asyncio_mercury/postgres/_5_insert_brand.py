import asyncpg
import asyncio
from typing import List, Tuple
from random import sample


def load_common_words() -> List[str]:
    with open('./data/common_words.txt', mode='r') as c_words:
        return c_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[str, int]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    connection = await asyncpg.connect(host='192.168.180.128',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    await insert_brands(load_common_words(), connection)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())