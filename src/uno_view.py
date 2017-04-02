from tkinter import *


class Main (Tk):
    def __init__ (self):
        Tk.__init__(self)
        #self.wm_iconbitmap("") #for icons
        self.title("KWATRO!")
        self.geometry("945x600+300+0")
        self.resizable(0, 0)
        
        frame2 = Frame(self, relief = RAISED, borderwidth = 30)
        frame2.pack(fill = X)
        buttonCards = []
            

        listCards = []
        self.first = PhotoImage(file = '../cards/red_0.jpg')
        self.first = self.first.subsample(2,2)
        listCards.append(self.first)
        self.sec = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\red_1.jpg')
        self.sec = self.sec.subsample(2,2)
        listCards.append(self.sec)
        self.third = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\blue_0.jpg')
        self.third = self.third.subsample(2,2)
        listCards.append(self.third)
        self.fourth = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\draw_4.jpg')
        self.fourth = self.fourth.subsample(2,2)
        listCards.append(self.fourth)
        self.fifth = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\green_7.jpg')
        self.fifth = self.fifth.subsample(2,2)
        listCards.append(self.fifth)
        self.sixth = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\yellow_skip.jpg')
        self.sixth = self.sixth.subsample(2,2)
        listCards.append(self.sixth)
        self.seven = PhotoImage(file = 'C:\\Users\\Angel\\Documents\\2nd year - 2nd Term\\NETWORK\\NETWORK_S19-MP\\cards\\green_plus2.jpg')
        self.seven = self.seven.subsample(2,2)
        listCards.append(self.seven)

        self.image = PhotoImage(file = "../cards/blue_1.jpg")
        self.image = self.image.subsample(3, 3)
        self.blue0 = Button (self, text = "HI!", image = self.image)
        self.blue0.pack()

        x = 0
        while x != 6:
            buttonCards.append(Button(frame2, image = listCards[x]))
            buttonCards[x].grid(row = 0, column = x)
            x += 1
            
        
        buttonCards.append(Button(frame2, image = listCards[x]))
        buttonCards[x].grid(row = 1, column = 0)

main = Main ()
main.mainloop()
