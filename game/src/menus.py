"""
This module defines classes for various menus and menu-related functionality in a Pygame-based game.

Classes:
- Menu: Represents a basic menu with common menu operations and attributes.
- MainMenu: Represents the main menu of the game, inheriting from Menu.
- SettingsMenu: Represents the settings menu of the game, inheriting from Menu.
- VideoMenu: Represents the video settings menu, inheriting from Menu.
- SelectorMenu: Represents a menu with selectable items, inheriting from Menu.
- SelectorCharacter:
    Represents a specific selector menu for choosing character types, inheriting from SelectorMenu.

Attributes and Methods:
- Menu Class:
    Attributes:
    - MAX_FPS (int): Maximum frames per second for the menu.
    - clock (pygame.time.Clock): Pygame clock object for timing.
    - cursor (pygame.Surface): Surface for the cursor image.
    - is_restart (bool): Flag indicating if the menu should restart.
    - can_move_buttons (bool): Flag indicating if buttons can be moved.
    - title (str): Title of the menu.
    - WIDTH (int): Width of the menu screen.
    - HEIGHT (int): Height of the menu screen.
    - main_background (pygame.Surface): Background surface for the menu.

    Methods:
    - draw_menu(menu_obj, screen): Draws the menu on the screen.
    - fade(screen): Creates a fade effect on the screen.
    - check_size(): Checks and updates the menu size based on the screen size.

- MainMenu Class (Inherits from Menu):
    Attributes:
    - start_button (Button): Button for starting the game.
    - settings_button (Button): Button for accessing settings.
    - exit_button (Button): Button for exiting the game.
    - buttons (list): List of all buttons in the main menu.
    - title (str): Title of the main menu.
    - settings_menu (SettingsMenu): Settings menu object.

    Methods:
    - handle_events(event, screen, running): Handle events specific to the main menu.

- SettingsMenu Class (Inherits from Menu):
    Attributes:
    - audio_button (Button): Button for audio settings.
    - video_button (Button): Button for video settings.
    - back_button (Button): Button for returning to the previous menu.
    - buttons (list): List of all buttons in the settings menu.
    - title (str): Title of the settings menu.
    - video_menu (VideoMenu): Video settings menu object.

    Methods:
    - handle_events(event, screen, running): Handle events specific to the settings menu.

- VideoMenu Class (Inherits from Menu):
    Attributes:
    - resolution1_button (Button): Button for selecting 960x600 resolution.
    - resolution2_button (Button): Button for selecting 1280x800 resolution.
    - resolution3_button (Button): Button for selecting fullscreen resolution.
    - back_button (Button): Button to return to the previous menu.
    - buttons (list): List of buttons in the video settings menu.
    - title (str): Title of the menu, set to "Video Settings".

    Methods:
    - handle_events(event, screen, running): Handle events specific to the video settings menu.

- SelectorMenu Class (Inherits from Menu):
    Attributes:
    - can_move_buttons (bool): Flag indicating if buttons can be moved.
    - title (str): Title of the menu.
    - buttons (list): List of buttons in the menu.
    - returned (list): List of returned values corresponding to each button.

    Methods:
    - handle_events(event, screen, running): Handle events specific to the selector menu.
    - choice(screen): Display the choice menu and handle interaction.

- SelectorCharacter Class (Inherits from SelectorMenu):
    Attributes:
    Inherits attributes from SelectorMenu.

    Methods:
    - __init__(): Initialize the SelectorCharacter object.
"""

# Import statements for game dependencies
# (constants, various hero classes, Button, GameOn, screen_obj, sys, pygame)
import sys
from game.src import constants
from game.src.Heroes.fire_knight import FireKnight
from game.src.Heroes.leaf_ranger import LeafRanger
from game.src.Heroes.standard_hero import StandardHero
from game.src.Heroes.water_princess import WaterPrincess
from game.src.Heroes.wind_hashahin import WindHashahin
from game.src.button import Button
from game.src.game_start import GameOn
from game.src.screen import screen_obj
import pygame


class Menu:
    """
        A class representing a menu in a game.

        Attributes:
            MAX_FPS (int): Maximum frames per second for the menu.
            clock (pygame.time.Clock): Pygame clock object for timing.
            cursor (pygame.Surface): Surface for the cursor image.
            is_restart (bool): Flag indicating if the menu should restart.
            can_move_buttons (bool): Flag indicating if buttons can be moved.
            title (str): Title of the menu.
            WIDTH (int): Width of the menu screen.
            HEIGHT (int): Height of the menu screen.
            main_background (pygame.Surface): Background surface for the menu.

        Methods:
            draw_menu(menu_obj, screen):
                Draws the menu on the screen.
            fade(screen):
                Creates a fade effect on the screen.
            check_size():
                Checks and updates the menu size based on the screen size.
        """

    def __init__(self):
        """
        Initialize the Menu object.

        :rtype: object
        """
        self.MAX_FPS = constants.MAX_FPS
        self.clock = pygame.time.Clock()
        self.cursor = pygame.image.load("image/UI/cursor/cursor.png").convert_alpha()
        self.is_restart = False

        self.can_move_buttons = True
        self.title = ""

    WIDTH = screen_obj.width
    HEIGHT = screen_obj.height
    main_background = pygame.transform.scale(pygame.image.load("image/UI/Panel/Window/Big.png").convert_alpha(),
                                             (WIDTH, HEIGHT))

    @staticmethod
    def draw_menu(menu_obj, screen):
        """
        Draw the menu on the screen.

        :param menu_obj: The menu object to be drawn.
        :param screen: The screen surface to draw on.
        :rtype: None | object
        :return: Result of menu interaction, if any.
        """
        pygame.mouse.set_visible(False)

        running = [True]
        while running[0]:
            screen.fill((0, 0, 0))

            if menu_obj.is_restart:
                menu_obj.is_restart = False
                menu_obj.fade(screen)
                player = SelectorCharacter().choice(screen_obj.screen)
                menu_obj.fade(screen)
                menu_obj.is_restart = GameOn(player).start(screen)

            screen.blit(menu_obj.main_background, (0, 0))

            font = pygame.font.Font(None, 72)
            text_surface = font.render(menu_obj.title, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(Menu.WIDTH / 2, 60))
            screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running[0] = False
                    pygame.quit()
                    sys.exit()

                result = menu_obj.handle_events(event, screen, running)

                if result:
                    return result

                for btn in menu_obj.buttons:
                    btn.handle_event(event)

            for btn in menu_obj.buttons:
                if menu_obj.can_move_buttons:
                    btn.set_pos((Menu.WIDTH - 252) / 2)
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            screen.blit(menu_obj.cursor, pygame.mouse.get_pos())

            pygame.display.flip()

    def fade(self, screen):
        """
        Create a fade effect on the screen.

        :param screen: The screen surface to draw on.
        :rtype: None
        """
        running = True
        fade_alpha = 0  # level of transparency

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            fade_surface = pygame.Surface((Menu.WIDTH, Menu.HEIGHT))
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))

            fade_alpha += 10
            if fade_alpha >= 200:
                fade_alpha = 255
                running = False

            pygame.display.flip()
            self.clock.tick(self.MAX_FPS)

    @staticmethod
    def check_size():
        """
        Check and update the menu size based on the screen size.

        :rtype: None
        """
        if Menu.WIDTH != screen_obj.width:
            Menu.WIDTH = screen_obj.width
            Menu.HEIGHT = screen_obj.height
            Menu.main_background = pygame.transform.scale(Menu.main_background, (Menu.WIDTH, Menu.HEIGHT))


class MainMenu(Menu):
    """
        A class representing the main menu in a game, inherits from Menu.

        Attributes:
            start_button (Button): Button for starting the game.
            settings_button (Button): Button for accessing settings.
            exit_button (Button): Button for exiting the game.
            buttons (list): List of all buttons in the main menu.
            title (str): Title of the main menu.
            settings_menu (SettingsMenu): Settings menu object.

        Methods:
            handle_events(event, screen, running):
                Handle events specific to the main menu.
        """

    def __init__(self):
        """
        Initialize the MainMenu object.

        :rtype: object
        """
        super().__init__()

        self.start_button = Button(Menu.WIDTH / 2 - (252 / 2), 200, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                   "Play", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.settings_button = Button(Menu.WIDTH / 2 - (252 / 2), 300, 252, 74,
                                      "image/UI/Buttons/PlayText/Default@3x.png",
                                      "Settings", "image/UI/Buttons/PlayText/Hover@3x.png",
                                      "sound/knopka-schelchok.mp3")
        self.exit_button = Button(Menu.WIDTH / 2 - (252 / 2), 400, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                  "Exit", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.buttons = [self.start_button, self.settings_button, self.exit_button]

        self.title = "Menu"

        self.settings_menu = SettingsMenu()

    def handle_events(self, event, screen, running):
        """
        Handle events for the main menu.

        :param event: The event to handle.
        :param screen: The screen surface to draw on.
        :param running: A list with a boolean indicating if the menu is running.
        :rtype: None
        """
        if event.type == pygame.USEREVENT:

            if event.button == self.exit_button:
                running[0] = False
                pygame.quit()
                sys.exit()

            if event.button == self.settings_button:
                self.fade(screen)
                Menu.draw_menu(self.settings_menu, screen)

            if event.button == self.start_button:
                self.fade(screen)
                player = SelectorCharacter().choice(screen_obj.screen)
                self.is_restart = GameOn(player).start(screen)


class SettingsMenu(Menu):
    """
        A class representing the settings menu in a game, inherits from Menu.

        Attributes:
            audio_button (Button): Button for audio settings.
            video_button (Button): Button for video settings.
            back_button (Button): Button for returning to previous menu.
            buttons (list): List of all buttons in the settings menu.
            title (str): Title of the settings menu.
            video_menu (VideoMenu): Video settings menu object.

        Methods:
            handle_events(event, screen, running):
                Handle events specific to the settings menu.
        """

    def __init__(self):
        """
        Initialize the SettingsMenu object.

        :rtype: object
        """
        super().__init__()

        self.audio_button = Button(Menu.WIDTH / 2 - (252 / 2), 200, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                   "Audio", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.video_button = Button(Menu.WIDTH / 2 - (252 / 2), 300, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                   "Video", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.back_button = Button(Menu.WIDTH / 2 - (252 / 2), 400, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                  "Back", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.buttons = [self.audio_button, self.video_button, self.back_button]

        self.title = "Settings"

        self.video_menu = VideoMenu()

    def handle_events(self, event, screen, running):
        """
        Handle events for the settings menu.

        :param event: The event to handle.
        :param screen: The screen surface to draw on.
        :param running: A list with a boolean indicating if the menu is running.
        :rtype: None
        """
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or
                event.type == pygame.USEREVENT and event.button == self.back_button):
            self.fade(screen)
            running[0] = False

        if event.type == pygame.USEREVENT and event.button == self.video_button:
            self.fade(screen)
            Menu.draw_menu(self.video_menu, screen)


class VideoMenu(Menu):
    """
        VideoMenu class represents the menu for video settings.

        Attributes:
            resolution1_button (Button): Button for selecting 960x600 resolution.
            resolution2_button (Button): Button for selecting 1280x800 resolution.
            resolution3_button (Button): Button for selecting fullscreen resolution.
            back_button (Button): Button to return to the previous menu.
            buttons (list): List of buttons in the video settings menu.
            title (str): Title of the menu, set to "Video Settings".

        Methods:
            __init__(): Initialize the VideoMenu object.
            handle_events(event, screen, running):
                Handle events specific to the video settings menu.
        """

    def __init__(self):
        """
        Initialize the VideoMenu object.

        :rtype: object
        """
        super().__init__()

        self.resolution1_button = Button(Menu.WIDTH / 2 - (252 / 2), 200, 252, 74,
                                         "image/UI/Buttons/PlayText/Default@3x.png",
                                         "960x600", "image/UI/Buttons/PlayText/Hover@3x.png",
                                         "sound/knopka-schelchok.mp3")
        self.resolution2_button = Button(Menu.WIDTH / 2 - (252 / 2), 300, 252, 74,
                                         "image/UI/Buttons/PlayText/Default@3x.png",
                                         "1280x800", "image/UI/Buttons/PlayText/Hover@3x.png",
                                         "sound/knopka-schelchok.mp3")
        self.resolution3_button = Button(Menu.WIDTH / 2 - (252 / 2), 400, 252, 74,
                                         "image/UI/Buttons/PlayText/Default@3x.png",
                                         "Full screen", "image/UI/Buttons/PlayText/Hover@3x.png",
                                         "sound/knopka-schelchok.mp3")
        self.back_button = Button(self.WIDTH / 2 - (252 / 2), 500, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                  "Back", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.buttons = [self.resolution1_button, self.resolution2_button, self.resolution3_button, self.back_button]

        self.title = "Video Settings"

    def handle_events(self, event, screen, running):
        """
        Handle events for the video settings menu.

        :param event: The event to handle.
        :param screen: The screen surface to draw on.
        :param running: A list with a boolean indicating if the menu is running.
        :rtype: None
        """
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or
                event.type == pygame.USEREVENT and event.button == self.back_button):
            self.fade(screen)
            running[0] = False

        if event.type == pygame.USEREVENT:

            if event.button == self.resolution1_button:
                screen_obj.change_screen_size(960, 600)

            if event.button == self.resolution2_button:
                screen_obj.change_screen_size(1280, 800)

            if event.button == self.resolution3_button:
                screen_obj.change_screen_size(1920, 1080)

            self.fade(screen)
            Menu.check_size()


# {
#     name: str
#     returned: any
# }

class SelectorMenu(Menu):
    """
        SelectorMenu class represents a menu with selectable items.

        Attributes:
            can_move_buttons (bool): Flag indicating if buttons can be moved.
            title (str): Title of the menu.
            buttons (list): List of buttons in the menu.
            returned (list): List of returned values corresponding to each button.

        Methods:
            __init__(*args): Initialize the SelectorMenu object with a list of selectable items.
            handle_events(event, screen, running): Handle events specific to the selector menu.
            choice(screen): Display the choice menu and handle interaction.
        """

    def __init__(self, *args):
        """
        Initialize the SelectorMenu object with a list of selectable items.

        :param args: The list of selectable items.
        :rtype: object
        """
        super().__init__()

        self.can_move_buttons = False

        self.title = "Chose character"

        self.buttons = []
        self.returned = []

        y = 150
        for (i, obj) in enumerate(args):
            if i != 0 and i % 3 == 0:
                y += 230 * screen_obj.height_scale

            x = Menu.WIDTH / 3 * (i % 3) + 10 * screen_obj.width_scale

            width = Menu.WIDTH / 3 - 20 * screen_obj.width_scale
            height = 200 * screen_obj.height_scale

            self.buttons.append(Button(x, y, width, height, "image/UI/Buttons/PlayText/Default@3x.png", obj["name"],
                                       "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3"))

            self.returned.append(obj["returned"])

    def handle_events(self, event, screen, running):
        """
        Handle events for the selector menu.

        :param event: The event to handle.
        :param screen: The screen surface to draw on.
        :param running: A list with a boolean indicating if the menu is running.
        :rtype: object
        :return: The selected item, if any.
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.fade(screen)
            running[0] = False

        if event.type == pygame.USEREVENT:

            for (i, btn) in enumerate(self.buttons):
                if event.button == btn:
                    x = screen_obj.width // 2
                    y = screen_obj.height - 120 * screen_obj.height_scale

                    self.fade(screen)
                    return self.returned[i](x, y)

    def choice(self, screen):
        """
        Display the choice menu.

        :param screen: The screen surface to draw on.
        :rtype: object
        :return: The result of the menu interaction, if any.
        """
        return self.draw_menu(self, screen)


class SelectorCharacter(SelectorMenu):
    """
        SelectorCharacter class represents a menu for selecting character types.

        Attributes:
            Inherits attributes from SelectorMenu.

        Methods:
            __init__(): Initialize the SelectorCharacter object.
        """

    def __init__(self):
        """
        Initialize the SelectorCharacter object.

        :rtype: object
        """
        super().__init__(
            {"name": "Standard hero", "returned": StandardHero},
            {"name": "Fire Knight", "returned": FireKnight},
            {"name": "Wind Hashshin", "returned": WindHashahin},
            {"name": "Water Princess", "returned": WaterPrincess},
            {"name": "Leaf Ranger", "returned": LeafRanger},

        )

# можно переписать в клас не наследующий от меню но копирующий его и
# исполбзующий его статический метод
