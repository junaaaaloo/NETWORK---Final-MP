from tkinter import *
from tetris import tetris_model
import random

def createBlock (tetrimino):
    currblock = list()

    return currblock

WIDTH = 400
HEIGHT = 600
SIDE = 20
SCORE = 0
FONT = ("Lucida Sans", 20)
GAME = True

root = Tk()
root.geometry('400x600')

canvas = Canvas (root, width = WIDTH, height = HEIGHT)
canvas.pack()

currblock = list()
currblock.append (canvas.create_rectangle((0, 0, SIDE, SIDE), fill = "yellow"))
currblock.append (canvas.create_rectangle((SIDE, SIDE, 2*SIDE, 2*SIDE), fill = "yellow"))
currblock.append (canvas.create_rectangle((0, SIDE, SIDE, 2*SIDE), fill = "yellow"))
currblock.append (canvas.create_rectangle((SIDE, 0, 2*SIDE, SIDE), fill = "yellow"))

statusVar = StringVar()
statusVar.set("Score: ")
statusLabel = Label(root, text = statusVar, font = FONT)

statusVar.pack()

canvas.focus_set()
root.mainloop()
