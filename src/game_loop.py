import pygame

HIT_COOLDOWN = pygame.USEREVENT
HIT_COOLDOWN_ENEMY = pygame.USEREVENT + 1


class GameLoop:
    def __init__(self, level, renderer, eventqueue, clock, cell_size):
        self._level = level
        self._clock = clock
        self._eventqueue = eventqueue
        self._cell_size = cell_size
        self._renderer = renderer
        self._game_state = "main_menu"
        self._left = False
        self._right = False
        self._up = False
        self._down = False

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            
            if self._game_state == "main_menu":
                self._renderer.render_menu()

            if self._game_state == "game":
                self._render()
            
            if self._game_state == "game_over":
                self._renderer.render_game_over()

            self._clock.tick(60)

    def _handle_events(self):

        for event in pygame.event.get():
            if event.type == HIT_COOLDOWN:
                self._level.wizard.cooldown = False
                pygame.time.set_timer(HIT_COOLDOWN, 0)
            if event.type == HIT_COOLDOWN_ENEMY:
                for enemy in self._level.enemies:
                    enemy.cooldown = False
                pygame.time.set_timer(HIT_COOLDOWN_ENEMY, 0)
            if event.type == pygame.KEYDOWN:
                if self._game_state == "main_menu":
                    if event.key == pygame.K_RETURN:
                        self._game_state = "game"

                if event.key == pygame.K_LEFT:
                    self._left = True

                if event.key == pygame.K_RIGHT:
                    self._right = True

                if event.key == pygame.K_UP:
                    self._up = True

                if event.key == pygame.K_DOWN:
                    self._down = True

                if event.key == pygame.K_SPACE:
                    self._level.shoot_projectile()

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

        if self._level._get_colliding_enemies(self._level.wizard):
            self._game_state = "game_over"

    def _render(self):
        self._renderer.render()
        self._renderer.render_healthbar()
        self._renderer.shoot_projectile()
