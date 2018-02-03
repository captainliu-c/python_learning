# testRe.py

'侧重的是提取group，而不是验证是否合法'

import re

def name_of_email(addr):
    name = re.split(r'[\@]', addr)
    if len(name) != 2:
        othername = re.split()
    return name[0]

def test(addr):
    temp = re.split('[\<\>\@]', addr)
    for i in temp:
        print(i)
        
    

#assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
#assert name_of_email('tom@voyager.org') == 'tom'
#print('ok')

test('tom@voyager.org')
