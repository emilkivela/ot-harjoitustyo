import pygame


class GameLoop:
    def __init__(self, level, renderer, eventqueue, clock, cell_size):
        self._level = level
        self._clock = clock
        self._eventqueue = eventqueue
        self._cell_size = cell_size
        self._renderer = renderer
        self._left = False
        self._right = False
        self._up = False
        self._down = False

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self._left = True

                if event.key == pygame.K_RIGHT:
                    self._right = True

                if event.key == pygame.K_UP:
                    self._up = True

                if event.key == pygame.K_DOWN:
                    self._down = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    self._left = False

                if event.key == pygame.K_RIGHT:
                    self._right = False

                if event.key == pygame.K_UP:
                    self._up = False

                if event.key == pygame.K_DOWN:
                    self._down = False

            elif event.type == pygame.QUIT:
                return False

        if self._left:
            self._level.wizard.facing = "left"
            self._level.move_player(dx=-2)

        if self._right:
            self._level.wizard.facing = "right"
            self._level.move_player(dx=2)

        if self._up:
            self._level.wizard.facing = "up"
            self._level.move_player(dy=-2)

        if self._down:
            self._level.wizard.facing = "down"
            self._level.move_player(dy=2)

    def _render(self):
        self._renderer.render()
