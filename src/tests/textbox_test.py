import unittest
import pygame
from entities.textbox import TextBox

class TestTextBox(unittest.TestCase):
    def setUp(self):
        self.textbox = TextBox(0, 0, 50, 50)
    
    def test_rect_dimensions(self):
        self.assertEqual(self.textbox.box.w, 50)
    
    def test_update_width_under_120(self):
        self.textbox.update(70)
        self.assertEqual(self.textbox.box.w, 120)
    
    def test_update_width_over_120(self):
        self.textbox.update(150)
        self.assertEqual(self.textbox.box.w, 160)
    
    def test_clicking_activates(self):
        self.assertEqual(self.textbox.active, False)
        self.assertEqual(self.textbox.color, pygame.Color(224, 224, 224))
        testevent = pygame.event.Event(pygame.KEYDOWN, {"pos":(0,0)})
        self.textbox.toggle(testevent)
        self.assertEqual(self.textbox.active, True)
        self.assertEqual(self.textbox.color, pygame.Color(0, 240, 0))

    def test_activation_changes_colour(self):
        self.textbox.change_color()
        self.assertEqual(self.textbox.color, pygame.Color(224, 224, 224))
        self.textbox.active = True
        self.textbox.change_color()
        self.assertEqual(self.textbox.color, pygame.Color(0, 240, 0))
    
    def test_key_inputs_writes_text(self):
        self.assertEqual(self.textbox.text, "")
        testevent = pygame.event.Event(pygame.KEYDOWN, {"key":pygame.K_a, "unicode":"a"})
        self.textbox.write(testevent)
        self.assertEqual(self.textbox.text, "a")
    
    def test_text_cant_go_over_12_characters(self):
        self.assertEqual(self.textbox.text, "")
        testevent = pygame.event.Event(pygame.KEYDOWN, {"key":pygame.K_a, "unicode":"123456789101112"})
        self.assertEqual(self.textbox.text, "")
    
    def test_backspace_removes_character(self):
        self.textbox.text = "test"
        testevent = pygame.event.Event(pygame.KEYDOWN, {"key":pygame.K_BACKSPACE})
        self.textbox.write(testevent)
        self.assertEqual(self.textbox.text, "tes")
