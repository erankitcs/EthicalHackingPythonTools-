import socket

ip = "8.8.4.4"

for port in range(1, 100):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.close()
        print('%d/tcp' % port)
    except:
        pass