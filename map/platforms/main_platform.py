import pygame

class MainPlatform(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('resources/platforms/platform_main.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.move_ip(position_x, position_y)