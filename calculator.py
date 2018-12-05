import asyncio
import math
import time

async def square_root(x):
  y = math.sqrt(x)
  await asyncio.sleep(x)
  return y
