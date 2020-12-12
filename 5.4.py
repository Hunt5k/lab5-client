import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\n\n Run like \n python3 client.py < serverip address > \n\n")
    exit(1)


s = socket.socket()

PORT = 9898

s.connect((ServerIp, PORT))

file = open("sample.txt", "rb")
SendData = file.read(1024)


while SendData:
    print("\n\n##################____incoming messege from server___#################\n\n", s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)      

s.close()

