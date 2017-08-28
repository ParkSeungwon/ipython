import socket
mysock = socket.socket();
mysock.connect(('localhost', 80))
mysock.send('GET http://localhost/index.html HTTP/1.1\n\n')

while True:
    data=mysock.recv(512)
    if len(data) < 1: break
    print data

mysock.close()
