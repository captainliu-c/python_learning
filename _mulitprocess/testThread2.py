# testThread2.py

import time, threading

balance = 0
lock = threading.Lock()


'''
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)
'''


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire() #为什么需要try，acqure为什么放在try外面？
        try:
            change_it(n)
        finally:
            lock.release()

#为什么用try，这是一个安全的写法，保证当acquire后续的代码出现问题后，线程被一直阻塞

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

