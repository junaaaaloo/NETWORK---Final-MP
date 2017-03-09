'''
Created on Mar 2, 2017
@author: Jonal Ray Ticug
'''

import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")
fpsClock = pygame.time.Clock()

limitx = 500
limity = 400

FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


x = [20, 40, 40, 40]
y = [20, 20, 40, 60]
orientation = 'U'
i = 0

while (i < 4):
    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
    i += 1

while True:
    DISPLAYSURF.fill(BLACK)
    add = 0
    if orientation == 'U':
        if( y[0] == 340 and \
        y[1] == 340 and \
        y[2] == 360 and \
        y[3] == 380):
            pass
        else:
            add = 20;
    if orientation == 'R':
        if(y[0] == 360 and \
        y[1] == 380 and \
        y[2] == 380 and \
        y[3] == 380):
            pass
        else:
            add = 20;
    if orientation == 'L':
        if ( y[0] == 380 and \
        y[1] == 360 and \
        y[2] == 360 and \
        y[3] == 360):
            pass
        else:
            add = 20;
    if orientation == 'D':
        if (y[0] == 380 and \
        y[1] == 380 and \
        y[2] == 360 and \
        y[3] == 340):
            pass
        else:
            add = 20;

    i = 0
    while (i < 4):
        y[i] += add;
        pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
        i += 1

    for event in pygame.event.get():


        if event.type == pygame.KEYDOWN: # @UndefinedVariable
            if event.key == pygame.K_LEFT:  # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0
                while (i < 4):
                    x[i] -= 20;
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            if event.key == pygame.K_RIGHT:  # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0
                while (i < 4):
                    x[i] += 20;
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            if event.key == pygame.K_DOWN:  # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0
                while (i < 4):
                    y[i] += 20;
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            if event.key == pygame.K_SPACE: # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0
                if orientation == 'U':
                    y[0] = 340
                    y[1] = 340
                    y[2] = 360
                    y[3] = 380
                if orientation == 'R':
                    y[0] = 360
                    y[1] = 380
                    y[2] = 380
                    y[3] = 380
                if orientation == 'L':
                    y[0] = 380
                    y[1] = 360
                    y[2] = 360
                    y[3] = 360
                if orientation == 'D':
                    y[0] = 380
                    y[1] = 380
                    y[2] = 360
                    y[3] = 340

                while (i < 4):
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            if event.key == pygame.K_UP:  # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0

                if orientation == 'U':
                    x[0] += 40
                    x[1] += 20
                    y[1] += 20
                    x[3] -= 20
                    y[3] -= 20
                    orientation = 'R'
                elif orientation == 'R':
                    y[0] += 40
                    x[1] -= 20
                    y[1] += 20
                    x[3] += 20
                    y[3] -= 20
                    orientation = 'D'
                elif orientation == 'D':
                    x[0] -= 40
                    x[1] -= 20
                    y[1] -= 20
                    x[3] += 20
                    y[3] += 20
                    orientation = 'L'
                elif orientation == 'L':
                    y[0] -= 40
                    x[1] += 20
                    y[1] -= 20
                    x[3] -= 20
                    y[3] += 20
                    orientation = 'U'

                while (i < 4):
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            if event.key == pygame.K_LCTRL:  # @UndefinedVariable
                DISPLAYSURF.fill(BLACK)
                i = 0

                if orientation == 'U':
                    y[0] += 40
                    x[1] -= 20
                    y[1] += 20
                    x[3] += 20
                    y[3] -= 20
                    orientation = 'L'
                elif orientation == 'L':
                    x[0] += 40
                    x[1] += 20
                    y[1] += 20
                    x[3] -= 20
                    y[3] -= 20
                    orientation = 'D'
                elif orientation == 'D':
                    y[0] -= 40
                    x[1] += 20
                    y[1] -= 20
                    x[3] -= 20
                    y[3] += 20
                    orientation = 'R'
                elif orientation == 'R':
                    x[0] -= 40
                    x[1] -= 20
                    y[1] -= 20
                    x[3] += 20
                    y[3] += 20
                    orientation = 'U'

                while (i < 4):
                    pygame.draw.rect(DISPLAYSURF, RED, (x[i], y[i], 19, 19))
                    i += 1
            print(x, y)
        if event.type == QUIT:  # @UndefinedVariable
            pygame.quit()  # @UndefinedVariable
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
