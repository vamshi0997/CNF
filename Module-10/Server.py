import socket
import threading
soc = socket.socket()
host = '127.0.0.1'
port = 7070
users = []
soc.bind((host,port))
soc.listen(10)
print("Server Started....")
print("IP Address of the Server: %s " %host)

def sever_thread(conn):
    while True:
        message = conn.recv(1024).decode()
        for user in users:
            if conn != user:
                user.send(message.encode())

while True:
    conn, addr = soc.accept()
    print("%s connected to the server.."%str(addr))
    conn.send("Welcome to chat Messenger".encode())

    if (soc not in users):
        users.append(conn)
        threading.Thread(target = sever_thread, args=(conn,)).start()
