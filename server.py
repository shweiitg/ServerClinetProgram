import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

c, addr = s.accept()
print('client connected', addr)
while(True):
    ss = input()
    c.send(ss.encode('utf-8'))
    print(c.recv(1024))
c.close()

