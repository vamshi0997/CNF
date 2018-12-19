import socket

def Main():
        host = '127.0.0.1'
        port = 5000
        
        currency = {'Dollar_INR': 67, 'INR_Dollar': 0.0149,
                    'Dollar_Pounds': 0.75, 'Pounds_Dollar': 1.3333,
                    'Dollar_Yen': 113.41, 'Yen_Dollar' : 0.0088 }

        s = socket.socket()
        s.bind((host, port))
        
        s.listen(1)
        c, addr = s.accept()
        print ("Connection from:" + str(addr))

        while True:
                data = c.recv(1024)
                if not data:
                        break
                print ("from connected user:" + data.decode())
                data = data.decode()
                data = data.split(" ")
                result = 0;
                result += int(data[2]) * (currency[data[1]+ "_" + data[4]])
                result = str(round(result,1)).encode()
                c.send(result)
        c.close()

if __name__ == '__main__':
        Main()

