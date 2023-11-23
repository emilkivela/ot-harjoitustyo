import pygame


class Renderer():
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)
        pygame.display.update()
    
    def render_healthbar(self):
        self._display.blit(self._level.healthbar.image, (0, 0))

