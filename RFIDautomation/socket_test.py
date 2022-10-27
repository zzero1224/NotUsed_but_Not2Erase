import os
from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
res = sock.connect(('192.168.1.20', 9100))
sock.settimeout(1)

file = open("RFID_format.txt")
strings = file.readlines()
file.close

for i in range(len(strings)):
    strings[i] = strings[i].replace("\n","\r\n")

if res:
    print("none")
else:
    print("open")

sock.sendall("~S,CHECK\r\n".encode("utf-8"))
# data = sock.recv(1024)
#--------------nogada--------------
# sock.sendall("~B\r\n".encode("utf-8"))
# time.sleep(0.1)
# sock.sendall("~HS03,18\r\n".encode("utf-8"))
# time.sleep(0.1)
# sock.sendall("~E20,3000\r\n".encode("utf-8"))

# #--------------from format--------------
# print("send from format")
# for i in range(6):
#     time.sleep(0.1)
#     sock.send(strings[i].encode("utf-8"))
# time.sleep(0.1)
# for i in range(6):
#     sock.send(strings[i+6].encode("utf-8"))

sock.close()

