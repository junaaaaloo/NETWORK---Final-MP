import random

class player_queue:
    def __init__ (self):
        self.players = list()

    def insert(self, player):
        self.players.insert(0, player)

    def next_player (self):
        return self.players[1]

    def curr_player(self):
        return self.players[0]

    def dequeue(self):
        player = self.players.pop(0)
        self.players.append(player)

    def reverse (self):
        self.players = list(reversed(self.players))

class special_cards:
    def drawTwo(players, deck):
        draw = 2

        while players.next_player().withPlusTwo():
            draw += 2
            print("CHAIN Draw ", draw)
            for card in players.next_player().cards:
                if(hasattr(card, "effect")):
                    if (card.effect == "d2"):
                        players.next_player().cards.remove(card)
            players.dequeue()

        print(players.next_player().name, " drawing ", draw, " cards!")
        while draw != 0:
            players.next_player().draw(deck.pop())
            draw -= 1

    def drawFour(players, deck, game):
        draw = 4

        while players.next_player().withPlusFour():
            draw += 4
            print("CHAIN Draw ", draw)
            for card in players.next_player().cards:
                if (hasattr(card, "effect")):
                    if (card.effect == "d4"):
                        players.next_player().cards.remove(card)
            players.dequeue()

        j = 1

        for color in normal_cards.colors:
            print(j, " ", color)
            j += 1

        col = input("Pick a color: ")
        col = int(col) - 1

        special_cards.choose_color(game, normal_cards.colors[col])
        print(players.next_player().name, " drawing ", draw, " cards!")
        print("CHOSEN COLOR: ", normal_cards.colors[col])
        while draw != 0:
            players.next_player().draw(deck.pop())
            draw -= 1

    def reverse (players):
        players.reverse()

    def skip (players):
        players.dequeue()

    def choose_color(game, chosen_color):
        game.card_q.queue[0].color = chosen_color

    effects = {"d2": drawTwo,
               "d4": drawFour,
               "rev": reverse,
               "skip": skip,
               "color": choose_color}

    def __init__ (self, effect, color):
        self.effect = effect
        self.color = color

    def __str__ (self):
        if self.effect == "d2":
            return self.color + " Draw two cards"
        elif self.effect == "d4":
            return "WILD Draw four cards"
        elif self.effect == "rev":
            return self.color + " Reverse"
        elif self.effect == "skip":
            return self.color + " Skip"
        elif self.effect == "color":
            return "WILD Choose color"

    def applyEffect (self, chosen, game):
        if self.effect == "d2":
            special_cards.drawTwo(game.players, game.deck)
        elif self.effect == "d4":
            special_cards.choose_color(game, chosen)
            special_cards.drawFour(game.players, game.deck, game)
        elif self.effect == "rev":
            special_cards.reverse(game.players)
        elif self.effect == "skip":
            special_cards.skip(game.players)
        elif self.effect == "color":
            special_cards.choose_color(game, chosen)

    def compare (self, other):
        if(hasattr(other, "number")):
            if (other.color == self.color):
                return True
        else:
            if (other.color == "BLACK"):
                return True
            elif(other.color == self.color):
                return True
            elif (other.effect == self.effect):
                return True
        return False

class normal_cards:
    colors = ["BLUE", "RED", "GREEN", "YELLOW"]
    wild = "BLACK"
    numbers = range(0, 10)

    def __init__ (self, number, color):
        self.number = number
        self.color = color

    def compare(self, other):
        if(hasattr(other, 'effect')):
            if(other.color == "BLACK"):
                return True
            elif(other.color == self.color):
                return True
        else:
            if(other.color == self.color):
                return True
            elif (other.number == self.number):
                return True
        return False

    def __str__ (self):
        return self.color + " " + str(self.number)

class deck:
    def __init__ (self):
        self.cards = list()

        for i in normal_cards.colors:
            for j in normal_cards.numbers:
                self.cards.append(normal_cards(j, i))
            for j in normal_cards.numbers:
                if (j != 0):
                    self.cards.append(normal_cards(j, i))

            self.cards.append(special_cards("d2", i))
            self.cards.append(special_cards("d2", i))
            self.cards.append(special_cards("skip", i))
            self.cards.append(special_cards("skip", i))
            self.cards.append(special_cards("rev", i))
            self.cards.append(special_cards("rev", i))

        self.cards.append(special_cards("d4", normal_cards.wild))
        self.cards.append(special_cards("d4", normal_cards.wild))
        self.cards.append(special_cards("d4", normal_cards.wild))
        self.cards.append(special_cards("d4", normal_cards.wild))
        self.cards.append(special_cards("d4", normal_cards.wild))
        self.cards.append(special_cards("color", normal_cards.wild))
        self.cards.append(special_cards("color", normal_cards.wild))
        self.cards.append(special_cards("color", normal_cards.wild))
        self.cards.append(special_cards("color", normal_cards.wild))
        self.cards.append(special_cards("color", normal_cards.wild))

        self.shuffle()

    def shuffle (self):
        random.shuffle(self.cards)

    def pop (self):
        return self.cards.pop(0)

    def push (self, list):
        self.cards.extend(list)

    def size (self):
        return len(self.cards)

    def __str__(self):
        msg = "Deck: " + str(len(self.cards)) + "/108\n"
        for card in self.cards:
            msg += card.__str__() + "\n"
        return msg

class card_queue:
    def __init__ (self):
        self.queue = []

    def push (self, card):
        self.queue.insert(0, card)

    def returnToDeck (self, card, deck):
        if(deck.size() == 0):
            returnTo = self.queue[1:len(self.queue)]
            deck.push(card)

    def compareTop (self, card):
        return self.queue[0].compare(card)

class user:
    def __init__(self, cards, name):
        self.cards = cards
        self.name = name
        self.uno = False
        self.win = False

    def withPlusTwo (self):
        for card in self.cards:
            if hasattr(card, "effect"):
                if card.effect == "d2":
                    return True
        return False

    def withPlusFour (self):
        for card in self.cards:
            if hasattr(card, "effect"):
                if card.effect == "d4":
                    return True
        return False

    def noPlayableCard (self, cardQ):
        for card in self.cards:
            if cardQ.compareTop(card):
                return False
        return True

    def unoQ (self):
        return len(self.cards) == 1

    def callUno (self):
        if (self.unoQ()):
            self.uno = True

    def init_draw (self, deck):
        i = 0

        while i != 7:
            self.cards.append(deck.pop())
            i += 1

    def draw (self, card):
        self.cards.append(card)

    def makeUno (self, player, deck):
        if (player.uno() and not player.uno):
            special_cards.drawTwo(player, deck)

    def playCard (self, cards, i, game):
        if(self.win):
            return True
        if cards.compareTop (self.cards[i]):
            if len(cards.queue) == 0:
                self.win = True
                game.players.players.remove(self)

            cards.push(self.cards.pop(i))

            if(isinstance(cards.queue[0], special_cards)):
                if(cards.queue[0].effect == "color" or cards.queue[0].effect == "d4"):
                    j = 1

                    for color in normal_cards.colors:
                        print(j, " ",color)
                        j += 1

                    col = input ("Pick a color: ")
                    col = int(col) - 1

                    cards.queue[0].applyEffect(normal_cards.colors[col], game)
                    print("CHOSEN COLOR: ", normal_cards.colors[col])
                else:
                    cards.queue[0].applyEffect(None, game)
            return True
        else:
            return False

class game:
    def __init__ (self, names):
        self.deck = deck()
        self.players = player_queue()
        self.card_q = card_queue()
        self.winners = list()

        for name in names:
            self.players.insert(user(list(), name))

    def console_start (self):
        for player in self.players.players:
            player.init_draw(self.deck)

        print("UNO Game is starting!")

        gameOver = False
        random.shuffle(self.players.players)

        self.card_q.push(self.deck.pop())

        print ("Users in game: ")
        i = 1

        for player in self.players.players:
            print(i, " ", player.name)
            i += 1

        while not gameOver:
            print("\nUSER: ", self.players.curr_player().name)
            finish = False

            print("Current Card: ", self.card_q.queue[0])
            print("Cards: ")

            i = 1
            for card in self.players.curr_player().cards:
                print(i, " ", card)
                i += 1

            if self.players.curr_player().noPlayableCard(self.card_q):
                card = self.deck.pop()
                print("No playable card! Drawing a card")
                print("Draw a ", card)
                self.players.curr_player().draw(card)
                if self.players.curr_player().noPlayableCard(self.card_q):
                    print("PASS! Still no playable card")
                else:
                    print("SUCCESS! played a card!")
                    self.players.curr_player().playCard(self.card_q, len(self.players.curr_player().cards) - 1, game)

            else:
                while not finish:
                    opt = input("Pick a card: ")

                    opt = int(opt) - 1
                    card = self.players.curr_player().cards[0]
                    finish = (self.players.curr_player().playCard(self.card_q, opt, game))

                    if finish:
                        print("Next player!")

            if hasattr(card, "effect"):
                if card.effect != "rev":
                    self.players.dequeue()
            else:
                self.players.dequeue()

            for player in self.players.players:
                if player.unoQ() and not player.uno:
                    print(player.name + " UNO!")

            for player in self.players.players:
                if len(player.cards) == 0:
                    print(player.name+ " has won!")
                    self.winners.append(player)
                    self.players.players.remove(player)

            if len(self.players.players) == 1:
                gameOver = True
            i = 1

        self.winners.append(self.players.players[0])

        print("Ranking: ")
        for player in self.winners:
            print(i, " ", player.name)
            i += 1

names = ["Mary", "John", "Moana"]
game = game(names)
game.console_start()