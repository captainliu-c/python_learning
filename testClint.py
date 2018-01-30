#testClint

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))
#接受超过1K，会打印不全吗
for data in [b'Micheal', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    #发、收反复进行不会乱吗

s.send(b'exit')
#print(s.recv(1024).decode('utf-8'))
s.close()
