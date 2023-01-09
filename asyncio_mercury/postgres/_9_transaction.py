import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='192.168.180.128',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    async with connection.transaction():
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_2')")

    query = """SELECT brand_name FROM brand 
                WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())