import pygame
from map.platforms import Platform, MovingPlatformUpDefault, MainPlatform, FloatingIsland
from characters.player import Player

class World1:
    def __init__(self):
        self.player = Player(0,0, 5)

        self.moving_platform = MovingPlatformUpDefault(225,280, 200 , -5)
        self.moving_platform2 = MovingPlatformUpDefault(50,170, 30 , -5)

        platform = MainPlatform(0,368)
        
        floating_island = FloatingIsland(150,200)
        floating_island2 = FloatingIsland(95,30)

        platform1 = Platform(335,300)
        platform2 = Platform(280,289)
        platform3 = Platform(95,180)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(platform1)
        self.platforms.add(platform2)
        self.platforms.add(platform3)
        self.platforms.add(platform)
        self.platforms.add(floating_island)
        self.platforms.add(floating_island2)


    def render(self, screen):
        self.player.move(self.platforms)
        self.player.draw(screen)

        self.moving_platform.move()
        self.moving_platform2.move()

        self.moving_platform.draw(screen)
        self.moving_platform2.draw(screen)

        self.platforms.draw(screen)