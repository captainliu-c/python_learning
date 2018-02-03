# testContextmanager.py

from contextlib import contextmanager

@contextmanager
def make_context():
    print('enter')
    a = 1
    b = 2
    try:
        yield a,b 
    except RuntimeError as err:
        print(err)

    finally :
        print('exit')

with make_context() as value:
    print(value)
