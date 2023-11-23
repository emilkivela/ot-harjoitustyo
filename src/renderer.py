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
        pygame.display.update()

    def shoot_projectile(self):
        self._level.firebolt.draw(self._display)
        for firebolt in self._level.firebolt:
            if firebolt.facing == "left":
                firebolt.rect.move_ip(-3, 0)
            if firebolt.facing == "right":
                firebolt.rect.move_ip(3, 0)
            if firebolt.facing == "up":
                firebolt.rect.move_ip(0, -3)
            if firebolt.facing == "down":
                firebolt.rect.move_ip(0, 3)
            if self._level.projectile_colliding_walls(firebolt):
                firebolt.kill()
            self._level.projectile_colliding_enemy(firebolt)
            while len(self._level.firebolt) > 3:
                firebolt.kill()

        pygame.display.update()
