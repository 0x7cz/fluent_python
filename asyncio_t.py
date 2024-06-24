import threading
import asyncio
# 使用协程必须保证库函数支持协程,比如aiohttp，aiofiles
async def hello():
    print('Hello world! (%s)' % threading.current_thread())
    # await asyncio.sleep(1)
    import time
    time.sleep(3)  # 使用io阻塞会阻塞整个线程
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())

loop = asyncio.new_event_loop()
a1 = loop.create_task(hello())
a2 = loop.create_task(hello())
tasks = [a1, a2]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()