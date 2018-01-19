# dictTest.py

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)
        
    def __getattr__(self, key):
        try:
            print('use getattr')    
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute: %s" % key)
    
    def __setattr__(self, key, value):
        print(self)
        print('use setattr')
        self[key] = value
        
def main():
    print('begin')
    d = Dict()
    d.x = 'nimei'
    print(d)
    print(d.x)
    #print(d.x)
    '''
    for i in d:
        print(i)
    print('Dict test finish')
    # 测试普通的dict

    
    b = dict()
    b.key = 'value_b'
    print(b.key)
    
   
    b = Dict2()
    b.x='aaa'
    print(b.x)
    '''
main()
