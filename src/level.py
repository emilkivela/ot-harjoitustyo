import pygame
from wizard import Wizard
from floor import Cobble
from wall import Brick
from door import Door
from skeleton import Skeleton
from firebolt import Firebolt
from healthbar import HealthBar
from load_image import load_image
healthbars = [load_image("0hearts.png"), load_image("1heart.png"), load_image("2hearts.png"), load_image("3hearts.png")]

class Level:
    def __init__(self, level_room, cell_size):
        self.cell_size = cell_size
        self.wizard = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        self.skeletons = pygame.sprite.Group()
        self.firebolt = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_room)
        self.enemies.add(self.skeletons)
        self.healthbar = HealthBar()
        

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
        if pygame.sprite.spritecollide(sprite, self.enemies, False):
            print(self.wizard.health) 
            self.wizard.health -= 1
            self.healthbar.image = healthbars[self.wizard.health]
            if self.wizard.health <= 0:
                return True
            else:
                if self.wizard.facing == "up":
                    self.move_player(dy = 32)
                if self.wizard.facing == "down":
                    self.move_player(dy = -32)
                if self.wizard.facing == "left":
                    self.move_player(dx = 32)
                if self.wizard.facing == "right":
                    self.move_player(dx = -32)


    def shoot_projectile(self):
        if self.wizard.facing == "left":
            self.firebolt.add(Firebolt(self.wizard.rect.x - 32, self.wizard.rect.y, "left"))
        
        if self.wizard.facing == "right":
            self.firebolt.add(Firebolt(self.wizard.rect.x + 32, self.wizard.rect.y, "right"))
        
        if self.wizard.facing == "up":
            self.firebolt.add(Firebolt(self.wizard.rect.x, self.wizard.rect.y -32, "up"))
        
        if self.wizard.facing == "down":
            self.firebolt.add(Firebolt(self.wizard.rect.x, self.wizard.rect.y +32, "down"))

    def projectile_colliding_walls(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.walls, False)

    def projectile_colliding_enemy(self, sprite):
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(sprite, enemy):
                enemy.health =-1
            if enemy.health <= 0:
                enemy.kill()

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
                elif cell == 3:
                    self.door.add(Door(normalized_x, normalized_y))
                elif cell == 4:
                    self.floors.add(Cobble(normalized_x, normalized_y))
                    self.skeletons.add(Skeleton(normalized_x, normalized_y))
                
        self.all_sprites.add(self.floors, self.walls, self.wizard, self.door, self.skeletons)

    
