import pygame
import sys
from game.src.button import Button
from game.src.screen import screen_obj
import game.src.constants as constants
from game.src.game_start import GameOn


class Menu:

    def __init__(self):

        self.MAX_FPS = constants.MAX_FPS
        self.clock = pygame.time.Clock()
        self.cursor = pygame.image.load("image/UI/cursor/cursor.png").convert_alpha()

    WIDTH = screen_obj.width
    HEIGHT = screen_obj.height
    main_background = pygame.transform.scale(pygame.image.load("image/UI/Panel/Window/Big.png").convert_alpha(), (WIDTH, HEIGHT))

    @staticmethod
    def draw_menu(menu_obj, screen):

        pygame.mouse.set_visible(False)

        running = [True]
        while running[0]:
            screen.fill((0, 0, 0))
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

                menu_obj.handle_events(event, screen, running)

                for btn in menu_obj.buttons:
                    btn.handle_event(event)

            for btn in menu_obj.buttons:
                btn.set_pos((Menu.WIDTH - 252) / 2)
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            screen.blit(menu_obj.cursor, pygame.mouse.get_pos())

            pygame.display.flip()

    def fade(self, screen):

        running = True
        fade_alpha = 0  # уровень прозрачности

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
        if Menu.WIDTH != screen_obj.width:
            Menu.WIDTH = screen_obj.width
            Menu.HEIGHT = screen_obj.height
            Menu.main_background = pygame.transform.scale(Menu.main_background, (Menu.WIDTH, Menu.HEIGHT))


class MainMenu(Menu):

    def __init__(self):
        super().__init__()

        self.start_button = Button(Menu.WIDTH / 2 - (252 / 2), 200, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                   "Play", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.settings_button = Button(Menu.WIDTH / 2 - (252 / 2), 300, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                      "Settings", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.exit_button = Button(Menu.WIDTH / 2 - (252 / 2), 400, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                  "Exit", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.buttons = [self.start_button, self.settings_button, self.exit_button]

        self.title = "Menu"

        self.settings_menu = SettingsMenu()

    def handle_events(self, event, screen, running):

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

                game = GameOn()
                game.start(screen)



class SettingsMenu(Menu):

    def __init__(self):
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

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or
           event.type == pygame.USEREVENT and event.button == self.back_button):
            self.fade(screen)
            running[0] = False

        if event.type == pygame.USEREVENT and event.button == self.video_button:
            self.fade(screen)
            Menu.draw_menu(self.video_menu, screen)


class VideoMenu(Menu):

    def __init__(self):
        super().__init__()

        self.resolution1_button = Button(Menu.WIDTH / 2 - (252 / 2), 200, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                         "960x600", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.resolution2_button = Button(Menu.WIDTH / 2 - (252 / 2), 300, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                         "1280x800", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.resolution3_button = Button(Menu.WIDTH / 2 - (252 / 2), 400, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                         "Full screen", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.back_button = Button(self.WIDTH / 2 - (252 / 2), 500, 252, 74, "image/UI/Buttons/PlayText/Default@3x.png",
                                  "Back", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")
        self.buttons = [self.resolution1_button, self.resolution2_button, self.resolution3_button, self.back_button]

        self.title = "Video Settings"

    def handle_events(self, event, screen, running):

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
