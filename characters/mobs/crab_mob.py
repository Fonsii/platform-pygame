import pygame
import time

class Crab(pygame.sprite.Sprite):
    def __init__(self, floating_island_to_guard, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.side_movement = 'RIGHT'

        self.sprite = pygame.image.load('resources/mobs/enemy_crab.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.border = {
            'left': floating_island_to_guard.rect.topleft[0],
            'right': floating_island_to_guard.rect.topright[0] - self.image.get_width()
        }

        self.rect.move_ip(floating_island_to_guard.rect.topright[0] - self.image.get_width(), floating_island_to_guard.rect.topright[1] - self.image.get_height())


    def move(self):
        if self.side_movement == 'RIGHT' and self.rect.x + self.speed > self.border['right']:
            self.speed *= -1
            self.side_movement = 'LEFT'
        
        if self.side_movement == 'LEFT' and self.rect.x - self.speed < self.border['left']:
            self.speed *= -1
            self.side_movement = 'RIGHT'
        
        self.rect.x += self.speed