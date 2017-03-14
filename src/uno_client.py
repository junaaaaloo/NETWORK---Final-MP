import socket
import threading
import time

tlock = threading.Lock()
shutdown = False


def receving(name, sock):
    while not shutdown:
        try:
            tlock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data.decode('ascii')))
        except:
            pass
        finally:
            tlock.release()


host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

setNames = False
while not setNames:
    alias = input("Name: ")
    if alias != '':
        data = alias
        data = data.encode('ascii')
        s.sendto(data, server)
        setNames = True


waiting = True

while waiting:
    if(data.decode('ascii') != "Complete"):
        waiting = False



s.close()

