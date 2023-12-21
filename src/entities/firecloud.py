import pygame
from services.load_image import load_image


class Firecloud(pygame.sprite.Sprite):
    """A class to handle the clouds of fire that the dragon shoots

    Args:
        pygame (pygame.sprite.Sprite):
        Inherits pygame sprite object so pygame knows how to handle it.
    """
    def __init__(self, x, y, target_x, target_y):
        """Constructor that creates the Firecloud-object.

        Args:
            x (x): X-coordinates for the Firecloud
            y (y): Y-coordinates for the Firecloud
            facing (str): Which way the player is facing
        """
        super().__init__()
        self.image = load_image("firecloud.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target_x = target_x
        self.target_y = target_y