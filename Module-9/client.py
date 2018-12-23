from threading import Thread
import socket

host = '127.0.0.1'
port  = 8080
soc = socket.socket()
soc.connect((host, port))

def main(server):
    data = b''
    while True:
        try:
            data = server.recv(1024)
        except:
            break
        if len(data) > 2:
            print(str(data.decode()))
        elif data and (len(data) == 1 or 2):
            print('server responce: ' + str(data.decode()))
        else:
            break
    server.close()

def client_thread():
    message = input('')
    while message != 'quit':
        soc.send(message.encode())
        message = input("your response:")
    soc.close()

if __name__ == '__main__':

    new = Thread(target = main, args=(soc,))
    newthread = Thread(target = client_thread)
    new.start()
    newthread.start()
    new.join()
    newthread.join()
