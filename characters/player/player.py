import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_position_x, start_position_y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.gravity = 1
        self.jump_height = 10

        self.sprite = pygame.image.load('resources/player/test_player.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.move_ip(start_position_x, start_position_y)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    def apply_gravity(self):
        self.rect.y += self.gravity

    
    def move(self):
        self.get_input()
        self.apply_gravity()

    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x + self.speed < 400 - self.image.get_width():
                self.rect.x += self.speed
            else:
                self.rect.x = 400 - self.image.get_width() 
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 0
        elif keys[pygame.K_SPACE]:
            if self.rect.y - self.jump_height > self.image.get_height():
                self.rect.y -= self.jump_height
            else:
                self.rect.y = 0