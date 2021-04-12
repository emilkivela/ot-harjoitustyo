import pygame
from wizard import Wizard
from floor import Cobble
from wall import Brick
from door import Door
from skeleton import Skeleton

class Level:
    def __init__(self, level_room, cell_size):
        self.cell_size = cell_size
        self.wizard = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        self.skeletons = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_room)
        self.enemies.add(self.skeletons)
        

    def move_player(self, dx=0, dy=0):
        if not self._player_can_move(dx, dy):
            return
        
        self.wizard.rect.move_ip(dx, dy)
    
    def _player_can_move(self, dx = 0, dy = 0):
        self.wizard.rect.move_ip(dx, dy)

        colliding_walls = pygame.sprite.spritecollide(self.wizard, self.walls, False)

        can_move = not colliding_walls

        self.wizard.rect.move_ip(-dx, -dy)

        return can_move
    
    def _get_colliding_enemies(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.enemies, False)
    
    def _initialize_sprites(self, level_room):
        height = len(level_room)
        width = len(level_room[0])

        for y in range(height):
            for x in range(width):
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
                elif cell == 3:
                    self.door.add(Door(normalized_x, normalized_y))
                elif cell == 4:
                    self.floors.add(Cobble(normalized_x, normalized_y))
                    self.skeletons.add(Skeleton(normalized_x, normalized_y))
                
        self.all_sprites.add(self.floors, self.walls, self.wizard, self.door, self.skeletons)

    
