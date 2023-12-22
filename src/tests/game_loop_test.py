import unittest
import pygame

from game.level import Level
from game.game_loop import GameLoop

class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEventQueue:
    def __init__(self, events):
        self._events = events
    
    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

    def render_menu(self, textbox):
        pass

    def render_healthbar(self):
        pass

    def shoot_projectile(self):
        pass

LEVEL_ROOM = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1],
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
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 32

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = [Level(LEVEL_ROOM, CELL_SIZE)]
        self.level2 = [Level(LEVEL_ROOM2, CELL_SIZE)]
    
    def test_enter_changes_game_state(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RETURN), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._game_state, "main_menu")
        game_loop.start()
        
        self.assertEqual(game_loop._game_state, "game")

    def test_pressing_space_shoots_firebolt(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(len(game_loop._level.firebolt), 0)
        game_loop.start()
        self.assertEqual(len(game_loop._level.firebolt), 1)
    
    def test_pressing_down_changes_direction(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN),StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._down, False)
        game_loop.start()
        
        self.assertEqual(game_loop._down, True)
        self.assertEqual(game_loop._level.wizard.facing, "left")
    
    def test_pressing_up_changes_direction(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_UP),StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._up, False)
        game_loop.start()
        
        self.assertEqual(game_loop._up, True)
        self.assertEqual(game_loop._level.wizard.facing, "left")
    
    def test_pressing_left_changes_direction(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT),StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._left, False)
        game_loop.start()
        
        self.assertEqual(game_loop._left, True)
        self.assertEqual(game_loop._level.wizard.facing, "left")

    def test_pressing_right_changes_direction(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._right, False)
        game_loop.start()
        
        self.assertEqual(game_loop._right, True)
        self.assertEqual(game_loop._level.wizard.facing, "left")

    def test_lifting_up_resets_direction(self):
        events = [StubEvent(pygame.KEYUP, pygame.K_UP), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        game_loop._up = True
        self.assertEqual(game_loop._up, True)
        game_loop.start()
        
        self.assertEqual(game_loop._up, False)
    
    def test_lifting_down_resets_direction(self):
        events = [StubEvent(pygame.KEYUP, pygame.K_DOWN), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        game_loop._down = True
        self.assertEqual(game_loop._down, True)
        game_loop.start()
        
        self.assertEqual(game_loop._down, False)
    
    def test_lifting_left_resets_direction(self):
        events = [StubEvent(pygame.KEYUP, pygame.K_LEFT), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        game_loop._left = True
        self.assertEqual(game_loop._left, True)
        game_loop.start()
        
        self.assertEqual(game_loop._left, False)
    
    def test_lifting_right_resets_direction(self):
        events = [StubEvent(pygame.KEYUP, pygame.K_RIGHT), StubEvent(pygame.QUIT, pygame.MOUSEBUTTONDOWN)]

        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        game_loop._right = True
        self.assertEqual(game_loop._right, True)
        game_loop.start()
        
        self.assertEqual(game_loop._right, False)
    
    def test_pressing_right_moves_wizard_correctly(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)]
        game_loop = GameLoop(self.level2, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._level.wizard.facing, "left")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,224))
        game_loop.force_end = True
        game_loop.start()
        self.assertEqual(game_loop._level.wizard.facing, "right")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (290,224))
    
    def test_pressing_left_moves_wizard_correctly(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT)]
        game_loop = GameLoop(self.level2, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._level.wizard.facing, "left")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,224))
        game_loop.force_end = True
        game_loop.start()
        self.assertEqual(game_loop._level.wizard.facing, "left")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (286,224))
    
    def test_pressing_up_moves_wizard_correctly(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_UP)]
        game_loop = GameLoop(self.level2, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._level.wizard.facing, "left")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,224))
        game_loop.force_end = True
        game_loop.start()
        self.assertEqual(game_loop._level.wizard.facing, "up")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,222))
    
    def test_pressing_down_moves_wizard_correctly(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN)]
        #pygame.QUIT, pygame.MOUSEBUTTONDOWN
        game_loop = GameLoop(self.level2, StubRenderer(), StubEventQueue(events), StubClock(), CELL_SIZE)
        self.assertEqual(game_loop._level.wizard.facing, "left")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,224))
        game_loop.force_end = True
        game_loop.start()
        self.assertEqual(game_loop._level.wizard.facing, "down")
        self.assertEqual((game_loop._level.wizard.rect.x,game_loop._level.wizard.rect.y) , (288,226))