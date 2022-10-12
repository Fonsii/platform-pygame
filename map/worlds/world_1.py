import pygame
from map.platforms import Platform, MovingPlatformUpDefault, MainPlatform, FloatingIsland

class World1:
    def __init__(self):
        self.moving_platform = MovingPlatformUpDefault(225,280, 200 , -5)
        self.moving_platform2 = MovingPlatformUpDefault(50,170, 30 , -5)

        self.platform = MainPlatform(0,368)
        
        self.floating_island = FloatingIsland(150,200)
        self.floating_island2 = FloatingIsland(95,30)

        self.platform1 = Platform(335,300)
        self.platform2 = Platform(280,289)
        self.platform3 = Platform(95,180)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.platform1)
        self.platforms.add(self.platform2)
        self.platforms.add(self.platform3)
        self.platforms.add(self.platform)
        self.platforms.add(self.floating_island)
        self.platforms.add(self.floating_island2)


    def render(self, screen):
        self.moving_platform.move()
        self.moving_platform2.move()

        self.moving_platform.draw(screen)
        self.moving_platform2.draw(screen)

        self.platforms.draw(screen)