#pygame_tutorial-01
import pygame
import sys
from pygame.locals import *  # @UnusedWildImport

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello, World!")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # @UndefinedVariable
            sys.exit()
        pygame.display.update()
    
