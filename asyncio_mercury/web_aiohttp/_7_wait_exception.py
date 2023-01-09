import asyncio
import aiohttp
import sys
import logging

from aiohttp import ClientSession
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _3_time_out import fetch_status
from utilq.async_timer import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_req = fetch_status(session, 'https://www.vkusnyblog.ru/')
        bad_req = fetch_status(session, 'https://bad')

        fetchers = [asyncio.create_task(good_req),
                    asyncio.create_task(bad_req)]
        done, pending = await asyncio.wait(fetchers)
        
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Exception', exc_info=done_task.exception())
        
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
