
import asyncio
import random
import time
import numpy as np

async def count():
    print(1)
    #time.sleep(1)
    await asyncio.sleep(1)
    print(2)
    
async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())



