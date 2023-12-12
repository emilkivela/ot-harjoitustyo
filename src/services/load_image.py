import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(filename):
    """Loads a image file from the sprites folder

    Args:
        filename (str): Name of the image file.

    Returns:
        _type_: pygame function that loads the given image
    """
    return pygame.image.load(os.path.join(dirname, "..", "sprites", filename))
