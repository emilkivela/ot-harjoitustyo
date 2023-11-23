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
    
    def render_menu(self):
        font = pygame.font.SysFont('arial', 40)
        self._display.fill((0, 0, 0))
        start_button = font.render('Press ENTER to start', True, (255, 255, 255))
        movement_info = font.render('Arrows to move', True, (255, 255, 255))
        shoot_info = font.render('Space to shoot fireballs', True, (255, 255, 255))
        self._display.blit(start_button, (150,100))
        self._display.blit(movement_info, (150,200))
        self._display.blit(shoot_info, (150,300))
        pygame.display.update()
    
    def render_game_over(self):
        font = pygame.font.SysFont('arial', 40)
        self._display.fill((0, 0, 0))
        death = font.render('You died', True, (255, 255, 255))
        self._display.blit(death, (200,200))
        pygame.display.update()
