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
            player_addresses.insert(0, addr)
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
msg = ""

random.shuffle(player_queue.players)

for player in player_queue.players:
    player.init_draw(deck)
    msg = "# IN QUEUE: " + str(i)
    msg = msg.encode('ascii')
    s.sendto(msg, player.address)
    i += 1

print("UNO Game is starting!")

card_queue.push(deck.pop())
gameOver = False
while not gameOver:
    print("\nUSER: ", player_queue.curr_player().name)

    msg = "CURRENT CARD: " + str(card_queue.queue[0]) + "\n"

    for player in player_queue.players:
        if (player.name == player_queue.curr_player().name):
            i = 1
            for card in player_queue.curr_player().cards:
                msg += str(i) + " " + str(card) + "\n"
                i += 1

            msg = msg.encode('ascii')
            s.sendto(msg, player.address)

        else:
            msg = player_queue.curr_player().name + "'S TURN"
            msg = msg.encode('ascii')
            s.sendto(msg, player.address)

    if player_queue.curr_player().noPlayableCard(card_queue):
        card = deck.pop()
        noPlayable = "No playable card! Drawing a card: " + str(card)
        print(player_queue.curr_player().name, ":", noPlayable)
        noPlayable = noPlayable.encode('ascii')
        s.sendto(noPlayable, player_queue.curr_player().address)
        player_queue.curr_player().draw(card)

        if player_queue.curr_player().noPlayableCard(card_queue):
            noPlayable = "PASS! Still no playable card"
            noPlayable = noPlayable.encode('ascii')
            s.sendto(noPlayable, player_queue.curr_player().address)
        else:
            msg = "SUCCESS! played a card!"
            msg = msg.encode('ascii')
            s.sendto(msg, player_queue.curr_player().address)
            if (isinstance(card_queue.queue[0], special_cards)):
                if (card_queue.queue[0].effect == "color"):
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    receiving = True
                    while receiving:
                        try:
                            color, addr = s.recvfrom(4096)
                            color = color.decode()
                            receiving = False
                        except:
                            pass
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, normal_cards[color], opt))
                elif (card_queue.queue[0].effect == "d4"):
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    receiving = True
                    while receiving:
                        color, addr = s.recvfrom(4096)
                        color = int(color)
                        receiving = False
                    if finish:
                        special_cards.choose_color(card_queue, normal_cards.colors[color])
                else:
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))
            else:
                finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))
    else:
        finish = False
        while not finish:
            receiving = True

            opt = "input"
            opt = opt.encode('ascii')

            s.sendto(opt, player_queue.curr_player().address)

            while receiving:
                try:
                    opt, addr = s.recvfrom(4096)
                    opt = opt.decode()
                    opt = int(opt) - 1
                    receiving = False
                except:
                    pass

            color = None

            if (isinstance(card_queue.queue[0], special_cards)):
                if (card_queue.queue[0].effect == "color"):
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    receiving = True
                    while receiving:
                        try:
                            color, addr = s.recvfrom(4096)
                            color = color.decode()
                            color = int(color)
                            receiving = False
                        except:
                            pass
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, normal_cards[color], opt))
                elif (card_queue.queue[0].effect == "d4"):
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))
                    mess = "color"
                    mess = mess.encode('ascii')
                    s.sendto(mess, player_queue.curr_player().address)
                    receiving = True
                    while receiving:
                        try:
                            color, addr = s.recvfrom(4096)
                            color = color.decode()
                            color = int(color)
                            receiving = False
                        except:
                            pass
                    if finish:
                        special_cards.choose_color(card_queue, normal_cards.colors[color])
                else:
                    finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))
            else:
                finish = (player_queue.curr_player().playCard(card_queue, player_queue, deck, None, opt))

            if finish:
                mess = "Next player!"
                mess = mess.encode('ascii')
                s.sendto(mess, player_queue.curr_player().address)

            print(str(card))
    if hasattr (card, "effect"):
        if card.effect != "rev":
            player_queue.dequeue()
    else:
        player_queue.dequeue()

    for player in player_queue.players:
        if player.unoQ() and not player.uno:
            msg = player.name + " UNO!"
            msg = msg.encode('ascii')
            s.sendto(msg, player.address)

    for player in player_queue.players:
        if len(player.cards) == 0:
            msg = player.name + " has won!"
            s.sendto(msg, player.address)
            player_queue.players.remove(player)
            winners.append(player)

    if len(player_queue.players) == 1:
        gameOver = True

    if gameOver:
        opt = 'N'
    else:
        opt = 'Y'

    opt = opt.encode('ascii')
    for player in player_queue.players:
        s.sendto(opt, player.address)

winners.append(player_queue.players[0])

print("Ranking:")

i = 1

for player in winners:
    print(i, " ", player.name)
    msg = "Your ranking: " + str(i)
    msg = msg.encode('ascii')
    s.sendto(msg, player.address)
    i += 1

s.close()

