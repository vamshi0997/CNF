import socket
import csv
from threading import *

def Main():
    host = '127.0.0.1'
    port = 6060
    s = socket.socket()
    s.bind((host, port))
    s.listen(10)
    print('Server Started..')
    datalist = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            datalist[row[0]] = [row[1], row[2]]
    print('dictionary completed')
    while True:
        conn, addr = s.accept()
        fclient = conn.recv(1024).decode()
        fclient = fclient.split(":")
        rollno = fclient[1]
        print(rollno)
        temp = True
        if fclient[0] == 'MARK-ATTENDANCE':
            for i in datalist:
                if i == fclient[1]:
                    temp = False
                    question = datalist[i][0]
                    print(question)
                    conn.send(('SECRETQUESTION-'+ question).encode())
                    Thread(target = ser, args = (conn,datalist,rollno,question)).start()
                    break
        if temp:
                conn.send('ROLL NUMBER NOT FOUND'.encode())
                break

def ser(conn, datalist, roll, question):
    while True:
        fanswer = conn.recv(1024).decode()
        fanswer = fanswer.split('-')
        if fanswer[0] == 'SECRETANSWER':
            print(datalist[roll][1])
            if fanswer[1] == datalist[roll][1]:
                conn.send('ATTENDANCE SUCCESS'.encode())
            else:
                conn.send('ATTENDANCE FAILURE'.encode())
    conn.close()


if __name__ == '__main__':
    Main()