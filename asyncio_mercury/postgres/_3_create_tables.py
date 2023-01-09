import asyncpg
import asyncio
from _2_sql_for_tables import *


async def main():
    connection = await asyncpg.connect(host='192.168.180.128',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    statements = [CREATE_BRAND_TABLE,
                  CREATE_PRODUCT_TABLE,
                  CREATE_PRODUCT_COLOR_TABLE,
                  CREATE_PRODUCT_SIZE_TABLE,
                  CREATE_SKU_TABLE,
                  SIZE_INSERT,
                  COLOR_INSERT]

    print('Creating the product database...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('Finished creating the product database!')
    await connection.close()


asyncio.run(main())