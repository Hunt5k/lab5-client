import socket

s = socket.socket()

port = 8888
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("192.168.43.3",port))

data = s.recv(1048)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
