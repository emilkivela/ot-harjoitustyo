import pygame
import random
import math

from entities.wizard import Wizard
from entities.skeleton import Skeleton
from entities.cobble import Cobble
from entities.brick import Brick
from entities.door import Door
from entities.healthbar import HealthBar
from entities.firebolt import Firebolt
from entities.switch import Switch
from entities.torch import Torch
from entities.gate import Gate
from entities.water import Water
from entities.dragon import Dragon
from entities.firecloud import Firecloud

from game.game_loop import HIT_COOLDOWN, HIT_COOLDOWN_ENEMY

from services.load_image import load_image

HEALTHBARS = [load_image("0hearts.png"), load_image("1heart.png"),
              load_image("2hearts.png"), load_image("3hearts.png")]


class Level:
    """Class that handles everything contained in a level, such as the sprites and their actions.
    """
    def __init__(self, level_room, cell_size):
        """Constructor that creates the Level object

        Args:
            level_room (list): A matrix that contains the information what is where in the level
            cell_size (int): The dimensions for each sprite. This game uses 32 x 32 pixel sprites
        """
        self.cell_size = cell_size
        self.wizard = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.switch = pygame.sprite.Group()
        self.skeletons = pygame.sprite.Group()
        self.dragons = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.firebolt = pygame.sprite.Group()
        self.firecloud = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_room)
        self.healthbar = HealthBar()

    def move_player(self, dx=0, dy=0):
        """Moves the player sprite on the level

        Args:
            dx (int, optional): How much the player is moved on the x-axis Defaults to 0.
            dy (int, optional): How much the player is moved on the y-axis. Defaults to 0.
        """

        if not self._player_can_move(dx, dy):
            return
        self.wizard.rect.move_ip(dx, dy)

    def update_enemies(self, current_time):
        """Checks if the enemies should move or enter the aggro state

        Args:
            current_time (int): Current time in millisecods since the game started
        """
        pool = [-20, 0, 20]
        for enemy in self.enemies:
            if enemy not in self.firecloud:
                if math.dist((self.wizard.rect.x, self.wizard.rect.y), (enemy.rect.x, enemy.rect.y)) < 150:
                    enemy.aggro = True
                if enemy.aggro:
                    dx, dy = self.wizard.rect.x - enemy.rect.x, self.wizard.rect.y - enemy.rect.y
                    dist = math.hypot(dx, dy)
                    dx, dy = dx / dist, dy / dist
                    self.move_enemy(enemy, dx, dy)
                else: 
                    if enemy.should_move(current_time):
                        self.move_enemy(enemy, random.choice(pool), random.choice(pool))
                        enemy.previous_move_time = current_time
                if enemy in self.dragons:
                    if enemy.should_shoot(current_time):
                        self.shoot_firecloud(enemy.rect.x, enemy.rect.y, self.wizard.rect.x, self.wizard.rect.y)
                        enemy.previous_shoot_time = current_time
        self.enemies.update()

    def move_enemy(self, enemy, dx, dy):
        dx = enemy.speed * dx
        dy = enemy.speed * dy
        """Moves the enemy to the given direction if can

        Args:
            enemy (pygame.sprite.Sprite): The pygame sprite object of the enemy that should be moven
            dx (int): How much the enemy is moved on the x-axis
            dy (_type_): How much the enemy is moved on the y-axis
        """
        if self.enemy_can_move(enemy, dx, dy):
            enemy.rect.move_ip(dx, dy)

    def enemy_can_move(self, enemy, dx, dy):
        """Checks if the enemy is trying to move through a wall

        Args:
            enemy (pygame.sprite.Sprite): The pygame sprite object of the enemy that should be moven
            dx (int): How much the enemy is moved on the x-axis
            dy (_type_): How much the enemy is moved on the y-axis

        Returns:
            _type_: _description_
        """
        enemy.rect.move_ip(dx, dy)
        colliding = pygame.sprite.spritecollide(enemy, self.walls, False)
        can_move = not colliding
        enemy.rect.move_ip(-dx, -dy)
        return can_move

    def _player_can_move(self, dx=0, dy=0):
        """Checks if the player can move in the wanted direction,
           or if it collides with objects (such as walls)

        Args:
            dx (int, optional): The wanted place to move the player on the x-axis. Defaults to 0.
            dy (int, optional): The wanted place to move the player on the y-axis. Defaults to 0.

        Returns:
            Boolean: The information if the player collides with walls or not
        """
        self.wizard.rect.move_ip(dx, dy)

        colliding_walls = pygame.sprite.spritecollide(self.wizard, self.walls, False)
        
        can_move = not colliding_walls

        if pygame.sprite.spritecollide(self.wizard, self.doors, False) and not self.doors_open():
            can_move = False

        self.wizard.rect.move_ip(-dx, -dy)

        return can_move

    def switch_collision(self):
        if pygame.sprite.spritecollide(self.wizard, self.switch, False):
            for door in self.doors:
                door.open = True
            return True
        return False

    def get_colliding_enemies(self, sprite):
        """Checks if the player collides with enemies,
          makes the player lose hp, 
          checks if he dies and gives i-frames and push back,
          updates health bar image

        Args:
            sprite (Wizard()): _The player sprite

        Returns:
            Boolean: Returns True if the players health drops to 0
        """
        if pygame.sprite.spritecollide(sprite, self.enemies, False):
            if not self.wizard.cooldown:
                self.wizard.health -= 1
                self.wizard.cooldown = True
                pygame.time.set_timer(HIT_COOLDOWN, 1000)
            self.healthbar.image = HEALTHBARS[self.wizard.health]
            if self.wizard.health <= 0:
                return True
            if self.wizard.facing == "up":
                self.move_player(dy=32)
            if self.wizard.facing == "down":
                self.move_player(dy=-32)
            if self.wizard.facing == "left":
                self.move_player(dx=32)
            if self.wizard.facing == "right":
                self.move_player(dx=-32)
        return False

    def doors_open(self):
        """Checks if the doors open-attribute is True or not

        Returns:
            Boolean: True if door is open, False if not
        """
        for door in self.doors:
            if not door.open:
                return False
        return True

    def check_level_change(self):
        """Checks if the player collides with an open door, which results in a level change

        Returns:
            Boolean: Return True if there is a collide and door is open, False if not
        """
        if pygame.sprite.spritecollide(self.wizard, self.doors, False) and self.doors_open():
            return True
        return False

    def shoot_projectile(self):
        """Shoots the firebolt in the direction the player is facing
        """
        if self.wizard.facing == "left":
            self.firebolt.add(Firebolt(self.wizard.rect.x - 32, self.wizard.rect.y, "left"))

        if self.wizard.facing == "right":
            self.firebolt.add(Firebolt(self.wizard.rect.x + 32, self.wizard.rect.y, "right"))

        if self.wizard.facing == "up":
            self.firebolt.add(Firebolt(self.wizard.rect.x, self.wizard.rect.y -32, "up"))

        if self.wizard.facing == "down":
            self.firebolt.add(Firebolt(self.wizard.rect.x, self.wizard.rect.y +32, "down"))
    
    def shoot_firecloud(self, start_x, start_y, target_x, target_y):
        end = pygame.math.Vector2(target_x, target_y)
        start = pygame.math.Vector2(start_x, start_y)
        s = pygame.math.Vector2(end-start)
        s.normalize_ip()
        cloud = Firecloud(start_x, start_y, s[0], s[1])
        self.firecloud.add(cloud)
        self.enemies.add(cloud)

    def projectile_colliding_walls(self, sprite):
        """Checks if the projectile sprite collides with walls

        Args:
            sprite (Fireball(): The Fireball-sprite

        Returns:
            Boolean: Return if the fireball collides
        """
        return pygame.sprite.spritecollide(sprite, self.walls, False)

    def projectile_colliding_enemy(self, sprite):
        """Checks if the fireball collides with an enemy, and if so, makes it take damage

        Args:
            sprite (Firebolt()): The Firebolt-sprite
        """
        for enemy in self.enemies:
            if enemy not in self.firecloud:
                if pygame.sprite.collide_rect(sprite, enemy):
                    sprite.kill()
                    if not enemy.cooldown:
                        enemy.health -= 1
                        enemy.cooldown = True
                        pygame.time.set_timer(HIT_COOLDOWN_ENEMY, 1000)
                if enemy.health <= 0:
                    enemy.kill()

    def _initialize_sprites(self, level_room):
        """Builds the level sprites based on the given numbers on the level matrix

        Args:
            level_room (list): The level matrix information
        """

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
                    self.doors.add(Door(normalized_x, normalized_y))
                elif cell == 3:
                    self.wizard = Wizard(normalized_x, normalized_y)
                    self.floors.add(Cobble(normalized_x, normalized_y))
                elif cell == 4:
                    self.floors.add(Cobble(normalized_x, normalized_y))
                    self.skeletons.add(Skeleton(normalized_x, normalized_y))
                elif cell == 5:
                    self.switch.add(Switch(normalized_x, normalized_y))
                    self.floors.add(Cobble(normalized_x, normalized_y))
                elif cell == 6:
                    self.walls.add(Brick(normalized_x, normalized_y))
                    self.walls.add(Torch(normalized_x, normalized_y))
                elif cell == 7:
                    self.doors.add(Gate(normalized_x, normalized_y))
                elif cell == 8:
                    self.floors.add(Water(normalized_x, normalized_y))
                elif cell == 9:
                    self.floors.add(Cobble(normalized_x, normalized_y))
                    self.dragons.add(Dragon(normalized_x, normalized_y))

        self.enemies.add(self.skeletons, self.dragons, self.firecloud)
        self.all_sprites.add(self.floors, self.walls, self.doors,
                              self.switch, self.enemies, self.wizard)
