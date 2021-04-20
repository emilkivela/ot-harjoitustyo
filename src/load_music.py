import os
import pygame

dirname = os.path.dirname(__file__)

def load_music(filename):
    return pygame.mixer.music.load(os.path.join(dirname, "sounds", filename))
