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
        url = 'https://www.vkusnyblog.ru/'

        pending = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url))]
        
        while pending:
            done, pending = await asyncio.wait(pending,
                                            return_when=asyncio.FIRST_COMPLETED)
                    
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)
        
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
