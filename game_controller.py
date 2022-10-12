from sys import exit
import pygame
import time

from map.platforms import Platform, MovingPlatformUpDefault
from map.worlds import World1
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

        self.world = World1()

        #self.platform = Platform(0,0)
        self.moving_platform = MovingPlatformUpDefault(100,100, 5 , -5)
        self.run()

    def run(self):
        while True:
            #self.platform.drawn(self.screen)
            self.world.render(self.screen)
            #self.moving_platform.move()
            #self.moving_platform.drawn(self.screen)
            pygame.display.flip()
            self.screen.fill((87,138,52))
            self.clock.tick(20)
            #time.sleep(0.5)
