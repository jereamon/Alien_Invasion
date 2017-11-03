"""Various settings for project_start.py (main game)"""

# import pygame


class Settings():
    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (250, 250, 250)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = .5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 120
        self.bullets_allowed = 3
