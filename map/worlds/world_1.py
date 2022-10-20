import pygame
from map.platforms import Platform, MovingPlatformUpDefault, MainPlatform, FloatingIsland
from characters.player import Player, StateGame
from characters.mobs import Crab
from map.utils import Flag

class World1:
    def __init__(self):
        self.player = Player(0,0, 6)
        self.platforms = pygame.sprite.Group()
        self.moving_platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        

        moving_platform = MovingPlatformUpDefault(225,280, 200 , -5)
        moving_platform2 = MovingPlatformUpDefault(50,170, 30 , -5)

        platform = MainPlatform(0,368)
        
        floating_island = FloatingIsland(150,200)
        floating_island2 = FloatingIsland(95,30)

        platform1 = Platform(335,300)
        platform2 = Platform(280,289)
        platform3 = Platform(95,180)

        crab1 = Crab(floating_island, 2)
        crab2 = Crab(platform, 2)

        self.flag_end = Flag(floating_island2)

        self.platforms.add(platform1)
        self.platforms.add(platform2)
        self.platforms.add(platform3)
        self.platforms.add(platform)
        self.platforms.add(floating_island)
        self.platforms.add(floating_island2)

        self.moving_platforms.add(moving_platform)
        self.moving_platforms.add(moving_platform2)

        self.enemies.add(crab1)
        self.enemies.add(crab2)



    def render(self, screen):
        state = self.player.move(self.platforms, self.moving_platforms, self.enemies, self.flag_end)
        if state == StateGame.GAME_OVER:
            print("losing")
        elif state == StateGame.WIN:
            print("winning")


        self.player.draw(screen)

        for moving_platform in self.moving_platforms:
            moving_platform.move()

        for enemy in self.enemies:
            enemy.move()

        self.flag_end.draw(screen)
        self.moving_platforms.draw(screen)
        self.platforms.draw(screen)
        self.enemies.draw(screen)