import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='192.168.180.128',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')

    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())