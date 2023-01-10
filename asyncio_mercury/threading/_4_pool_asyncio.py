import functools
import requests
import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.async_timer import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())