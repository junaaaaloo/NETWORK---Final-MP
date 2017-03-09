#tetris_control
import pygame
from copy import deepcopy
import time
import sys
from pygame.locals import QUIT
from tetris.tetris_utils import colors

class app:
    HEIGHT = 400
    WIDTH = 700
    BLOCK_SIZE = 20
    FPS = 30

    FONT = "Lucida Sans"
    MUSIC = "res/bg_music.wav"

    COUNTDOWN = 5
    FLASH = False
    GAMESTART = False

    # Initializations
    def __init__ (self):
        self.SCORE = 0
        self.TOGGLE = True
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAY = pygame.display.set_mode((app.HEIGHT, app.WIDTH), 0, 32)
        pygame.display.set_caption("Tetris Battle")

    def loadmusic (self):
        pygame.mixer.music.load(app.MUSIC)
        pygame.mixer.music.play(-1)

    def loadfonts (self):
        self.SYSFONT = pygame.font.SysFont(app.FONT, 20)
        self.HEADERFONT = pygame.font.SysFont(app.FONT, 50, italic = True)

    def start (self):
        pygame.init()
        self.loadmusic()
        self.loadfonts()

        while True:
            self.DISPLAY.fill(colors.BLACK)
            if self.TOGGLE:
                title = self.HEADERFONT.render("TETRIS BATTLE", 1, colors.WHITE)
                title_s = title.get_rect()
                title_s.center = (app.HEIGHT/2, app.WIDTH/2)
                status = self.SYSFONT.render("Press B to Battle, E to Exit", 1, colors.WHITE)
                rect_s = status.get_rect()
                rect_s.center = (app.HEIGHT/2, app.WIDTH/2 + 100)
                self.DISPLAY.blit(status, rect_s)
                self.DISPLAY.blit(title, title_s)
            elif app.COUNTDOWN != 0:
                app.FPS = 1
                countdown = self.SYSFONT.render("Game starts in " + str(app.COUNTDOWN), 1, colors.WHITE)
                countdown_rect = countdown.get_rect()
                countdown_rect.center = (app.HEIGHT/2, app.WIDTH/2)
                self.DISPLAY.blit(countdown, countdown_rect)
                app.COUNTDOWN -= 1
            else:
                app.FPS = 30
                status = self.SYSFONT.render("Score: " + str(self.SCORE), 1, colors.WHITE)
                st_rect = status.get_rect()
                self.DISPLAY.blit(status, st_rect)
                self.game.start()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b and self.TOGGLE:
                        self.TOGGLE = False

            pygame.display.update()
            self.FPSCLOCK.tick(app.FPS)


app = app ()
app.start()




