import pygame


class EventQueue:
    """Class that is responsible for fetching pygame events
    """
    def get(self):
        return pygame.event.get()
