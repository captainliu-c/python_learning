# testAsyncio.py

import asyncio, threading

'''
@asyncio.coroutine
def hello():
    print('hello world')
    r = yield from asyncio.sleep(1)
    print('hello again!')

def main(x):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(x)
    loop.close()

x = hello()
#main(x)
'''

@asyncio.coroutine
def hello():
    print('hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
#1.asyncio.wait干什么用？2._complete()接收什么参数？
loop.close()

