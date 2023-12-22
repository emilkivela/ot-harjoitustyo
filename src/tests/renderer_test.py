import pygame
import unittest
from game.level import Level
from game.renderer import Renderer
from entities.textbox import TextBox

LEVEL_ROOM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1],
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
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 32

class TestRenderer(unittest.TestCase):
    def setUp(self):
        self._level = Level(LEVEL_ROOM, CELL_SIZE)
        self._display = pygame.display.set_mode((640, 480))
        self._username = "testname"
        self._scoreboard = [("first", 1), ("seccond", 2), ("third", 3), ("fourth", 4)]
    
    def test_no_more_than_3_fireballs(self):
        renderer = Renderer(self._display)
        
        self._level.shoot_projectile()
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firebolt), 1)
      
        self._level.shoot_projectile()
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firebolt), 2)

        self._level.shoot_projectile()
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firebolt), 3)
        
        self._level.shoot_projectile()
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firebolt), 3)

    def test_no_more_than_3_fireclouds(self):
        renderer = Renderer(self._display)
        
        self._level.shoot_firecloud(32,32,288,224)
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firecloud), 1)
      
        self._level.shoot_firecloud(32,32,288,224)
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firecloud), 2)

        self._level.shoot_firecloud(32,32,288,224)
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firecloud), 3)
        
        self._level.shoot_firecloud(32,32,288,224)
        renderer.shoot_projectile(self._level)
        self.assertEqual(len(self._level.firecloud), 3)

                                               
