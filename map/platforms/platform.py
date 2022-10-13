import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/platforms/platform_static.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(position_x, position_y)