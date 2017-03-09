# tetris_logic.py
import random
import copy
from tetris.tetris_utils import colors

class grid:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.grid = [[]]
        i = 0

        while i != x:
            self.grid.append(list())
            j = 0
            while j != y:
                self.grid[i].append(block(i, j, "0", colors.WHITE))
                j += 1
            i += 1

    def __str__ (self):
        msg = ""
        for i in self.grid:
            for j in i:
                msg += str(j)
            msg += "\n"
        return msg

class game:
    def __init__(self):
        self.initialize()
        self.observers = list()

    def initialize (self):
        self.SCORE = 0
        self.FALL = True
        self.GRID = grid (10, 22)
        self.QUEUE = list()
        self.TIME = 360

        i = 0
        while i != 5:
            self.QUEUE.append(tetrimino.randomshape())
            i += 1

    def register (self, obs):
        self.observers.append(obs)

    def notify (self):
        for i in self.observers:
            i.notify()

    def start (self):
        pass

class block:
    def __init__ (self, x, y, symbol, color):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color

    def __str__ (self):
        return self.symbol

    def clone (self):
        return block (self.x, self.y, self.symbol)

class tetriminoFactory:
    def all (self):
        return [T(), O(), Z(), S(), L(), J(), I()]

class tetrimino:
    def all ():
        return [T(), O(), Z(), S(), L(), J(), I()]

    def randomshape ():
        tetriminos = [T(), O(), Z(), S(), L(), J(), I()]
        return tetriminos[random.randint(1, len(tetriminos) - 1)]

    def __init__ (self):
        self.blocks = []
        self.color = colors.WHITE
        i = 0

        while (i < 4):
            self.blocks.append(block(0, 0, "*", self.color))
            i+= 1

    def clone (self):
        t = tetrimino()
        t.blocks = []

        for i in self.blocks:
            t.blocks.append(block(i.x, i.y, i.symbol))

        return t
    def moveLeft (self):
        for i in self.blocks:
            i.x -= 1
            i.board

    def moveRight (self):
        for i in self.blocks:
            i.x += 1

    def moveUp (self):
        for i in self.blocks:
            i.y += 1

    def moveDown (self):
        for i in self.blocks:
            i.y -= 1

    def rotateRight (self):
        origin = self.blocks[0].clone()
        for i in self.blocks:
            i.x -= origin.x
            i.y -= origin.y

            temp = i.x
            i.x = -i.y
            i.y = temp

            i.x += origin.x
            i.y += origin.y

    def rotateLeft (self):
        origin = self.blocks[0].clone()
        for i in self.blocks:

            i.x -= origin.x
            i.y -= origin.y

            temp = i.x
            i.x = i.y
            i.y = -temp

            i.x += origin.x
            i.y += origin.y


    def minY (self):
        yL = []

        for i in self.blocks:
            yL.append(i.y)

        return min(yL)

    def minX (self):
        xL = []

        for i in self.blocks:
            xL.append(i.x)

        return min (xL)

    def __str__ (self):
        msg = ""
        for i in self.blocks:
            msg += "(" + str(i.x) + "," + str(i.y) + ")"

        return msg
    def consoleDisplay (self):
        xL = []
        yL = []

        for i in self.blocks:
            xL.append(i.x)
            yL.append(i.y)

        i = min(yL)
        j = min(xL)
        msg = ""
        while i != max(yL) + 1:
            j = min(xL)
            while j != max(xL) + 1:
                if (i == yL[0] and j == xL[0]) \
                    or  (i == yL[1] and j == xL[1]) \
                    or  (i == yL[2] and j == xL[2]) \
                    or  (i == yL[3] and j == xL[3]):
                    msg += self.blocks[0].symbol
                else:
                    msg += " "
                j+=1
            i+=1
            msg += "\n"

        msg += "\n"
        print(msg)


class T (tetrimino):
    def __init__ (self):
        tetrimino.__init__ (self)
        self.color = colors.VIOLET
        self.blocks = [block(0, 0, "T", self.color), block(0, -1, "T", self.color), block(-1, 0, "T", self.color), block(0, 1, "T", self.color)]

class I (tetrimino):
    def __init__ (self):
        tetrimino.__init__(self)
        self.color = colors.BLUE
        self.blocks = [block(0, -1, "I", self.color), block(0, 0, "I", self.color), block(0, 1, "I", self.color), block(0, 2, "I", self.color)]

class J (tetrimino):
    def __init__(self):
        tetrimino.__init__(self)
        self.color = colors.DARKBLUE
        self.blocks = [block(0, 0, "J", self.color), block(0, 1, "J", self.color), block(1, 1, "J", self.color), block(2, 1, "J", self.color)]

class L (tetrimino):
    def __init__ (self):
        tetrimino.__init__(self)
        self.color = colors.DANDELION
        self.blocks = [block(0, 0, "L", self.color), block(0, -1, "L", self.color), block(-1, 0, "L", self.color), block(-1, 1, "L", self.color)]

class Z (tetrimino):
    def __init__(self):
        tetrimino.__init__(self)
        self.color = colors.RED
        self.blocks = [block(0, 0, "Z", self.color), block(0, -1, "Z", self.color), block(-1, 0, "Z", self.color), block(-1, 1, "Z", self.color)]

class S (tetrimino):
    def __init__(self):
        tetrimino.__init__(self)
        self.color = colors.GREEN
        self.blocks = [block(0, 0, "S", self.color), block(0, -1, "S", self.color), block(1, 0, "S", self.color), block(1, 1, "S", self.color)]

class O (tetrimino):
    def __init__ (self):
        tetrimino.__init__(self)
        self.color = colors.YELLOW
        self.blocks = [block(0, 0, "O", self.color), block(0, 1, "O", self.color), block(-1, 0, "O", self.color), block(-1, 1, "O", self.color)]

g = game ()