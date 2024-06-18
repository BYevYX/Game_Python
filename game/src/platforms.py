"""
Module defining classes for platform objects in a Pygame-based game.

Classes:
- Platform: Represents static platforms in the game.
- MovingPlatform:
    Subclass of Platform, represents platforms that can slide horizontally or vertically.

Attributes and Methods:
- Platform:
  Attributes:
  - image: Surface object representing the platform's image.
  - rect: Rect object representing the position and size of the platform.
  - velocity: Horizontal movement speed of the platform.
  - direction: Direction of movement ('right' or 'left').

  Methods:
  - __init__(self, x, y, width, height, image_type="main_platform"): Initializes a Platform object.
  - move_platform(self, direction): Moves the platform horizontally in the specified direction.

- MovingPlatform:
  Attributes:
  - up: Upper bound for sliding.
  - to: Lower bound for sliding.
  - slide_direction: Direction of sliding ('x' or 'y').
  - slide_velocity: Speed of sliding movement.

  Methods:
  - __init__(self, x, y, width, height, up, to, slide_direction='x', image_type="moving_platform"):
    Initializes a MovingPlatform object.
  - slide(self):
      Slides the platform within specified bounds based on slide_direction.
  - move_platform(self, direction):
      Moves the platform horizontally in the specified direction and adjusts slide bounds.

This module provides definitions for
both static and moving platforms used within the game environment,
allowing for varied platform behaviors and appearances based on specified parameters.
"""

from game.src import constants
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import pygame

# from random import randint


class Platform(pygame.sprite.Sprite):
    """
    A class representing platforms in a Pygame-based game.

    Attributes:
    - image: Surface object representing the platform's image.
    - rect: Rect object representing the position and size of the platform.
    - velocity: Horizontal movement speed of the platform.
    - direction: Direction of movement ('right' or 'left').

    Methods:
    - __init__(self, x, y, width, height, image_type="main_platform"): 
        Initializes the Platform object.
    - move_platform(self, direction): Moves the platform horizontally in the specified direction.
    """

    def __init__(self, x, y, width, height, image_type="main_platform"):
        """
        Initialize the Platform object.

        :param x: Initial x-coordinate of the platform.
        :param y: Initial y-coordinate of the platform.
        :param width: Width of the platform.
        :param height: Height of the platform.
        :param image_type: Type of image to use for the platform.
        :rtype: object
        """
        super().__init__()

        platform_images = {
            "main_platform": "image/locations/platforms/big platform.png",
            "left_wall": "image/locations/platforms/left_wall.png",
            "right_wall": "image/locations/platforms/right_wall.png",
            "moving_platform": "image/locations/platforms/moving_platform.png",
            "mountain": "image/locations/obstacles/big_mountain.png",
            "gate": "image/locations/obstacles/gate.png",
        }

        image = ImageCache.get_images([platform_images[image_type]])
        self.image = pygame.transform.scale(image[0], (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = constants.VELOCITY * screen_obj.width_scale
        self.direction = "right"

    def move_platform(self, direction):
        """
        Move the platform in the specified direction.

        :param direction: The direction to move the platform.
        :rtype: object
        """
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

        self.rect.x += self.velocity


class MovingPlatform(Platform):
    """
    Class:
    MovingPlatform:
    Attributes:
    - up: Upper bound for sliding.
    - to: Lower bound for sliding.
    - slide_direction: Direction of sliding ('x' or 'y').
    - slide_velocity: Speed of sliding movement.

    Methods:
    - __init__(self, x, y, width, height, up, to, slide_direction='x',
               image_type="moving_platform"):
    Initializes the MovingPlatform object.
    - slide(self): Slides the platform within specified bounds based on slide_direction.
    - move_platform(self, direction):
        Moves the platform horizontally in the specified direction and adjusts slide bounds.

    This docstring provides an overview of the `Platform` class and its `MovingPlatform` subclass,
    describing their attributes and methods for clarity and reference.
    """

    def __init__(self, x, y, width, height, up, to, slide_direction='x',
                 image_type="moving_platform"):
        """
        Initialize the MovingPlatform object.

        :param x: Initial x-coordinate of the moving platform.
        :param y: Initial y-coordinate of the moving platform.
        :param width: Width of the moving platform.
        :param height: Height of the moving platform.
        :param up: The upper bound for sliding.
        :param to: The lower bound for sliding.
        :param slide_direction: The direction of sliding ('x' or 'y').
        :param image_type: Type of image to use for the moving platform.
        :rtype: _SpriteSupportsGroup
        """
        super().__init__(x, y, width, height, image_type)

        self.up = up
        self.to = to
        self.slide_direction = slide_direction
        self.slide_velocity = constants.VELOCITY // 2

    def slide(self):
        """
        Slide the moving platform in the specified direction.

        :rtype: None
        """
        if self.slide_direction == 'x':
            self.rect.x += self.slide_velocity
            if self.rect.right > max(self.to, self.up) or self.rect.left < min(self.up, self.to):
                self.slide_velocity *= -1

        elif self.slide_direction == 'y':
            self.rect.y += self.slide_velocity
            if self.rect.top > max(self.to, self.up) or self.rect.bottom < min(self.up, self.to):
                self.slide_velocity *= -1

    def move_platform(self, direction):
        """
        Move the platform in the specified direction and adjust bounds for sliding.

        :param direction: The direction to move the platform.
        :rtype: None
        """
        super().move_platform(direction)

        if self.slide_direction == 'x':
            self.up += self.velocity
            self.to += self.velocity

    # @staticmethod
    # def grouper_random(levels, group=None):
    #     platforms = pygame.sprite.Group()
    #     if group:
    #         platforms.add(group)
    #
    #     for x in range(0, screen_obj.width, 300):
    #         platforms.add(Platform(x, screen_obj.height - 40, 300, 40))
    #
    #     for i in range(levels):
    #         for j in range(0, screen_obj.width, 330):
    #             platforms.add(Platform(j + randint(-70, 70),
    #                           (i + 0.7) * randint(130, 140), 20 * randint(9, 10), 30))
    #
    #
    #     return platforms
