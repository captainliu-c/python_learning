# testWith.py

class Sample():
    def __enter__(self):
        print('i am enter')
        #return 'i am return'

    def __exit__(self, type, value, trace):
        print(' i am exit')

'''
def test():
    return Sample()

with test() as sample:
    print('sample:', sample)
'''

a = Sample()

with a as sample:
    print('sample:', sample)
