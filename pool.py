# pool.py
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    temp = random.random() * 10
    time.sleep(temp)
    end = time.time()
    print('Task %s runs %0.2f seconds.|| The random is %f' % (name, end-start, temp))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waitting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
