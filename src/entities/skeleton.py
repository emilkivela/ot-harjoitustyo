import pygame
from services.load_image import load_image

class Skeleton(pygame.sprite.Sprite):
    """Object to take care of the skeleton-type enemies

    Args:
        pygame (pygame.sprite.Sprite):
        Inherits the pygame sprite class, so pygame can identify it correctly when used
    """
    def __init__(self, x=0, y=0):
        """The constructor that makes a Skeleton object

        Args:
            x (int, optional): X-coordinates for the skeleton. Defaults to 0.
            y (int, optional): Y-coordinates for the skeleton. Defaults to 0.
        """
        super().__init__()
        self.cooldown = False
        self.image = load_image("skeleton.png")
        self.health = 2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
