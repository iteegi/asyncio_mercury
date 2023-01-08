import asyncio
import aiohttp
import sys

from aiohttp import ClientSession
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://google.com'
        status = await fetch_status(session, url)
        print(f'Status for {url} was {status}')

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
