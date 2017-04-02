from tkinter import *
import socket
from uno_model import *

class Main (Tk):
    def initializeCards(self):
        first = PhotoImage(file = "../cards/red 0.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.buttonContent.append("0")
        self.listCards.append(first)
        sec = PhotoImage(file ="../cards/red 1.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.buttonContent.append("1")
        self.listCards.append(sec)
        third = PhotoImage(file = "../cards/blue 0.jpg").subsample(2,2)
        self.buttonColors.append("blue")
        self.buttonContent.append("0")
        self.listCards.append(third)
        fourth = PhotoImage(file = "../cards/wild draw four cards.jpg").subsample(2,2)
        self.buttonColors.append("black")
        self.buttonContent.append("")
        self.listCards.append(fourth)
        fifth = PhotoImage(file = "../cards/green 7.jpg").subsample(2,2)
        self.buttonColors.append("green")
        self.buttonContent.append("7")
        self.listCards.append(fifth)
        sixth = PhotoImage(file = "../cards/yellow skip.jpg").subsample(2,2)
        self.buttonColors.append("yellow")
        self.buttonContent.append("skip")
        self.listCards.append(sixth)
        seven = PhotoImage(file = "../cards/green draw two cards.jpg").subsample(2,2)
        self.buttonColors.append("green")
        self.buttonContent.append("d2")
        self.listCards.append(seven)
        e = PhotoImage(file = "../cards/blue skip.jpg").subsample(2,2)
        self.buttonColors.append("blue")
        self.buttonContent.append("skip")
        self.listCards.append(e)
        s = PhotoImage(file = "../cards/red draw two cards.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.buttonContent.append("d2")
        self.listCards.append(s)

    def destroyCard(self, button, newCard, color, con):
        if(self.colorLabel.cget("text") == color or color == "black" or self.conLabel.cget("text") == con):
            self.currCard.configure(image = newCard)
            self.colorLabel.configure(text = ""+color)
            self.conLabel.configure(text = ""+con)
            button.destroy()
            if(color == "black"):
                self.redButton.configure(state = NORMAL)
                self.blueButton.configure(state = NORMAL)
                self.greenButton.configure(state = NORMAL)
                self.yellowButton.configure(state = NORMAL)



    def populate(self): 
        x = 0
        while x != 9:
            self.buttonCards.append(Button(self.cardsFrame, image = self.listCards[x]))
            self.buttonCards[x].configure(command = lambda button = self.buttonCards[x], newCard = self.listCards[x], 
                color = self.buttonColors[x], con = self.buttonContent[x]: self.destroyCard(button, newCard, color,con))
            self.buttonCards[x].grid(row = 0, column = x)
            x += 1

    def onFrameConfigure(self):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(ALL))

    def changeColor(self,col):
        self.colorLabel.configure(text = col)
        self.redButton.configure(state = DISABLED)
        self.blueButton.configure(state = DISABLED)
        self.greenButton.configure(state = DISABLED)
        self.yellowButton.configure(state = DISABLED)

    def packOthers(self):
        self.currCardFrame.pack(fill = "both")
        self.cardsFrame.pack(fill = "both")
        self.optionsFrame.pack(fill = "both")
        self.currCard.pack(side = "left",fill = "both")
        self.colorLabel.pack(side = "left", fill = "both")
        self.conLabel.pack(side = "left", fill = "both")
        self.redButton.pack(side = "left")
        self.blueButton.pack(side = "left")
        self.greenButton.pack(side = "left")
        self.yellowButton.pack(side = "left")


    def enterName(self):
        setNames = False
        if self.nameEntry.get() != '':
            self.packOthers()
            data = self.nameEntry.get()
            data = data.encode('ascii')
            self.s.sendto(data, self.server)
            setNames = True

    def gameProcess(self):
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

    def __init__ (self):
        Tk.__init__(self)
        self.listCards = []
        self.buttonCards = []
        self.buttonColors = []
        self.buttonContent = []
        self.title("Kwatro!")
        self.geometry("945x600+300+0")
        self.canvas = Canvas(self, borderwidth=0, background="#000000")
        self.mainFrame = Frame(self.canvas, background="#fff123")
        self.currCardFrame = Frame(self.mainFrame,background="#000000")
        self.cardsFrame = Frame(self.mainFrame,background = "#000000")
        self.optionsFrame = Frame(self.mainFrame, background = "#ffffff")
        self.nameFrame = Frame(self.mainFrame, background = "#ffffff")

        self.vsb = Scrollbar(self.mainFrame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.vsb.set)
        self.canvas.create_window((1,1), window=self.mainFrame,anchor = "nw")

        self.image1 = PhotoImage(file = "../cards/green 9.jpg")
        self.image1 = self.image1.subsample(2,2)
        self.currCard = Label(self.currCardFrame, image = self.image1, background = "#000000", width = 945)

        self.colorLabel = Label(self.optionsFrame, text = "green",font = ("courier",30),background = "#ffffff")
        self.conLabel = Label(self.optionsFrame, text = "9",font = ("courier",30),background = "#ffffff")
        self.red = PhotoImage(file = "../cards/red plain.gif").subsample(2,2)
        self.redButton = Button(self.optionsFrame, image = self.red, command = lambda col = "red": self.changeColor(col), state = DISABLED)
        self.blue = PhotoImage(file = "../cards/blue plain.gif").subsample(2,2)
        self.blueButton = Button(self.optionsFrame, image = self.blue, command = lambda col = "blue": self.changeColor(col), state = DISABLED)   
        self.green = PhotoImage(file = "../cards/green plain.gif").subsample(2,2)
        self.greenButton = Button(self.optionsFrame, image = self.green, command = lambda col = "green": self.changeColor(col), state = DISABLED)
        self.yellow = PhotoImage(file = "../cards/yellow plain.gif").subsample(2,2)
        self.yellowButton = Button(self.optionsFrame, image = self.yellow, command = lambda col = "yellow":self.changeColor(col), state = DISABLED)

        self.nameLabel = Label(self.nameFrame, text = "Name:",font = ("courier",30),background = "#ffffff")
        self.nameEntry = Entry(self.nameFrame, font = ("courier",30), bg = "#000000", foreground = "#ffffff", width = 10)
        self.nameButton = Button(self.nameFrame, text = "Enter", font = ("courier",20), command = self.enterName)

        self.vsb.pack(side="bottom", fill="x")
        self.nameFrame.pack(fill = "both")
        self.canvas.pack(side="top", fill="both",expand = True)
        self.nameLabel.pack(side = "left")
        self.nameEntry.pack(side = "left")
        self.nameButton.pack(side = "left")

        #self.initializeCards()
        #self.populate()

        self.server = ('127.0.0.1', 5000)

        self.host = '127.0.0.1'
        self.port = 0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))
        self.s.setblocking(0)

        self.cardsFrame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure())


main = Main()    
main.mainloop()
