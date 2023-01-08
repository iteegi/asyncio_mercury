import asyncio
import sys


from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.delay_functions import delay

async def main():
    delay_task = asyncio.create_task(delay(10))
    try:
        # res = await asyncio.wait_for(delay_task, timeout=1)
        res = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(res)
    except asyncio.exceptions.TimeoutError:
        print(f'Time out')
        res = await delay_task
        print(delay_task.cancelled())

asyncio.run(main())