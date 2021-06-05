import socket
import sys
import json

s = socket.socket()

port = 8080

s.connect(('192.168.56.102', port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client!');

dataJ = json.loads(data)

print (type(dataJ))
print(dataJ)

s.close()
