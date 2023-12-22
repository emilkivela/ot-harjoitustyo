import pygame
from services.load_image import load_image


class Door(pygame.sprite.Sprite):
    """Class to handle the cobblestone texture sprites
    Args:
        pygame (pygame.sprite.Sprite):
        Inherits the pygame sprite class so pygame knows how to handle it correctly
    """
    def __init__(self, x=0, y=0):
        """Constructor that creates the Gate object

        Args:
            x (int, optional): X-coordinates for the boss gate sprite. Defaults to 0.
            y (int, optional): Y-coordinates for the boss gate sprite. Defaults to 0.
        """
        super().__init__()
        self.image = load_image("dngn_closed_door.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.open = False

    def update(self):
        if self.open:
            self.image = load_image("dngn_open_door.png")
        else:
            self.image = load_image("dngn_closed_door.png")
