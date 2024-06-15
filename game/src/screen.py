import pygame


class Screen:
    def __init__(self):
        """
        Initialize the Screen object with default width, height, and scaling factors.

        :rtype: object
        """
        self.width = 960
        self.height = 600
        self.width_scale = 1
        self.height_scale = 1
        self.screen = pygame.display.set_mode((self.width, self.height))

    def change_screen_size(self, width, height):
        """
        Change the size of the screen and adjust scaling factors accordingly.

        :param width: The new width of the screen.
        :param height: The new height of the screen.
        :rtype: None
        """
        self.width = width
        self.height = height
        if width != 960 and height != 600:
            self.width_scale = width / 960
            self.height_scale = height / 600
        else:
            self.width_scale = 1
            self.height_scale = 1

        if width == 1920 and height == 1080:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))


screen_obj = Screen()
