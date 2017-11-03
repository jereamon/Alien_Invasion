"""All the necessary code for the alien ships (Scary lions)."""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image. This is getting ridiculous though. My version
        # is a giraffe shooting stylized lions...
        self.image = pygame.image.load('lion.bmp')
        self.rect = self.image.get_rect()

        # Start this image near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien (lion thing) to the screen"""
        self.screen.blit(self.image, self.rect)
