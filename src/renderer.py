import pygame
from load_font import load_font


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


    def render_menu(self, textbox):
        self.textbox = textbox
        font = load_font('Acer710_CGA.woff', 20)
        self._display.fill((0, 0, 0))
        self.text_surface = font.render(self.textbox.text, True, (255,255,255))
        start_button = font.render('Enter username and press ENTER', True, (255, 255, 255))
        movement_info = font.render('Arrows to move', True, (255, 255, 255))
        shoot_info = font.render('Space to shoot fireballs', True, (255, 255, 255))

        self._display.blit(start_button, (0,10))
        self._display.blit(movement_info, (0,100))
        self._display.blit(shoot_info, (0,200))
        self._display.blit(self.text_surface,(self.textbox.box.x+5, self.textbox.box.y+5))
        self.textbox.update(self.text_surface.get_width())

        pygame.draw.rect(self._display, self.textbox.color, self.textbox.box, 2)
        pygame.display.update()

    def render_game_over(self, username):
        font = load_font('Acer710_CGA.woff', 20)
        self._display.fill((0, 0, 0))
        death = font.render('Game Over', True, (255, 255, 255))
        name = font.render(f"Player: {username}", True, (255, 255, 255))
        self._display.blit(death, (200,200))
        self._display.blit(name, (200, 250))
        pygame.display.update()
