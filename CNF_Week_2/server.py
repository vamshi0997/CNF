import socket
import csv
from threading import *

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host,port))
	s.listen(10)
	print('server started....')
	attlist = {}
	with open('attlist.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			attlist[row[0]] = [row[1],row[2]]
	personid = {}
	person = []

	while True:
		c, addr = s.accept()
		inpu = c.recv(1024).decode()
		data = inpu.split()
		roll = data[1]
		temp = 1
		if data[0] == 'MARK-ATTENDANCE':
			for key, value in attlist.items():
				if key == roll:
					temp = 0
					personid[c] = key
					print(key + ' -- Started PUZZLE')
					Thread(target = att, args = (attlist,c,personid,person)).start()
			if temp:
				c.send('ROLL NUMBER-NOT FOUND'.encode())
				check(person)
	s.close()
			
def check(person):
	if (active_count() == 2):
		print('WAIT TIME - 15 Seconds')
		time.sleep(15)
		if (active_count() == 2):
			print('Rollnumbers of Presented Students are: ')
			print(person)

def att(attlist, c, personid,person):
	lis = attlist[personid[c]]
	while True:

		c.send(('SECRETQUESTION-' + lis[0]).encode())
		user_ans = c.recv(1024).decode().split('-')

		if (user_ans[0] == 'SECRETANSWER'):
			if (user_ans[1] == lis[1]):
				person.append(personid[c])
				print(str(personid[c]) + ' -- Present')
				c.send('ATTENDANCE SUCCESS'.encode())
				check(person)
			else:
				c.send('ATTENDANCE FAILURE'.encode())
		else:
			c.send('Invalid Syntax'.encode())


if __name__ == '__main__':
	Main()