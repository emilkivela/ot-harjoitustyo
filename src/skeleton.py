import pygame
from load_image import load_image

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.cooldown = False
        self.image = load_image("skeleton.png")
        self.health = 2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y