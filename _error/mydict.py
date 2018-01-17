# mydict.py
import unittest

class Dict(dict):


    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute: %s" % key)

    def __setattr__(self, key, value):
        self[key] = value
        
'''
如果用a=dict(),来给变量a赋值，那么就不能用a.key
如果用a=Dict(),来给变量a赋值，那么就可以使用a.key

a.key是对类属性的调用，两者的区别是dict是python原生的数据类型，
而Dict是继承自dict，那么深层原因是为甚呢？

def main():
    d = Dict()
    d.key = 'value'
    print(d.key)
    b = dict()
    d.key = 'nimei'
    print(d.key)
'''

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict)) 

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value' 
        self.assertTrue('key' in d) 
        self.assertEqual(d['key'], 'value') #为毛不用d.key这个方式了？

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty'] 

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()
