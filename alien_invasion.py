import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Init game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
        # check bullets are being removed
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
