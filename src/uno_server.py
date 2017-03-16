import socket
import time
import random
from uno_model import *

host = '127.0.0.1'
port = 5000

players = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

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
            namesList.insert(0, data.decode('ascii'))
            print(time.ctime(time.time()), "-", namesList[0]," connected! Current players:", len(player_addresses))
        if len(player_addresses) >= 2:
            print("Complete!")
            print("Accept more players?")
            opt = input("(Y/N): ")
            if opt != "Y":
                names = True
    except:
        pass

data = 'Y'
data = data.encode('ascii')

i = 1
print("PLAYERS: ")
for player in player_addresses:
    print(i, " ", player, " ", namesList[i - 1])
    s.sendto(data, player)
    i += 1

deck = deck()
player_queue = player_queue()
card_queue = card_queue()
winners = []

i = 0
for name in namesList:
    player = user(list(), name)
    player.address = player_addresses[i]
    player_queue.insert(player)
    i += 1

i = 1
msg = "";
random.shuffle(player_queue.players)
for player in player_queue.players:
    player.init_draw(deck)
    msg += str(i) + " " + player.name + "\n"
    i += 1

print("")
print(msg)
print("")

msg = msg.encode('ascii')

for player in player_queue.players:
    s.sendto(msg, player.address)


gameOver = False
while not gameOver:
    opt = input("Input to continue game (Y/N): ")
    data = opt.encode('ascii')

    if opt != "Y":
        gameOver = True

    for player in player_addresses:
        s.sendto(data, player)
s.close()

