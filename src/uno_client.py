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

gameOver = 'Y'
while gameOver != 'N':
    try:
        data, addr = s.recvfrom(4096)
        gameOver = data.decode('ascii')

        if gameOver == "input":
            sending = True
            while sending:
                try:
                    gameOver = input("card -> ")
                    gameOver = gameOver.encode()
                    s.sendto(gameOver, server)
                    sending = False
                except Exception as e:
                    print(e)
                    pass
        elif gameOver == "color":

            j = 1
            for color in normal_cards.colors:
                print(j, " ", color)
                j += 1

            try:
                col = input("Pick a color: ")
                col = col.encode()
                s.sendto(col, server)
            except Exception as e:
                print(e)
                pass

        elif gameOver == "Y":
            pass
        elif gameOver == "N":
            pass
        else:
            print("")
            print(gameOver)
            print("")
    except Exception:
        pass

print("Finished")
s.close()

