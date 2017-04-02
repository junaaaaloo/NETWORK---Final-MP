from tkinter import *
import socket
from uno_model import *

class Main (Tk):
    def initializeCards(self, cards):
        for i in cards:
            try:
                name = i.lower()
                print(name)
                path = "../cards/" + name + ".jpg"
                c = PhotoImage(file = path).subsample(2,2)
                self.buttonColors.append(name.split(" ")[0])
                self.buttonContent.append(name.split(" ")[1])
                self.listCards.append(c)
            except:
                pass
        self.populate(len(self.listCards))

    def destroyCard(self, button, newCard, color, con, ind):
        if(self.colorLabel.cget("text") == color or color == "wild" or self.conLabel.cget("text") == con):
            self.currCard.configure(image = newCard)
            self.colorLabel.configure(text = ""+color)
            self.conLabel.configure(text = ""+con)
            
            if(color != "wild"):
                sending = True
                while sending:
                    try:
                        sendCard = str(ind)
                        print(sendCard)
                        sendCard = sendCard.encode()
                        self.s.sendto(sendCard, self.server)
                        sending = False
                    except Exception as e:
                        sending = False
                        print(e)
                        pass
            button.destroy()

    def populate(self, cnt): 
        x = 0
        while x != cnt:
            self.buttonCards.append(Button(self.cardsFrame, image = self.listCards[x]))
            self.buttonCards[x].configure(command = lambda button = self.buttonCards[x], newCard = self.listCards[x], 
                color = self.buttonColors[x], con = self.buttonContent[x], ind = x: 
                self.destroyCard(button, newCard, color,con, ind))
            self.buttonCards[x].grid(row = 0, column = x)
            x += 1

    def onFrameConfigure(self):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(ALL))

    def changeColor(self,col, num):
        self.colorLabel.configure(text = col)
        self.redButton.configure(state = DISABLED)
        self.blueButton.configure(state = DISABLED)
        self.greenButton.configure(state = DISABLED)
        self.yellowButton.configure(state = DISABLED)
        sending = True
        while sending:
            try:
                sendCol = num
                sendCol = sendCol.encode()
                self.s.sendto(sendCol, self.server)
                sending = False
            except:
                pass

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

    def disableCards(self):
        x = 0
        while x != len(self.buttonCards):
            self.buttonCards[x].configure(state = DISABLED)
            x += 1

    def enterName(self):
        setNames = False
        if self.nameEntry.get() != '':
            #self.packOthers()
            data = self.nameEntry.get()
            data = data.encode('ascii')
            self.s.sendto(data, self.server)
            setNames = True
        self.wait()
        

    def wait(self):
        waiting = True
        while waiting:
            try:
                numQ, addr = self.s.recvfrom(4096)
                numQ = numQ.decode('ascii')
                waiting = False
                print(numQ)
            except:
                pass
        self.getCards()
        self.gameStart()

    def getCards(self):
        waiting = True
        while waiting:
            try:
                msg, addr = self.s.recvfrom(4096)
                msg = msg.decode('ascii')
                cards = msg.split("\n")
                waiting = False
                self.listCards = []
                self.buttonCards = []
                self.buttonColors = []
                self.buttonContent = []
                self.initializeCards(cards)
            except:
                pass
        
    def gameStart(self):
        game = True
        while game:
            try:
                currCard, addr = self.s.recvfrom(4096)
                currCard = currCard.decode('ascii')
                currPlayer, addr = self.s.recvfrom(4096)
                currPlayer = currPlayer.decode('ascii')
                self.updateCurr(currCard)
                if self.nameEntry.get() == currPlayer:
                    self.getCards()
                    try:
                        data, addr = s.recvfrom(4096)
                        data = data.decode('ascii')
                        if data == "color":
                            self.redButton.configure(state = NORMAL)
                            self.blueButton.configure(state = NORMAL)
                            self.greenButton.configure(state = NORMAL)
                            self.yellowButton.configure(state = NORMAL)
                        elif data == "quit":
                            game = False
                        elif data == "continue":
                            pass
                    except:
                        pass
                else:
                    self.disableCards()
                game = False
                
            except:
                pass

    def updateCurr(self, c):
        c = c.lower()
        path = "../cards/" + c + ".jpg"
        self.image1 = PhotoImage(file = path)
        self.image1 = self.image1.subsample(2,2)
        self.currCard = Label(self.currCardFrame, image = self.image1, background = "#000000", width = 945)
        self.colorLabel = Label(self.optionsFrame, text = c.split(" ")[0], font = ("courier",30),background = "#ffffff")
        self.conLabel = Label(self.optionsFrame, text = c.split(" ")[1] ,font = ("courier",30),background = "#ffffff")
        self.packOthers()

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

        #self.image1 = PhotoImage(file = "../cards/green 9.jpg")
       # self.image1 = self.image1.subsample(2,2)
        #self.currCard = Label(self.currCardFrame, image = self.image1, background = "#000000", width = 945)

       # self.colorLabel = Label(self.optionsFrame, text = "green",font = ("courier",30),background = "#ffffff")
        #self.conLabel = Label(self.optionsFrame, text = "9",font = ("courier",30),background = "#ffffff")
        
        self.red = PhotoImage(file = "../cards/red plain.gif").subsample(2,2)
        self.redButton = Button(self.optionsFrame, image = self.red, command = lambda col = "red", num  = 2: self.changeColor(col, num), state = DISABLED)
        self.blue = PhotoImage(file = "../cards/blue plain.gif").subsample(2,2)
        self.blueButton = Button(self.optionsFrame, image = self.blue, command = lambda col = "blue", num  = 1: self.changeColor(col, num), state = DISABLED)   
        self.green = PhotoImage(file = "../cards/green plain.gif").subsample(2,2)
        self.greenButton = Button(self.optionsFrame, image = self.green, command = lambda col = "green", num  = 3: self.changeColor(col, num), state = DISABLED)
        self.yellow = PhotoImage(file = "../cards/yellow plain.gif").subsample(2,2)
        self.yellowButton = Button(self.optionsFrame, image = self.yellow, command = lambda col = "yellow", num  = 4:self.changeColor(col, num), state = DISABLED)

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

        self.server = ('127.0.0.1',5002)

        self.host = '127.0.0.1'
        self.port = 0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))
        self.s.setblocking(0)

        '''y = 0
        while y != 10:
            self.gameStart()
            y += 1'''

        self.cardsFrame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure())


main = Main()    
main.mainloop()
