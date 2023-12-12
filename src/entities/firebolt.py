import pygame
from services.load_image import load_image


class Firebolt(pygame.sprite.Sprite):
    """A class to handle the fireballs that player shoots

    Args:
        pygame (pygame.sprite.Sprite):
        Inherits pygame sprite object so pygame knows how to handle it.
    """
    def __init__(self, x, y, facing: str):
        """Constructor that creates the Fireball-object.

        Args:
            x (x): X-coordinates for the Fireball
            y (y): Y-coordinates for the Fireball
            facing (str): Which way the player is facing
        """
        super().__init__()
        self.image = load_image("firebolt.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.facing = facing
