#pygame_tutorial-02
import pygame
import sys
from pygame.locals import *  # @UnusedWildImport

pygame.init()  # @UndefinedVariable
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.draw.rect(DISPLAYSURF, RED, (20, 20, 19, 19))
pygame.draw.rect(DISPLAYSURF, RED, (40, 20, 19, 19))
pygame.draw.rect(DISPLAYSURF, RED, (40, 40, 19, 19))
pygame.draw.rect(DISPLAYSURF, RED, (40, 60, 19, 19))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        
        if event.type == QUIT:  # @UndefinedVariable
            pygame.quit()  # @UndefinedVariable
            sys.exit()
        pygame.display.update()