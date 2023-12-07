import pygame
from load_font import load_font


class Renderer():
    """Class that is responsible rendering the elements on the display.

    Attributes: 
        display: Pygame display to draw on
        level: Level-class, that has information of the current level and the sprites that should be rendered
    """
    def __init__(self, display, level):
        """Class constructor, which creates the Renderer-object 

        Args:
            display (pygame display): Pygame display that is defined in index.py
            level (Level()): Level-object that contains the information for the current level and its sprites
        """
        self._display = display
        self._level = level

    def render(self):
        """Renders all the sprite objects contained in a level
        """
        self._level.all_sprites.draw(self._display)
        pygame.display.update()

    def render_healthbar(self):
        """REnders and updates the players healthbar
        """
        self._display.blit(self._level.healthbar.image, (0, 0))
        pygame.display.update()

    def shoot_projectile(self):
        """Renders the shot fireball to the direction faced. Makes sure there are only 3 fireballs at a time
        """
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
        """Renders the main menu before the actual game is started, its text and the username input

        Args:
            textbox (TextBox()): Object that is responsible for inputting the players username
        """
        font = load_font('Acer710_CGA.woff', 20)
        self._display.fill((0, 0, 0))
        text_surface = font.render(textbox.text, True, (255,255,255))
        start_button = font.render('Enter username and press ENTER', True, (255, 255, 255))
        movement_info = font.render('Arrows to move', True, (255, 255, 255))
        shoot_info = font.render('Space to shoot fireballs', True, (255, 255, 255))

        self._display.blit(start_button, (0,10))
        self._display.blit(movement_info, (0,100))
        self._display.blit(shoot_info, (0,200))
        self._display.blit(text_surface,(textbox.box.x+5, textbox.box.y+5))
        textbox.update(text_surface.get_width())

        pygame.draw.rect(self._display, textbox.color, textbox.box, 2)
        pygame.display.update()

    def render_game_over(self, username):
        """Renders the game over screen after death

        Args:
            username (text): The username that was inputted in main menu
        """
        font = load_font('Acer710_CGA.woff', 20)
        self._display.fill((0, 0, 0))
        death = font.render('Game Over', True, (255, 255, 255))
        name = font.render(f"Player: {username}", True, (255, 255, 255))
        self._display.blit(death, (200,200))
        self._display.blit(name, (200, 250))
        pygame.display.update()
