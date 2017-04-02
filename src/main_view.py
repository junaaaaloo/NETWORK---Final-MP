import tkinter
from tkinter import *
from uno_model import *

class Main (Tk):
    def __init__ (self):
        Tk.__init__(self)
        self.title("KWATRO!")
        self.geometry("945x600+300+0")
        self.resizable(0, 0)
        self.board = Board(self)
        self.board.pack()
        self.players = []

    def initializePlayerFrames (self, players):
        currPlayer = players.curr_player()

        self.players.append(Player(self.board, currPlayer, BOTTOM))
        players.dequeue()

        if(currPlayer != players.curr_player()):
            self.players.append(Player(self.board, players.curr_player(), LEFT))
            players.dequeue()

        if (currPlayer != players.curr_player()):
            self.players.append(Player(self.board, players.curr_player(), TOP))
            players.dequeue()

        if (currPlayer != players.curr_player()):
            self.players.append(Player(self.board, players.curr_player(), RIGHT))
            players.dequeue()

class Board (PanedWindow):
    def __init__ (self, frame):
        PanedWindow.__init__(self, frame)
        self.bgImage = PhotoImage(file = "../res/bg.png")
        self.bg = Label(frame, image = self.bgImage)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

class Player (Frame):
    def __init__ (self, window, player, orientation):
        Frame.__init__(self, window)
        self.nameLabel = Label(text = player.name, font = "Verdana 16 bold")
        self.nameLabel.pack()
        self.buttonCards = []
        self.canvas = Canvas(window)
        self.canvas.pack(side = orientation)
        self.player = player
        self.scrollbar = Scrollbar(window, command= self.canvas.xview)
        self.scrollbar.pack(side = LEFT, fill = 'y')
        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        self.canvas.bind('<Configure>', self.on_configure)

    def on_configure(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))

    def setCards (self, cards):
        pass

names = ["Jones", "Angel", "Jam"]
players = player_queue()

for name in names:
    players.insert(user(list(), name))

main = Main()
main.initializePlayerFrames(players)
main.mainloop()