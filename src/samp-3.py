from tkinter import *

class Main (Tk):
    def initializeCards(self):
        first = PhotoImage(file = "../res/cards/red_0.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.listCards.append(first)
        sec = PhotoImage(file ="../res/cards/red_1.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.listCards.append(sec)
        third = PhotoImage(file = "../res/cards/blue_0.jpg").subsample(2,2)
        self.buttonColors.append("blue")
        self.listCards.append(third)
        fourth = PhotoImage(file = "../res/cards/wild_draw_four_cards.jpg").subsample(2,2)
        self.buttonColors.append("black")
        self.listCards.append(fourth)
        fifth = PhotoImage(file = "../res/cards/green_7.jpg").subsample(2,2)
        self.buttonColors.append("green")
        self.listCards.append(fifth)
        sixth = PhotoImage(file = "../res/cards/yellow_skip.jpg").subsample(2,2)
        self.buttonColors.append("yellow")
        self.listCards.append(sixth)
        seven = PhotoImage(file = "../res/cards/green_draw_two_cards.jpg").subsample(2,2)
        self.buttonColors.append("green")
        self.listCards.append(seven)
        e = PhotoImage(file = "../res/cards/blue_skip.jpg").subsample(2,2)
        self.buttonColors.append("blue")
        self.listCards.append(e)
        s = PhotoImage(file = "../res/cards/red_draw_two_cards.jpg").subsample(2,2)
        self.buttonColors.append("red")
        self.listCards.append(s)

    def destroyCard(self, button, newCard, color):
        if(self.colorLabel.cget("text") == color or color == "black"):
            self.currCard.configure(image = newCard)
            self.colorLabel.configure(text = ""+color)
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
            self.buttonCards[x].configure(command = lambda button = self.buttonCards[x], newCard = self.listCards[x], color = self.buttonColors[x]: self.destroyCard(button, newCard, color))
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



    def __init__ (self):
        Tk.__init__(self)
        self.listCards = []
        self.buttonCards = []
        self.buttonColors = []
        self.title("Kwatro!")
        self.geometry("945x600+300+0")
        self.canvas = Canvas(self, borderwidth=0, background="#000000")
        self.mainFrame = Frame(self.canvas, background="#fff123")
        self.currCardFrame = Frame(self.mainFrame,background="#000000")
        self.cardsFrame = Frame(self.mainFrame,background = "#000000")
        self.optionsFrame = Frame(self.mainFrame, background = "#ffffff")

        self.vsb = Scrollbar(self.mainFrame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.vsb.set)
        self.canvas.create_window((1,1), window=self.mainFrame,anchor = "nw")

        self.image1 = PhotoImage(file = "../res/cards/green_9.jpg")
        self.image1 = self.image1.subsample(2,2)
        self.currCard = Label(self.currCardFrame, image = self.image1, background = "#000000", width = 945)

        self.colorLabel = Label(self.optionsFrame, text = "green",font = ("courier",30),background = "#ffffff")
        self.red = PhotoImage(file = "../res/red_plain.gif")
        self.redButton = Button(self.optionsFrame, image = self.red, command = lambda col = "red": self.changeColor(col), state = DISABLED)
        self.blue = PhotoImage(file = "../res/blue_plain.gif")
        self.blueButton = Button(self.optionsFrame, image = self.blue, command = lambda col = "blue": self.changeColor(col), state = DISABLED)   
        self.green = PhotoImage(file = "../res/green_plain.gif")
        self.greenButton = Button(self.optionsFrame, image = self.green, command = lambda col = "green": self.changeColor(col), state = DISABLED)
        self.yellow = PhotoImage(file = "../res/yellow_plain.gif")
        self.yellowButton = Button(self.optionsFrame, image = self.yellow, command = lambda col = "yellow":self.changeColor(col), state = DISABLED)

        self.vsb.pack(side="bottom", fill="x")
        self.currCardFrame.pack(fill = "both")
        self.cardsFrame.pack(fill = "both")
        self.optionsFrame.pack(fill = "both")
        self.canvas.pack(side="top", fill="both",expand = True)
        self.currCard.pack(side = "left",fill = "both")
        self.colorLabel.pack(side = "left", fill = "both")
        self.redButton.pack(side = "left")
        self.blueButton.pack(side = "left")
        self.greenButton.pack(side = "left")
        self.yellowButton.pack(side = "left")

        self.initializeCards()
        self.populate()

        self.cardsFrame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure())


main = Main()    
main.mainloop()
