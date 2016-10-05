import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    # Init game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
