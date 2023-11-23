import os
import pygame

dirname = os.path.dirname(__file__)


def load_font(filename, font_size):
    return pygame.font.Font(os.path.join(dirname, "fonts", filename), font_size)
