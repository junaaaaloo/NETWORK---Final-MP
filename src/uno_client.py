import socket
from uno_model import *

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
        print ("Sent name data!")
        data = alias
        data = data.encode('ascii')
        s.sendto(data, server)
        setNames = True

waiting = True
while waiting:
    try:
        msg, addr = s.recvfrom(4096)
        msg = msg.decode('ascii')
        print(msg)
        waiting = False
    except:
        pass

game = True
while game:
    try:
        data, addr = s.recvfrom(4096)
        gameOver = data.decode('ascii')

        if gameOver == "input":
            sending = True
            while sending:
                try:
                    gameOver = input("Card -> ")
                    gameOver = gameOver.encode()
                    s.sendto(gameOver, server)
                    sending = False
                except Exception as e:
                    print(e)
                    pass
        elif gameOver == "color":
            j = 1
            print("\nColors: ")
            for color in normal_cards.colors:
                print(j, " ", color)
                j += 1
            sending = True
            while sending:
                try:
                    col = input("Color -> ")
                    col = col.encode()
                    s.sendto(col, server)
                    sending = False
                except Exception as e:
                    print(e)
                    pass
        elif gameOver == "quit":
            game = False
        elif gameOver == "continue":
            pass
        else:
            print("")
            print(gameOver)
            print("")
    except Exception:
        pass

s.close()

