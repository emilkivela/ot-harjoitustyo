import os
import pygame

dirname = os.path.dirname(__file__) # pylint: disable=invalid-name

def load_image(filename):
    return pygame.image.load(os.path.join(dirname, "sprites", filename))
