"""Main game for Alien Invasion. More or less copied from Pyth Crash Course
and typed by Jeremy Monroe.
"""

import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        )
    pygame.display.set_caption("Alien Invasion!")

    # make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
