import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\n\n cara nk guna ada di bwh: \n python3 client.py < letak ip address server di sini> \n\n contoh: \n python3 client.py 100.200.23.123 \n\n")
    exit(1)


s = socket.socket()

PORT = 9090

s.connect((ServerIp, PORT))

file = open("sample.txt", "rb")
SendData = file.read(1024)


while SendData:
    print("\n\n____incoming messege dari server___\n", s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)      

s.close()

