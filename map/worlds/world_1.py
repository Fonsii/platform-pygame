import pygame
from map.platforms import Platform, MovingPlatformUpDefault, MainPlatform

class World1:
    def __init__(self):
        self.moving_platform = MovingPlatformUpDefault(100,100, 5 , -5)
        self.platform = MainPlatform(0,368)
        self.platform1 = Platform(0,0)
        self.platform2 = Platform(50,50)
        self.platform3 = Platform(200,200)
        self.platform4 = Platform(300,300)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.platform1)
        self.platforms.add(self.platform2)
        self.platforms.add(self.platform3)
        self.platforms.add(self.platform4)


    def render(self, screen):
        self.platform.draw(screen)
        self.platforms.draw(screen)