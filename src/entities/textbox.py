import pygame

class TextBox():
    """A class to handle the username input, and the box that surrounds the text output
    """
    def __init__(self, x, y, w, h):
        """Constructor creates the TextBox object.

        Args:
            x (int): X-coordinates for the box
            y (int): Y-coordinate for the box
            w (int): Width of the box
            h (int): Height of the box
        """
        self.box = pygame.Rect(x, y, w, h)
        self.passive_color = pygame.Color(224, 224, 224)
        self.active_color = pygame.Color(0, 240, 0)
        self.color = self.passive_color
        self.active = False
        self.text = ''

    def toggle(self, event):
        """Checks if the user clicks the textbox to activate it

        Args:
            event (pygame.MOUSEBUTTONDOWN): 
            The method is feeded pygame events when a mouse button is pressed
        """
        if self.box.collidepoint(event.pos):
            self.active = not self.active
        else:
            self.active = False
        self.change_color()

    def write(self, event):
        """Manages the string that is written as the username if the textbox is active.

        Args:
            event (pygame.KEYDOWN): The method is feeded keyboard presses
        """
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.key == pygame.K_RETURN:
            self.active = False
        else:
            if len(self.text) <= 12:
                self.text += event.unicode

    def change_color(self):
        """Changes the color of the textbox depending if its active or not
        """
        if self.active:
            self.color = self.active_color
        else:
            self.color = self.passive_color

    def update(self, width):
        """Updates the width of the box as the length of the string changes.

        Args:
            width (int): Width of the text surface.
        """
        wide = max(120, width+10)
        self.box.w = wide
