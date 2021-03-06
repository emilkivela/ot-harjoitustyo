import pygame

HIT_COOLDOWN = pygame.USEREVENT # pylint: disable=no-member
HIT_COOLDOWN_ENEMY = pygame.USEREVENT + 1 # pylint: disable=no-member

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
            self._renderer.render_healthbar()
            self._renderer.shoot_projectile()

            self._clock.tick(60)

    def _handle_events(self):

        for event in pygame.event.get():
            if event.type == HIT_COOLDOWN:
                self._level.wizard.cooldown = False
                pygame.time.set_timer(HIT_COOLDOWN, 0)
            #if event.type == HIT_COOLDOWN_ENEMY:
            #    self._level.enemies
            if event.type == pygame.KEYDOWN: # pylint: disable=no-member

                if event.key == pygame.K_LEFT: # pylint: disable=no-member
                    self._left = True

                if event.key == pygame.K_RIGHT: # pylint: disable=no-member
                    self._right = True

                if event.key == pygame.K_UP: # pylint: disable=no-member
                    self._up = True

                if event.key == pygame.K_DOWN: # pylint: disable=no-member
                    self._down = True

                if event.key == pygame.K_SPACE: # pylint: disable=no-member
                    self._level.shoot_projectile()

            if event.type == pygame.KEYUP: # pylint: disable=no-member

                if event.key == pygame.K_LEFT: # pylint: disable=no-member
                    self._left = False

                if event.key == pygame.K_RIGHT: # pylint: disable=no-member
                    self._right = False

                if event.key == pygame.K_UP: # pylint: disable=no-member
                    self._up = False

                if event.key == pygame.K_DOWN: # pylint: disable=no-member
                    self._down = False

            elif event.type == pygame.QUIT: # pylint: disable=no-member
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

        if self._level._get_colliding_enemies(self._level.wizard):
            return False

    def _render(self):
        self._renderer.render()
