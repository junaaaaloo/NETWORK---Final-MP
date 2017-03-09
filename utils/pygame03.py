#pygame_tutorial-03
import pygame
import sys
from pygame.locals import *  # @UnusedWildImport

pygame.init()  # @UndefinedVariable
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Drawing")

WHITE = (255, 255, 255)
pacImg = pygame.image.load('pacman.png')
pacx = 10
pacy = 10
direction = 'R'

while True:
    DISPLAYSURF.fill(WHITE)
    
    if direction == 'R':
        pacx += 5
        if pacx == 280:
            direction = 'D'
    elif direction == 'D':
        pacy += 5
        if pacy == 220:
            direction = 'L'
    elif direction == 'L':
        pacx -= 5
        if pacx == 10:
            direction = 'U'
    elif direction == 'U':
        pacy -= 5
        if pacy == 10:
            direction = 'R'
            
    DISPLAYSURF.blit(pacImg, (pacx, pacy))
    for event in pygame.event.get():
        if event.type == QUIT:  # @UndefinedVariable
            pygame.quit()  # @UndefinedVariable
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)