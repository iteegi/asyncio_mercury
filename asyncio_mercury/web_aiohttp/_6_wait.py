import asyncio
import aiohttp
import sys

from aiohttp import ClientSession
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.async_timer import async_timed
from _3_time_out import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.vkusnyblog.ru/')),
                    asyncio.create_task(fetch_status(session, 'https://www.vkusnyblog.ru/')),]
        
        done, pending = await asyncio.wait(fetchers)

        print(f'Done task count: {done}')
        print(f'Pending task count: {pending}')

        for done_task in done:
            res = await done_task
            print(res)
        
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
