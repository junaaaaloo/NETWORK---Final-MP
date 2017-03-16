import socket
import threading
from uno_model import *

server = ('127.0.0.1', 5000)

host = '127.0.0.1'
port = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

tlock = threading.Lock()
shutdown = False

def receving (name, sock):
    while not shutdown:
        try:
            tlock.acquire()
            while True:
                data, addr = sock.recvfrom(4096)
                print(str(data))
        except:
            pass
        finally:
            tlock.release()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

setNames = False
while not setNames:
    alias = input("Name: ")
    if alias != '':
        print ("Sent name data!")
        data = alias
        data = data.encode('ascii')
        s.sendto(data, server)
        setNames = True

waiting = True
while waiting:
    try:
        msg = s.recvfrom(4096)
        print(msg.decode('ascii'))
        waiting = False
    except:
        pass

gameOver = 'Y'
while gameOver == 'Y':
    try:
        data, addr = s.recvfrom(1024)
        gameOver = data.decode('ascii')
    except Exception as e:
        pass

print("Finished")
s.close()

