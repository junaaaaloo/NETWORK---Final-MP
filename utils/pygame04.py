#pygame_tutorial-04
import pygame
import sys
from pygame.locals import *  # @UnusedWildImport

pygame.init()  # @UndefinedVariable
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Font")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.SysFont("Lucida Console", 40, 0, 0, None)
textSurface = fontObj.render("Hello World", True, WHITE, BLACK)
textRect = textSurface.get_rect()
textRect.center = (200, 150)

while True:
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurface, textRect)
    
    for event in pygame.event.get():
        if event.type == QUIT: # @UndefinedVariable
            pygame.quit()  # @UndefinedVariable
            sys.exit()
    pygame.display.update()