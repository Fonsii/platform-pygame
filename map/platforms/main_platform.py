import pygame

class MainPlatform(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        self.sprite = pygame.image.load('resources/platforms/platform_main.png').convert_alpha()
        self.surface = self.sprite
        self.rect = self.surface.get_rect()
        self.rect.move_ip(position_x, position_y)

    def draw(self, screen):
        screen.blit(self.surface)

