from _3_time_out import fetch_status
import asyncio
import aiohttp
import sys

from aiohttp import ClientSession
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.async_timer import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.vkusnyblog.ru/', 1),
                    fetch_status(session, 'https://www.vkusnyblog.ru/', 1),
                    fetch_status(session, 'https://www.vkusnyblog.ru/', 10),]
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print(f'Time-out')
        
        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
