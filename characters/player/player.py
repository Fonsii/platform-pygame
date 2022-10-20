import pygame
import time
from enum import Enum
class StateGame(Enum):
    PLAYING = 1
    WIN = 2
    GAME_OVER = 3
class Player(pygame.sprite.Sprite):
    def __init__(self, start_position_x, start_position_y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.gravity = 2
        self.jump_height = 76
        self.lose = False
        self.wining = False
        self.first_jump = True

        self.sprite = pygame.image.load('resources/player/test_player.png').convert_alpha()
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.move_ip(start_position_x, start_position_y)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    def apply_gravity(self):
        self.rect.y += self.gravity

    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x + self.speed < 400 - self.image.get_width():
                self.rect.x += self.speed
            else:
                self.rect.x = 400 - self.image.get_width() 
            self.rect.x += self.speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 0

        if self.first_jump and keys[pygame.K_SPACE]:
            self.first_jump = False
            if self.rect.y - self.jump_height > self.image.get_height():
                self.rect.y -= self.jump_height
            else:
                self.rect.y = 0


    def move(self, platforms, moving_platforms, enemies, flag):
        if self.lose or self.get_collision_enemies(enemies):
            self.lose = True
            return StateGame.GAME_OVER
        elif self.wining or self.get_collision_flag(flag):
            self.wining = True
            return StateGame.WIN
        else:
            self.get_input()

            if not self.get_collision_platforms(platforms) and not self.get_collision_moving_platforms(moving_platforms):
                self.apply_gravity()
            else:
                self.first_jump = True
            
        return StateGame.PLAYING

    def get_collision_platforms(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)

        if hits:
            if hits[0].rect.top == self.rect.bottom - 2:
                return True
            elif hits[0].rect.bottomleft > self.rect.topright or hits[0].rect.topleft < self.rect.bottomright: #Side collider
                if hits[0].rect.x < self.rect.x:
                    self.rect.x = hits[0].rect.x + hits[0].rect.width
                else:
                    self.rect.x = hits[0].rect.x - self.rect.width
            else: #Botton collider
                self.rect.y = hits[0].rect.y - self.rect.height

        return False

    
    def get_collision_moving_platforms(self, moving_platforms):
        hits = pygame.sprite.spritecollide(self, moving_platforms, False)

        if hits:
            if hits[0].rect.top == self.rect.bottom - 2 or hits[0].rect.top == self.rect.bottom - 1:
                if not hits[0].allow_movement:
                    hits[0].set_allow_movement()

                if hits[0].movement_state == 'DEFAULT':
                    self.rect.y += hits[0].speed
                else:
                    self.rect.y -= hits[0].speed

                return True
            elif hits[0].rect.bottomleft > self.rect.topright or hits[0].rect.topleft < self.rect.bottomright: #Side collider
                if hits[0].rect.x < self.rect.x:
                    self.rect.x = hits[0].rect.x + hits[0].rect.width
                else:
                    self.rect.x = hits[0].rect.x - self.rect.width
            else: #Botton collider
                self.rect.y = hits[0].rect.y - self.rect.height

        return False


    def get_collision_enemies(self, enemies):
        hits = pygame.sprite.spritecollide(self, enemies, False)
        
        if hits:
            return True
        else:
            return False

    
    def get_collision_flag(self, flag):
        hit = self.rect.colliderect(flag)

        if hit:
            return True
        else:
            return False