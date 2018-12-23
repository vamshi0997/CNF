import socket
from threading import *
def Main():
    host = '127.0.0.1'
    port = 6060
    soc = socket.socket()

    soc.connect((host, port))
    roll = input('MARK-ATTENDANCE:')
    soc.send(('MARK-ATTENDANCE:' + roll).encode())
    Thread(target = client_thread, args=(soc,)).start()
    soc.close()

def client_thread(soc):
    while True:
        question = soc.recv(1024).decode()
        print(question)
        question = question.split("-")
        if (question[0] == 'SECRETQUESTION'):
            ans = input('respond to question:')
            soc.send(('SECRETANSWER-'+ ans).encode())
        if question[0] == 'ATTENDANCE SUCESS':
            print('ATTENDANCE SUCESS')
            break
        if question[0] == 'ATTENDANCE FAILURE':
            print('ATTENDANCE FAILURE')
            break
        if question[0] == 'ROLL NUMBER NOT FOUND':
            print('you rollnumber are not existed')
            break


if __name__ == '__main__':
    Main()
