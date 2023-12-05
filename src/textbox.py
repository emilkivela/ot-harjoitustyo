from load_font import load_font
import pygame

class TextBox():
    def __init__(self, x, y, w, h):
        self.box = pygame.Rect(x, y, w, h)
        #self.font = load_font('Acer710_CGA.woff', 20)
        self.passive_color = pygame.Color(105, 105, 105)
        self.active_color = pygame.Color(169, 169, 169)
        self.color = self.passive_color
        self.active = False
        self.text = ''
    
    def toggle(self, event):
        if self.box.collidepoint(event.pos):
            self.active = not self.active
        else:
            self.active = False
        self.change_color()

    def write(self, event):
        if event.key == pygame.K_RETURN:
            print(self.text)
            #self.text = ''
        elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
        else:
            print(event.key)
            self.text += event.unicode
        
    def change_color(self):
        if self.active:
            self.color = self.active_color
        else:
            self.color = self.passive_color
        
    def update(self, width):
        wide = max(120, width+10)
        self.box.w = wide

