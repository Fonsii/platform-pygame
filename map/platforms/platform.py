import pygame

class Platform:
    def __init__(self, position_x, position_y):
        self.surface = pygame.image.load('resources/platforms/platform_static.png').convert_alpha()
        self.rect = self.surface.get_rect()
        self.position = self.rect.move([position_x, position_y])

    
    def drawn(self, screen):
        screen.blit(self.surface, self.position)