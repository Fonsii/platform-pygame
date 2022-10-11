from sys import exit
import pygame
import time

from map.platforms import Platform, MovingPlatformUpDefault

class GameController:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Platform Game')
        self.clock = pygame.time.Clock()
        self.screen.fill((87,138,52))

        self.font_score = pygame.font.SysFont("Garamond", 32)
        self.font_text = pygame.font.SysFont("Garamond", 30, bold=True)

        #self.platform = Platform(0,0)
        self.moving_platform = MovingPlatformUpDefault(100,100, 5 , -5)
        self.game()

    def game(self):
        self.clock.tick(60)

        while True:
            #self.platform.drawn(self.screen)
            self.moving_platform.move()
            self.moving_platform.drawn(self.screen)
            pygame.display.flip()
            self.screen.fill((87,138,52))
            time.sleep(0.5)
