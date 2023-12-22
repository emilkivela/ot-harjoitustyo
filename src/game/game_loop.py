import time
import pygame
from entities.textbox import TextBox
from repositories.resultrepository import ResultRepository
from connect_db import get_db_connection
HIT_COOLDOWN = pygame.USEREVENT
HIT_COOLDOWN_ENEMY = pygame.USEREVENT + 1


class GameLoop:
    """The GameLoop class that is responsible for changing game state, player inputs and saving data to database
    """
    def __init__(self, levels, renderer, eventqueue, clock, cell_size):
        self._levels = levels
        self._level_number = 0
        self._level = self._levels[self._level_number]
        self._clock = clock
        self._eventqueue = eventqueue
        self._cell_size = cell_size
        self._renderer = renderer
        self.textbox = TextBox(10, 40, 100, 35)
        self._game_state = "main_menu"
        self._left = False
        self._right = False
        self._up = False
        self._down = False
        self.start_time = 0
        self.scoreboard = ''
        self.connection = get_db_connection()
        self.resultrepo = ResultRepository(get_db_connection())
        self.force_end = False

    def start(self):
        """The function that starts the game loop 
        """
        while True:

            if self._handle_events() is False:
                break

            if self._game_state == "main_menu":
                self._renderer.render_menu(self.textbox)

            if self._game_state == "game":
                current_time = self._clock.get_ticks()
                self._level.update_enemies(current_time)
                self._render()

            if self._game_state == "game_over":

                self._renderer.render_game_over(self.textbox.text, self.scoreboard)

            if self._game_state == "game_completed":
                self._renderer.render_game_complete(self.textbox.text, self.scoreboard)

            self._clock.tick(60)
            str(int(time.time()-self.start_time))
        pygame.quit()

    def _handle_events(self):
        """The method that is responsible for player inputs and changing game state

        Returns:
            Boolean: True id game loop should continue, False if not
        """

        for event in self._eventqueue.get():
            if event.type == HIT_COOLDOWN:
                self._level.wizard.cooldown = False
                pygame.time.set_timer(HIT_COOLDOWN, 0)

            if event.type == HIT_COOLDOWN_ENEMY:
                for enemy in self._level.enemies:
                    enemy.cooldown = False
                pygame.time.set_timer(HIT_COOLDOWN_ENEMY, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.textbox.toggle(event)

            if event.type == pygame.KEYDOWN:
                if self.textbox.active:
                    self.textbox.write(event)

                if event.key == pygame.K_RETURN:
                    if self._game_state == "main_menu":
                        self.start_time = time.time()
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
        self._level.wizard.update()

        if self._game_state == "game":
            if self._level.get_colliding_enemies(self._level.wizard):
                self.scoreboard = self.resultrepo.get_scoreboard()
                self._game_state = "game_over"

            if self._level.boss_dead:
                self.resultrepo.save_info(self.textbox.text, int(time.time()-self.start_time))
                self.scoreboard = self.resultrepo.get_scoreboard()
                self._game_state = "game_completed"

            if self._level.check_level_change():
                self._level_number += 1
                if self._level_number <= len(self._levels)-1:
                    self._level = self._levels[self._level_number]

            if self._level.switch_collision():
                self._level.doors.update()

        if self.force_end:
            return False
        return True

    def _render(self):
        """Calls for rendering in the main game state
        """
        self._renderer.render(self._level, int(time.time()-self.start_time))
        self._renderer.render_healthbar(self._level)
        self._renderer.shoot_projectile(self._level)
