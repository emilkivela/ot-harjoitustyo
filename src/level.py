import pygame
from wizard import Wizard
from floor import Cobble
from wall import Brick
from load_image import load_image

class Level:
    def __init__(self, level_room, cell_size):
        self.cell_size = cell_size
        self.wizard = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_room)


    def move_player(self, dx=0, dy=0):
        #if not self._player_can_move(dx, dy):
        #    return
        self.wizard.rect.move_ip(dx, dy)

    def _initialize_sprites(self, level_room):

        for y in range(15):
            for x in range(20):
                cell = level_room[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Cobble(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Brick(normalized_x, normalized_y))
                elif cell == 2:
                    self.wizard = Wizard(normalized_x, normalized_y)
                    self.floors.add(Cobble(normalized_x, normalized_y))        

        self.all_sprites.add(self.floors, self.walls, self.wizard)


