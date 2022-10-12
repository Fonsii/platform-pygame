import pygame

class MovingPlatformUpDefault(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, max_position_y, speed):
        self.sprite_default = pygame.image.load('resources/platforms/platform_moving_up.png').convert_alpha()
        self.sprite_reset = pygame.image.load('resources/platforms/platform_moving_down.png').convert_alpha()

        self.movement_restrictions = {'movement_default' : max_position_y, 'movement_reset' : position_y}
        self.movement_state = 'DEFAULT'
        self.speed = speed

        self.surface = self.sprite_default
        self.rect = self.surface.get_rect()
        self.position = self.rect.move([position_x, position_y])

    
    def drawn(self, screen):
        screen.blit(self.surface, self.position)

    
    def move(self):
        if self.movement_state == 'DEFAULT':
            self.default_movement()
        elif self.movement_state == 'RESET':
            self.reset_movement()

    
    def default_movement(self):
        if self.position.y + self.speed < self.movement_restrictions['movement_default']:
            self.movement_state = 'RESET'
            self.surface = self.sprite_reset
            self.reset_movement()
        else:
            self.position.y += self.speed


    def reset_movement(self):
        if self.position.y - self.speed > self.movement_restrictions['movement_reset']:
            self.movement_state = 'DEFAULT'
            self.surface = self.sprite_default
            self.default_movement()
        else:
            self.position.y -= self.speed