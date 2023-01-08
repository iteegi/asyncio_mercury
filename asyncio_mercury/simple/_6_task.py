import asyncio
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.delay_functions import delay


async def every_second():
    for _ in range(5):
        await asyncio.sleep(1)


async def main():
    sl_1 = asyncio.create_task(delay(3))
    sl_2 = asyncio.create_task(delay(3))
    sl_3 = asyncio.create_task(delay(3))
    await every_second()
    print(type(sl_1))
    res = await sl_1
    await sl_2
    await sl_3
    print(res)

asyncio.run(main())
