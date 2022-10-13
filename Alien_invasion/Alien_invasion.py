import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    
    pygame.display.set_caption("Alien Invasion")

    #creating ship
    ship = Ship(screen)

    while True:

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()
