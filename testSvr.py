#testSvr.py

import socket
import time, threading

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    #sock.send(b'WOW!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    #%s:%s为什么对应的是一个参数，ip+port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

while True:
    #print('1')
    sock, addr = s.accept()#阻塞
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    #time.sleep(1)
    #print('2')


'''
服务器与客户端之间的收发消息，感觉像是两个先进先出的队列；
目前来看，只要是两个队列的元素数量相同即可，
也就是我发多少个，你就需要收多少个；
因为，毕竟这是符合tcp链接的特性[保证数据包按顺序到达]

关于accept：
1. 本函数会阻塞等待，直到有客户端请求到达
2. 调用accep()，可以返回一个新的socket来处理连接到的客户端请求，
   而原有的socket将继续监听其他请求
'''


    
