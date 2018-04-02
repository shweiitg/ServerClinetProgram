import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
while(True):
    print(s.recv(1024))
    ip = input()
    s.send(ip.encode('utf-8'))
s.close()
