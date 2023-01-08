import asyncio
import aiohttp
import sys

from aiohttp import ClientSession
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.async_timer import async_timed
from _3_time_out import fetch_status


@async_timed()
async def  main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://www.vkusnyblog.ru/' for _ in range(100)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())