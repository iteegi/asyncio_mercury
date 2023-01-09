import asyncio
import asyncpg


async def main():
    conn = await asyncpg.connect(host='192.168.180.128',
                                 port=5432,
                                 user='postgres',
                                 database='products',
                                 password='postgres')
    version = conn.get_server_version()
    print(f'{version}')
    await conn.close()

asyncio.run(main())