import socket

server = ('127.0.0.1', 5000)

host = '127.0.0.1'
port = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

setNames = False
while not setNames:
    alias = input("Name: ")
    if alias != '':
        print ("Got connection!")
        data = alias
        data = data.encode('ascii')
        s.sendto(data, server)
        setNames = True


waiting = True

while waiting:
    try:
        s.recvfrom(1024)
        if (data.decode('ascii') != "Complete"):
            waiting = False
        print("Got game data!")
    except:
        pass

print("Game should start here!")

s.close()

