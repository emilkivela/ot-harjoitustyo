import pygame
from services.load_image import load_image


class Torch(pygame.sprite.Sprite):
    """Class to handle the torch texture sprites

    Args:
        pygame (pygame.sprite.Sprite):
        Inherits the pygame sprite class so pygame knows how to handle it correctly
    """
    def __init__(self, x=0, y=0):
        """Constructor that creates the Torch object

        Args:
            x (int, optional): X-coordinates for the torch sprite. Defaults to 0.
            y (int, optional): Y-coordinates for the torch sprite. Defaults to 0.
        """
        super().__init__()

        self.image = load_image("torch1.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y