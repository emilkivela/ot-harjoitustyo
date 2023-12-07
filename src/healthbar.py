import pygame
from load_image import load_image

class HealthBar(pygame.sprite.Sprite):
    """A class to manage the players healthbar and loads the initial healthbar image

    Args:
        pygame (sprite.Sprite): pygame sprite object so pygame knows how to handle it correctly
    """
    def __init__(self, x=0, y=0):
        """Constructor that creates the HealthBar-object

        Args:
            x (int, optional): X-coordinate for the healthbar position. Defaults to 0.
            y (int, optional): Y-coordinate for the healthbar position. Defaults to 0.
        """
        super().__init__()
        self.image = load_image("3hearts.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    