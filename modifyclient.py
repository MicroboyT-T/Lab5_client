import socket
import sys

s = socket.socket()
host = '192.168.56.102'
port = 8888

s.connect((host, port))

filename='virus.txt'
f = open(filename, 'rb')
l = f.read(1024)
while(l):
    s.send(l)
    print('Sending to server ', repr(l))
    l = f.read(1024)
f.close()

print('Done sending file to server...')
s.send(b'\nThank you from client!')
s.close()
