#pygame_tutorial-05
import pygame
import sys
from pygame.locals import *  # @UnusedWildImport

pygame.init()  # @UndefinedVariable
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Sounds")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)

pygame.mixer.init()
pygame.mixer.music.load('bg_music.wav')
pygame.mixer.music.play()

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT: # @UndefinedVariable
            pygame.quit()  # @UndefinedVariable
            sys.exit()
    pygame.display.update()
