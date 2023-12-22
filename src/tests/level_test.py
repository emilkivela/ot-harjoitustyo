import unittest
import pygame
from game.level import Level
from entities.skeleton import Skeleton


LEVEL_ROOM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

LEVEL_ROOM2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 5, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

LEVEL_ROOM3 = [[1, 1, 1, 1, 1, 1, 1, 1, 6, 7, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 0, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 3, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [8, 8, 8, 8, 8, 8, 8, 8, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8]]

CELL_SIZE = 32


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_room = Level(LEVEL_ROOM, CELL_SIZE)
        self.level_room2 = Level(LEVEL_ROOM2, CELL_SIZE)
        self.level_room3 = Level(LEVEL_ROOM3, CELL_SIZE)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_in_floor(self):
        wizard = self.level_room.wizard

        self.assert_coordinates_equal(wizard, CELL_SIZE, CELL_SIZE)

        self.level_room.move_player(dx=2)
        self.assert_coordinates_equal(wizard, 34, 32)

        self.level_room.move_player(dy=2)
        self.assert_coordinates_equal(wizard, 34, 34)
    
    def test_player_cant_move_through_walls(self):
        wizard = self.level_room.wizard
        self.assert_coordinates_equal(wizard, 32, 32)
        self.level_room.move_player(dx=-2)
        self.assert_coordinates_equal(wizard, 32,32)
    
    def test_enemy_collision_reduces_hp(self):
        pygame.init()
        wizard = self.level_room2.wizard
        #self.level_room2.enemies.add(Skeleton(wizard.rect.x, wizard.rect.y))
        self.assertEqual(wizard.health, 3)
        self.level_room2.move_player(dx=2)
        self.level_room2.get_colliding_enemies(wizard)
        self.assertEqual(wizard.health, 2)
        pygame.quit()
    
    def test_switch_collision_opens_doors(self):
        pygame.init()
        self.assertEqual(self.level_room2.doors_open(), False)
        self.level_room2.move_player(dx=-2)
        self.level_room2.switch_collision()
        self.assertEqual(self.level_room2.doors_open(), True)
        pygame.quit()
    
    def test_cannot_move_through_closed_door(self):
        pygame.init()
        wizard = self.level_room2.wizard
        self.assert_coordinates_equal(wizard, 288,288)
        self.level_room2.move_player(dy=-2)
        self.assert_coordinates_equal(wizard, 288,288)
        pygame.quit()
    
    def test_collision_with_open_door_changes_level(self):
        pygame.init()
        self.level_room2.move_player(dx=-2)
        self.level_room2.switch_collision()
        self.assertEqual(self.level_room2.doors_open(), True)
        self.level_room2.move_player(dx=2)
        self.level_room2.move_player(dy=-2)
        self.assertEqual(self.level_room2.check_level_change(), True)
        pygame.quit()
    
    def test_firebolt_faces_same_direction_as_wizard(self):
        wizard = self.level_room2.wizard
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.assertEqual(firebolt.facing, "left")
            firebolt.kill()

        wizard.facing = "right"
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.assertEqual(firebolt.facing, "right")
            firebolt.kill()

        wizard.facing = "down"
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.assertEqual(firebolt.facing, "down")
            firebolt.kill()

        wizard.facing = "up"
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.assertEqual(firebolt.facing, "up")
            firebolt.kill()
    
    def test_firebolt_does_damage_to_enemies(self):
        pygame.init()
        self.level_room2.wizard.facing = "right"
        for enemy in self.level_room2.enemies:
            self.assertEqual(enemy.health, 2)
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.level_room2.projectile_colliding_enemy(firebolt)
        for enemy in self.level_room2.enemies:
            self.assertEqual(enemy.health, 1)
        pygame.quit()
    
    def test_enemies_die(self):
        pygame.init()
        self.level_room2.wizard.facing = "right"
        for enemy in self.level_room2.enemies:
            enemy.health = 1
        self.level_room2.shoot_projectile()
        for firebolt in self.level_room2.firebolt:
            self.level_room2.projectile_colliding_enemy(firebolt)
        self.assertEqual(len(self.level_room2.enemies), 0)
        pygame.quit()
    
    def test_boss_gate_works_as_inteded(self):
        for door in self.level_room3.doors:
            self.assertTrue(door.open)




        
