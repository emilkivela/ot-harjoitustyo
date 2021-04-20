import pygame
from load_image import load_image


class Firebolt(pygame.sprite.Sprite):
    def __init__(self, x, y, facing: str):
        super().__init__()
        self.image = load_image("firebolt.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.facing = facing
