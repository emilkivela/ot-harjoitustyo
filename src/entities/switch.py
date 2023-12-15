import pygame
from services.load_image import load_image


class Switch(pygame.sprite.Sprite):
    """Class to handle the switch texture sprites

    Args:
        pygame (pygame.sprite.Sprite):
        Inherits the pygame sprite class so pygame knows how to handle it correctly
    """
    def __init__(self, x=0, y=0):
        """Constructor that creates the Switch object

        Args:
            x (int, optional): X-coordinates for the switch sprite. Defaults to 0.
            y (int, optional): Y-coordinates for the switch sprite. Defaults to 0.
        """
        super().__init__()

        self.image = load_image("switch.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
