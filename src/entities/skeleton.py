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
        self.image = load_image("skeleton_small.png")
        self.health = 2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.previous_move_time = 0
        self.aggro = False
        self.speed = 1.5

    def should_move(self, current_time):
        """Checks how much time has passed since the skeleton last moved

        Args:
            current_time (int): The time in milliseconds since the game started

        Returns:
            Boolean: Returns True if 2 seconds have passed since the skeleton last moved,
                     False otherwise
        """
        return current_time - self.previous_move_time >= 2000

    def update(self):
        """Updates the picture if the skeleton is aggroed
        """
        if self.aggro:
            self.image = load_image("skeleton_big.png")
        else:
            self.image = load_image("skeleton_small.png")
