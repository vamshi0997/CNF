import socket
from _thread import *
import threading
import random

connections = {}
r = random.randint(1, 50)
print("actual number", r)

def clientthread(conn, addr,connections):
    note = '$ welcome to Game ... \n$ enter your name and guess a number between 1 and 50'
    high = 'Opps...your guess is greater than value!'
    low = 'Opps...guess is lesser than value!'
    conn.send(note.encode())
    try:
        data = conn.recv(1024)
    except:
        return
    username = data.decode()
    connections[conn] = username
    print('user -->' + str(addr) + ' : ' + username)
    while True:
        answer = ''.encode()
        try:
            answer = conn.recv(1024)
            print('Guess :' + answer.decode())
        except:
            break

        for connx in connections:
            if  connx != conn and answer != b'playlist':
                msg = username + " guessed " + answer.decode()
                connx.send(msg.encode())

        if (str(answer.decode()) == 'playlist'):
            lplay = '\n'+'\n'.join(connections[i] for i in connections)
            conn.send(lplay.encode())
        elif (int(answer.decode()) > r):
            conn.send(high.encode())
        elif (int(answer.decode()) < r):
            conn.send(low.encode())
        else:
            conn.send('guess is correct'.encode())
            for connx in connections:
                result = "Winner is " + username + " gameover"
                connx.send(result.encode())
            break
    conn.close()

def Main():
    host = '127.0.0.1'
    port  = 8080
    soc = socket.socket()
    soc.bind((host, port))
    soc.listen(10)
    print('Sever has Stared...')
    while True:
        conn, addr = soc.accept()
        print('connected from ..' + str(addr))
        start_new_thread(clientthread, (conn, addr,connections))
    soc.close()

if __name__ == '__main__':
         Main()



