import socket
from threading import *

host = '127.0.0.1'
port = 5000
soc = socket.socket()
try:
    soc.connect((host, port))
except:
    print('error in server..')
    return
new = Thread(target = client_thread, args = (soc,)).start()
while True:
    data = soc.recv(1024).decode()
    if (data == 'ATTENDANCE SUCCESS' or data == 'ROLL NUMBER-NOT FOUND'):
        print(data)
        break
    print(data)
soc.close()


def server_thread(soc):
    while True:
        message = input()
        soc.send(message.encode())
    soc.close()
