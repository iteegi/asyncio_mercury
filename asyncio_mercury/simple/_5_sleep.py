import asyncio
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utilq.delay_functions import delay


async def add_one(n: int) -> int:
    return n + 1


async def hw_mes() -> str:
    await delay(1)
    return 'HW'


async def main() -> None:
    mes = await hw_mes()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(mes)

asyncio.run(main())
