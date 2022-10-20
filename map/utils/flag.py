import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self, last_floating_island):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('resources/utils/flag.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.move_ip(last_floating_island.rect.topright[0] - self.image.get_width(), last_floating_island.rect.topright[1] - self.image.get_height())

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)