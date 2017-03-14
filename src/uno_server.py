import socket
import time
from uno_model import *

host = '127.0.0.1'
port = 5000

players = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

deck = deck()
players = player_queue()
card_q = card_queue()
winners = list()
player_addresses = []
names = False
namesList = []
print("UNO Server Started")
print("Waiting for player(s)")

while not names:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in player_addresses:
            player_addresses.append(addr)
            namesList.append(data.decode())
        if len(player_addresses) >= 2:
            print("Complete!")
            print("Accept more players?")
            opt = input("(Y/N): ")
            if opt != "Y":
                names = True

            i = 1
            for player in player_addresses:
                print(i, player, namesList[i - 1])
                i += 1

        print("Waiting for more player(s)")
    except:
        pass

for i in player_addresses:
    print(i)

s.close()

