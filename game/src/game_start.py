"""
This module implements the GameOn
class for managing the main game loop, handling game events, gameplay mechanics,
and user interface interactions using Pygame.

Classes:
- GameOn:
    Manages the main game loop, game events, gameplay, and UI elements.

    Attributes:
    - clock (pygame.time.Clock): Pygame clock object for controlling FPS.
    - main_location (Locations): Main game location object.
    - partial_backgrounds (list): List of PartialBackground objects for additional backgrounds.
    - platforms (pygame.sprite.Group): Group of platforms in the game.
    - enemies (list): List of enemy groups in the game.
    - gates (None or pygame.sprite.Group): Group of gates in the game.
    - player (object): The player object.
    - npcs (pygame.sprite.Group): Group of NPCs in the game.
    - bosses (None or object): Bosses in the game.
    - gameplay (bool): Flag indicating if the game is in active gameplay.
    - pause (bool): Flag indicating if the game is paused.
    - running (bool): Flag indicating if the game is running.
    - is_restart (bool): Flag indicating if the game should restart.
    - absolute_x (int): Absolute x-coordinate of the game world.
    - is_boss_defeated (bool): Flag indicating if the boss is defeated.
    - is_boss_created (bool): Flag indicating if the boss is created.
    - lose_label (Label): Label object for displaying 'You Lose!' message.
    - pause_label (Label): Label object for displaying 'Pause' message.
    - restart_button (Button): Button object for restarting the game.
    - continue_button (Button): Button object for continuing the game.
    - menu_defeat_button (Button): Button object for returning to the main menu after defeat.

    Methods:
    - __init__(player):
        Initializes the GameOn object with the specified player object.
    - handle_events(screen, events):
        Handles game events such as key presses and button clicks.
    - draw_back_and_platforms(screen):
        Draws the background and platforms on the screen.
    - change_absolute_x(dx):
        Changes the absolute x-coordinate by a given amount.
    - start(screen):
        Starts the game loop and manages game state transitions.

Dependencies:
- External dependencies:
  - pygame: Library for game development in Python with multimedia capabilities.
"""

import sys
from game.src import constants
from game.src import creater
from game.src.button import Button
from game.src.labels import Label
from game.src.platforms import MovingPlatform
from game.src.screen import screen_obj
import pygame


class GameOn:
    """
        GameOn class manages the main game loop and handles game events, gameplay, and UI.

        Attributes:
            clock (pygame.time.Clock): Pygame clock object for controlling FPS.
            main_location (Locations): Main game location object.
            partial_backgrounds (list):
                List of PartialBackground objects for additional backgrounds.
            platforms (pygame.sprite.Group): Group of platforms in the game.
            enemies (list): List of enemy groups in the game.
            gates (None or pygame.sprite.Group): Group of gates in the game.
            player (object): The player object.
            npcs (pygame.sprite.Group): Group of NPCs in the game.
            bosses (None or object): Bosses in the game.
            gameplay (bool): Flag indicating if the game is in active gameplay.
            pause (bool): Flag indicating if the game is paused.
            running (bool): Flag indicating if the game is running.
            is_restart (bool): Flag indicating if the game should restart.
            absolute_x (int): Absolute x-coordinate of the game world.
            is_boss_defeated (bool): Flag indicating if the boss is defeated.
            is_boss_created (bool): Flag indicating if the boss is created.

        Methods:
            __init__(player):
                Initializes the GameOn object.
            handle_events(screen, events):
                Handles game events such as key presses and button clicks.
            draw_back_and_platforms(screen):
                Draws the background and platforms on the screen.
            change_absolute_x(dx):
                Changes the absolute x-coordinate by a given amount.
            start(screen):
                Starts the game loop and manages game state transitions.
        """

    def __init__(self, player):
        """
        Initialize the GameOn class.

        :param player: The player object.
        :rtype: object
        """
        self.clock = pygame.time.Clock()
        self.main_location, self.partial_backgrounds = creater.create_location()
        self.platforms = creater.create_platforms()
        self.enemies = creater.create_enemies()
        self.gates = None

        creater.add_moving_platforms(self.platforms)

        self.player = player
        self.npcs = creater.create_npc()
        self.bosses = None

        self.gameplay = True
        self.pause = False
        self.running = True

        self.is_restart = False

        self.absolute_x = 0
        self.is_boss_defeated = False
        self.is_boss_created = False

        self.lose_label = Label(screen_obj.width, screen_obj.height, None, 72, 'You Lose!',
                                (193, 196, 199), "image/UI/Panel/Window/Medium.png")
        self.pause_label = Label(screen_obj.width, screen_obj.height, None, 72, 'Pause',
                                 (193, 196, 199), "image/UI/Panel/Window/Medium.png")

        self.restart_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100,
                                     "image/UI/Buttons/PlayText/Default@3x.png", "Restart",
                                     "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

        self.continue_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100,
                                      "image/UI/Buttons/PlayText/Default@3x.png", "Continue",
                                      "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

        self.menu_defeat_button = Button((screen_obj.width + 50) / 2, screen_obj.height / 2, 200, 100,
                                         "image/UI/Buttons/PlayText/Default@3x.png",
                                         "Menu", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

    def handle_events(self, screen, events):
        """
        Handle game events.

        :param screen: The screen surface to draw on.
        :param events: The list of events to handle.
        :rtype: None
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if self.gameplay and event.key == pygame.K_ESCAPE:
                    self.pause = True

                if event.key == pygame.K_e:
                    collided_npc = pygame.sprite.spritecollideany(self.player, self.npcs)
                    if collided_npc and collided_npc.has_shop:
                        collided_npc.open_shop(screen, self.player)

            elif event.type == pygame.USEREVENT:
                if event.button == self.restart_button or event.button == self.menu_defeat_button:
                    self.main_location.sound.stop()
                    self.gameplay = True
                    self.player.x = screen_obj.width // 2
                    self.player.y = screen_obj.height - 100 * screen_obj.height_scale
                    self.player.current_hp = 5

                if event.button == self.menu_defeat_button:
                    self.running = False

                if event.button == self.restart_button:
                    self.is_restart = True

                if event.button == self.continue_button:
                    self.main_location.sound.play()
                    self.pause = False

            if self.pause:
                for btn in [self.menu_defeat_button, self.continue_button]:
                    btn.handle_event(event)
            elif not self.gameplay:
                for btn in [self.menu_defeat_button, self.restart_button]:
                    btn.handle_event(event)

    def draw_back_and_platforms(self, screen):
        """
        Draw the background and platforms on the screen.

        :param screen: The screen surface to draw on.
        :rtype: None
        """
        self.main_location.draw_background(screen)

        for part_back in self.partial_backgrounds:
            part_back.draw(screen)

        self.platforms.draw(screen)

    def change_absolute_x(self, dx):
        """
        Change the absolute x-coordinate by a given amount.

        :param dx: The amount to change the absolute x-coordinate by.
        :rtype: None
        """
        self.absolute_x += dx * screen_obj.width_scale

    def start(self, screen):
        """
        Start the game loop.

        :param screen: The screen surface to draw on.
        :return: Whether the game was restarted.
        :rtype: bool
        """
        self.main_location.sound.set_volume(0.5)
        self.main_location.sound.play(-1)

        while self.running:
            self.draw_back_and_platforms(screen)

            for platform in self.platforms:
                if isinstance(platform, MovingPlatform):
                    platform.slide()

            if self.gameplay and not self.pause:
                for enemy_group in self.enemies:
                    enemy_group.update(screen, enemy_group, self)

                self.npcs.update(screen)

                if self.player.current_hp <= 0:
                    self.gameplay = False

                self.player.update(screen, self)

                if self.absolute_x >= screen_obj.width * 4.6 and not self.is_boss_created:
                    self.bosses = creater.add_boss(self.enemies)
                    self.is_boss_created = True
                    self.gates = creater.create_and_add_gates(self.platforms)
            else:
                self.main_location.sound.stop()

                if self.pause:
                    self.pause_label.draw(screen)
                    self.continue_button.draw(screen)
                else:
                    self.lose_label.draw(screen)
                    self.restart_button.draw(screen)

                self.menu_defeat_button.draw(screen)

                for btn in [self.restart_button, self.menu_defeat_button, self.continue_button]:
                    btn.check_hover(pygame.mouse.get_pos())

                self.lose_label.draw_cursor(screen)

            pygame.display.update()
            self.handle_events(screen, pygame.event.get())

            if self.is_restart:
                return self.is_restart

            pygame.time.delay(constants.DELAY)
            self.clock.tick(constants.MAX_FPS)
            pygame.display.flip()
