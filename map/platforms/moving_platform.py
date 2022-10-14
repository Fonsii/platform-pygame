import pygame

class MovingPlatformUpDefault(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, max_position_y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_default = pygame.image.load('resources/platforms/platform_moving_up.png').convert_alpha()
        self.sprite_reset = pygame.image.load('resources/platforms/platform_moving_down.png').convert_alpha()

        self.movement_restrictions = {'movement_default' : max_position_y, 'movement_reset' : position_y}
        self.movement_state = 'DEFAULT'
        self.allow_movement = False
        self.speed = speed

        self.image = self.sprite_default
        self.rect = self.image.get_rect()
        self.rect.move_ip(position_x, position_y)
        self.position = self.rect.move([position_x, position_y])


    def move(self):
        if self.movement_state == 'DEFAULT' and self.allow_movement:
            self.default_movement()
        elif self.movement_state == 'RESET':
            self.reset_movement()

    
    def default_movement(self):
        if self.rect.y + self.speed < self.movement_restrictions['movement_default']:
            self.movement_state = 'RESET'
            self.image = self.sprite_reset
            self.reset_movement()
        else:
            self.rect.y += self.speed


    def reset_movement(self):
        if self.rect.y - self.speed > self.movement_restrictions['movement_reset']:
            self.allow_movement = False
            self.movement_state = 'DEFAULT'
            self.image = self.sprite_default
        else:
            self.rect.y -= self.speed

    
    def set_allow_movement(self):
        self.allow_movement = True