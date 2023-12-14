import pygame
from assets.level_maps import LEVEL_MAPS
from entities.eventqueue import EventQueue
from entities.clock import Clock

from game.game_loop import GameLoop
from game.renderer import Renderer
from game.level import Level






CELL_SIZE = 32


def main():
    display = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Dungeon Crawler")
    levels = []
    for map in LEVEL_MAPS:
        levels.append(Level(map, CELL_SIZE))
    eventqueue = EventQueue()
    renderer = Renderer(display)
    clock = Clock()
    game_loop = GameLoop(levels, renderer, eventqueue, clock, CELL_SIZE)

    pygame.init()
    game_loop.start()
    pygame.quit()

if __name__ == "__main__":
    main()
