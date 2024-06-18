"""
Module defining the Screen class for managing the display surface in a Pygame-based game.

Classes:
- Screen: Manages screen configuration, size adjustments, and scaling factors.

Attributes and Methods of Screen class:
Attributes:
- width: Width of the screen.
- height: Height of the screen.
- width_scale: Scaling factor for width relative to a default width of 960.
- height_scale: Scaling factor for height relative to a default height of 600.
- screen: Pygame display surface representing the game screen.

Methods:
- __init__(self):
    Initializes the Screen object with default width, height, and creates a Pygame display surface.
- change_screen_size(self, width, height):
    Changes the size of the screen and adjusts scaling factors accordingly.

Usage:
Create an instance of Screen using Screen() to manage and adjust the game screen size and scaling.

Note: Requires the pygame library for display management.
"""

import pygame


class Screen:
    """
    A class representing the screen configuration and management for a Pygame-based game.

    Attributes:
    - width: Width of the screen.
    - height: Height of the screen.
    - width_scale: Scaling factor for width relative to a default width of 960.
    - height_scale: Scaling factor for height relative to a default height of 600.
    - screen: Pygame display surface representing the game screen.

    Methods:
    - __init__(self): Initializes the Screen object with default width, height,
    and creates a Pygame display surface.
    - change_screen_size(self, width, height):
        Changes the size of the screen and adjusts scaling factors accordingly.
    """

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
