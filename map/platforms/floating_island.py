import pygame

class FloatingIsland(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('resources/platforms/floating_island.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.move_ip(position_x, position_y)