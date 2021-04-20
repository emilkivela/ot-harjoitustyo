import os
import pygame

dirname = os.path.dirname(__file__)

def load_music(filename):
    background_music = pygame.mixer.Sound(os.path.join(dirname, "sounds", filename))
    return background_music
