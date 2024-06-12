import pygame


class Screen:
    def __init__(self):
        self.width = 960
        self.height = 600
        self.width_scale = 1
        self.height_scale = 1
        self.screen = pygame.display.set_mode((self.width, self.height))

    def change_screen_size(self, width, height):
        self.width = width
        self.height = height
        if width != 960 and height != 600:
            self.width_scale = width / 960  # * 0.9
            self.height_scale = height / 600  # * 0.9
        else:
            self.width_scale = 1
            self.height_scale = 1

        if width == 1920 and height == 1080:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))


screen_obj = Screen()
