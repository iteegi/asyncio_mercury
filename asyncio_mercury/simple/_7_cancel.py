import asyncio
import sys

from asyncio import CancelledError

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.delay_functions import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print(f'The task is working!!!')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print(f'The task has been cancelled')

asyncio.run(main())