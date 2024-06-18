"""
This module provides classes for
managing backgrounds and partial backgrounds in a game using Pygame.

Classes:
- Locations:
    Represents a location in the game with multiple background layers and associated sound.

    Attributes:
    - backgrounds (list): List of background images and their x-coordinate.
    - background_speed (float): Speed at which the backgrounds move.
    - sound (pygame.mixer.Sound): Sound object for the location.

    Methods:
    - __init__(background_paths, sound_path, scale):
        Initializes the Locations object with background images and sound.
    - draw_background(screen):
        Draws the location's background on the screen.
    - move_background(direction):
        Moves the background layers in the specified direction ('right' or 'left').

- PartialBackground:
    Represents a single moving background image in the game.

    Attributes:
    - background (pygame.Surface): Surface of the partial background image.
    - x (int): X-coordinate of the background's position.
    - y (int): Y-coordinate of the background's position.
    - background_speed (float): Speed at which the background moves.

    Methods:
    - __init__(x, y, width, height, image_name="brick_wall"):
        Initializes the PartialBackground object with specific coordinates, size, and image name.
    - draw(screen):
        Draws the partial background on the screen.
    - move_background(direction):
        Moves the partial background in the specified direction ('right' or 'left').

Dependencies:
- From game.src:
  - constants: Constants used for defining speeds and paths.
  - cache.ImageCache: Cache mechanism for managing and loading images.
  - screen.screen_obj: Screen object containing screen dimensions and scales.
- External dependencies:
  - pygame: Main library for game development in Python with multimedia capabilities.
  - pygame.mixer: Module for handling sound playback.

"""

# Import statements for game dependencies (constants, cache.ImageCache, screen.screen_obj, pygame)

from game.src import constants
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import pygame

pygame.mixer.init()


class Locations:
    """
    Locations class handles the backgrounds and sound for a location in the game.

    Attributes:
        backgrounds (list): List of background images and their x-coordinate.
        background_speed (float): Speed at which the backgrounds move.
        sound (pygame.mixer.Sound): Sound object for the location.

    Methods:
        __init__(background_paths, sound_path, scale): Initializes the Locations object.
        draw_background(screen): Draws the background on the screen.
        move_background(direction): Moves the background in the specified direction.
    """

    def __init__(self, background_paths, sound_path, scale):
        """
        Initialize the Locations object.

        :param background_paths: List of paths to background images.
        :param sound_path: Path to the sound file for the location.
        :param scale: Tuple containing the width and height to scale the backgrounds to.
        """
        self.backgrounds = \
            [[pygame.transform.scale(pygame.image.load(background_path).convert_alpha(), scale), 0]
             for background_path in background_paths]

        self.background_speed = constants.BACKGROUND_SPEED * screen_obj.width_scale

        self.sound = pygame.mixer.Sound(sound_path)

    def draw_background(self, screen):
        """
        Draw the background on the screen.

        :param screen: The screen surface to draw on.
        """
        for background in self.backgrounds:
            screen.blit(background[0], (background[1], 0))
            screen.blit(background[0], (background[1] + screen_obj.width, 0))
            screen.blit(background[0], (background[1] - screen_obj.width, 0))

    def move_background(self, direction):
        """
        Move the background in the specified direction.

        :param direction: The direction to move the background ('right' or 'left').
        """
        if direction == 'right':
            self.background_speed = -constants.BACKGROUND_SPEED * screen_obj.width_scale
        elif direction == 'left':
            self.background_speed = constants.BACKGROUND_SPEED * screen_obj.width_scale

        for i, background in enumerate(self.backgrounds):
            if background[1] <= -screen_obj.width or background[1] >= screen_obj.width:
                background[1] = 0

            background[1] += self.background_speed * i


class PartialBackground:
    """
    PartialBackground class represents a background image that can move in the game.

    Attributes:
        background (pygame.Surface): Surface of the partial background image.
        x (int): X-coordinate of the background's position.
        y (int): Y-coordinate of the background's position.
        background_speed (float): Speed at which the background moves.

    Methods:
        __init__(x, y, width, height, image_name="brick_wall"):
            Initializes the PartialBackground object.
        draw(screen): Draws the partial background on the screen.
        move_background(direction): Moves the partial background in the specified direction.
    """

    def __init__(self, x, y, width, height, image_name="brick_wall"):
        """
        Initialize the PartialBackground object.

        :param x: The x-coordinate of the background's position.
        :param y: The y-coordinate of the background's position.
        :param width: The width to scale the background to.
        :param height:
            The height to scale the background to.
        :param image_name:
            The name of the image to use for the background (default is "brick_wall").
        """
        bases_image_paths = {
            "brick_wall": "image/locations/backgrounds/brick background.png",
            "brown_brick_wall": "image/locations/backgrounds/brick background with brown.png",
            "house_roof": "image/locations/house/house_roof.png",
            "house_tube": "image/locations/house/house_tube.png",
            "house_wall": "image/locations/house/house_wall.png",
            "house_enter": "image/locations/house/house_wood_entrance.png",
            "big_tree": "image/locations/decorations/big_tree.png",
            "collumn_back": "image/locations/backgrounds/collumn_background.png",
        }

        image = ImageCache.get_images([bases_image_paths[image_name]])

        self.background = pygame.transform.scale(image[0], (width, height))
        self.x = x
        self.y = y
        self.background_speed = constants.PARTIAL_BACKGROUND_SPEED * screen_obj.width_scale

    def draw(self, screen):
        """
        Draw the partial background on the screen.

        :param screen: The screen surface to draw on.
        """
        screen.blit(self.background, (self.x, self.y))

    def move_background(self, direction):
        """
        Move the partial background in the specified direction.

        :param direction: The direction to move the background ('right' or 'left').
        """
        if direction == 'right':
            self.x += -self.background_speed
        elif direction == 'left':
            self.x += self.background_speed
