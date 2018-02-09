# testTask2.py

import asyncio, time

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(1)
    return 'Done after {}s'.format(x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print(task.result())
print(now()-start)
