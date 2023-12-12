import pygame
from services.load_image import load_image


class Wizard(pygame.sprite.Sprite):
    """Object for handling the player controlled sprite

    Args:
        pygame (pygame.sprite.Sprite): Inherits the pygame sprite class so pygame knows how to handle it correctly
    """
    def __init__(self, x=0, y=0):
        """Constructor, creates the Wizard object

        Args:
            x (int, optional): X-coordinates for the Wizard. Defaults to 0.
            y (int, optional): Y-coordinates for the Wizard. Defaults to 0.
        """
        super().__init__()
        self.image = load_image("wizard.png")
        self.cooldown = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.facing = "left"
        self.health = 3
