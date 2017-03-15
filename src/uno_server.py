import socket
import time
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


i = 0
for player in player_addresses:
    print(i, player, namesList[i - 1])
    i += 1

for i in player_addresses:
    print(i)

s.close()

