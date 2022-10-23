from sys import exit
import pygame
from characters.player import StateGame
import time

from map.worlds import World1
class GameController:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Platform Game')
        self.clock = pygame.time.Clock()
        self.screen.fill((87,138,52))

        self.font_text = pygame.font.SysFont("Garamond", 20, bold=True)

        self.world = World1()

        self.run()
    

    def restart(self):
        self.world = World1()
        self.run()


    def run(self):
        while True:
            game_state = self.world.render(self.screen)
            self.events(game_state)
            if game_state == StateGame.WIN:
                self.restart_phrase()
                self.middle_phrase("You Win!")
            elif game_state == StateGame.GAME_OVER:
                self.restart_phrase()
                self.middle_phrase("You Lose :(")
            pygame.display.flip()
            self.screen.fill((87,138,52))
            self.clock.tick(20)

    
    def events(self, game_state):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pygame.quit()
                        exit()
                    elif event.key == 114 and game_state != StateGame.PLAYING:
                        self.restart()

    
    def restart_phrase(self):
        phrase_display = self.font_text.render("Press R to restart the game", False, "White")
        self.screen.blit(phrase_display, (75,376))

    
    def middle_phrase(self, phrase):
        pygame.display.set_caption(phrase)