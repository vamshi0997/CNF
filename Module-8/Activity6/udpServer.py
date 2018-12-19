import socket

def Main():
        host = '127.0.0.1'
        port = 5000

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host, port))

        print ("Server Server Started..")
        while True:
                data, addr = s.recvfrom(1024)
                print ("message from: " + str(addr))
                print ("from connect user: " + data.decode())
                data = data.decode().upper()
                print ("sending: " + data)
                s.sendto(data.encode(), addr)
        s.close()

if __name__ == '__main__':
        Main()
