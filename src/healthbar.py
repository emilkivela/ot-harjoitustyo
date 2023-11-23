import pygame
from load_image import load_image

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = load_image("3hearts.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    