import datetime
import pygame
from services.load_font import load_font



class Renderer():
    """Class that is responsible rendering the elements on the display.

    Attributes: 
        display: Pygame display to draw on
        level: Level-class, that has information of the current level
        and the sprites that should be rendered
    """
    def __init__(self, display):
        """Class constructor, which creates the Renderer-object 

        Args:
            display (pygame display): 
            Pygame display that is defined in index.py
            
            level (Level()):
                Level-object that contains the information for the current level and its sprites
        """
        self._display = display

    def render(self,level, seconds):
        """Renders all the sprite objects contained in a level and a running clock.
        """
        self._display.fill(pygame.Color('black'))
        level.all_sprites.draw(self._display)
        font = load_font('Acer710_CGA.woff', 15)
        timer = str(datetime.timedelta(seconds=seconds))
        time = font.render(timer, True, (224, 224, 224))
        self._display.blit(time, (100, 6))
        w = time.get_width()
        h = time.get_height()
        border = pygame.Rect(98, 4, w+4, h+4)
        pygame.draw.rect(self._display, (224,224,224), border, 1)
        pygame.display.update()

    def render_healthbar(self, level):
        """Renders and updates the players healthbar
        """
        self._display.blit(level.healthbar.image, (0, 0))

        pygame.display.update()

    def shoot_projectile(self, level):
        """Renders the shot firebolt to the direction faced.
           Makes sure there are only 3 fireballs at a time
        """
        level.firebolt.draw(self._display)
        for firebolt in level.firebolt:
            if firebolt.facing == "left":
                firebolt.rect.move_ip(-3, 0)
            if firebolt.facing == "right":
                firebolt.rect.move_ip(3, 0)
            if firebolt.facing == "up":
                firebolt.rect.move_ip(0, -3)
            if firebolt.facing == "down":
                firebolt.rect.move_ip(0, 3)
            if level.projectile_colliding_walls(firebolt):
                firebolt.kill()
            level.projectile_colliding_enemy(firebolt)
            while len(level.firebolt) > 3:
                firebolt.kill()

        level.firecloud.draw(self._display)
        for cloud in level.firecloud:
            cloud.rect.move_ip(3*cloud.target_x, 3*cloud.target_y)
            if level.projectile_colliding_walls(cloud):
                cloud.kill()
            while len(level.firecloud)  > 3:
                cloud.kill()

        pygame.display.update()


    def render_menu(self, textbox):
        """Renders the main menu before the actual game is started,
           its text and the username input

        Args:
            textbox (TextBox()):
            Object that is responsible for inputting the players username
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

    def render_game_over(self, username, data):
        """Renders the game over screen and the scoreboard of players and their times.

        Args:
            username (text): The username that was inputted in main menu
        """
        font = load_font('Acer710_CGA.woff', 20)
        board = []
        for row in data:
            board.append((row[0], row[1]))
        self._display.fill((0, 0, 0))
        death = font.render('Game Over', True, (255, 255, 255))
        name = font.render(f"Player: {username}", True, (255, 255, 255))
        score = font.render(str(board), True, (255,255,255))
        self._display.blit(death, (200,0))
        self._display.blit(name, (200, 50))
        y = 125
        scoreboard = font.render('Scoreboard:', True, (255, 255, 255))
        self._display.blit(scoreboard, (200, 100))
        for i in range(len(board)):
            score = font.render(f"{i+1}. {board[i][0]} : {board[i][1]}s", True, (255,255,255))
            self._display.blit(score, (200,y))
            y += 25
            if i == 9:
                break
        pygame.display.update()

    def render_game_complete(self, username, data):
        font = load_font('Acer710_CGA.woff', 20)
        board = []
        for row in data:
            board.append((row[0], row[1]))
        self._display.fill((0, 0, 0))
        win = font.render("Congratulations, Game Completed!", True, (255, 255, 255))
        name = font.render(f"Player: {username}", True, (255, 255, 255))
        score = font.render(str(board), True, (255,255,255))
        self._display.blit(win, (5,1))
        self._display.blit(name, (180, 50))
        y = 125
        scoreboard = font.render('Scoreboard:', True, (255, 255, 255))
        self._display.blit(scoreboard, (180, 100))
        for i in range(len(board)):
            score = font.render(f"{i+1}. {board[i][0]} : {board[i][1]}s", True, (255,255,255))
            self._display.blit(score, (200,y))
            y += 25
            if i == 9:
                break
        pygame.display.update()
