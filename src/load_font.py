import os
import pygame

dirname = os.path.dirname(__file__)


def load_font(filename, font_size):
    """Loads a custom font from a given file and creates a pygame font object based on it

    Args:
        filename (str): Name of the font file
        font_size (int): Font size

    Returns:
        pygame.font.Font: pygame font object with the given custom font and font size
    """
    return pygame.font.Font(os.path.join(dirname, "fonts", filename), font_size)
