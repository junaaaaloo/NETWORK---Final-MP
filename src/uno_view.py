from tkinter import *

class Server (Tk):
    def __init__ (self):
        Tk.__init__(self)
        #self.wm_iconbitmap("") #for icons
        self.title("KWATRO!")
        self.geometry("600x600+300+0")
        self.resizable(0, 0)

        self.image = PhotoImage(file = "../cards/blue_1.jpg")
        self.image = self.image.subsample(3, 3)
        self.blue0 = Button (self, text = "HI!", image = self.image)
        self.blue0.pack()

main = Server ()
main.mainloop()