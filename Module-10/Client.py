import socket
import threading

soc = socket.socket()
user = input("Enter username:")
host = "127.0.0.1"
port = 7070
soc.connect((host,port))

def client_thread(soc):
    while True:
        message = soc.recv(1024).decode()
        print(message)

threading.Thread(target = client_thread,args=(soc,)).start()

while True:
    tmessage = input()
    message = user+'>>'+tmessage 
    soc.send(message.encode())
