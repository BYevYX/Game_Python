"""
Module: game.src.enemies.satyr

This module defines the Satyr class, representing a Satyr enemy in the game.

Attributes:
- images (list): List of movement animation images for the Satyr.
- death_images (list): List of death animation images for the Satyr.
- current_hp (int): Current hit points of the Satyr.
- const_delay_death_animation (int): Constant delay for death animation frames.
- const_delay_animation (int): Constant delay for regular animation frames.
- speed (float): Speed of movement for the Satyr.

Methods:
- __init__(self, x, y, range_place=100 * screen_obj.width_scale):
    Initializes the Satyr with specific attributes and animations.
- move(self):
    Moves the Satyr horizontally based on its speed.
- die(self):
    Initiates the death animation sequence for the Satyr.

Usage:
from game.src.enemies.satyr import Satyr

# Example initialization of a Satyr enemy
satyr = Satyr(x=400, y=600)

Notes:
- This class assumes that constants, pygame,
ImageCache, CommonEnemy, and other necessary modules are correctly imported and initialized.
- Adjustments to image paths, scaling factors,
and game mechanics should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src import constants
from game.src.cache import ImageCache
from game.src.enemies.enemies_base import CommonEnemy
from game.src.screen import screen_obj


class Satyr(CommonEnemy):
    """
    Class representing a Satyr enemy in the game.

    Attributes:
        images (list): List of movement animation images for the Satyr.
        death_images (list): List of death animation images for the Satyr.
        current_hp (int): Current hit points of the Satyr.
        const_delay_death_animation (int): Constant delay for death animation frames.
        const_delay_animation (int): Constant delay for regular animation frames.
        speed (float): Speed of movement for the Satyr.

    Methods:
        __init__(self, x, y, range_place=100 * screen_obj.width_scale):
            Initializes the Satyr with specific attributes and animations.

        move(self):
            Moves the Satyr horizontally based on its speed.

        die(self):
            Initiates the death animation sequence for the Satyr.
    """

    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        """
        Initialize the Satyr with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the Satyr's initial position.
            y (int): The y-coordinate of the Satyr's initial position.
            range_place (int): The range in which the Satyr can move horizontally.
        """
        image_paths = [
            'image/enemys/satyr/move/satyr-Sheet_1.png',
            'image/enemys/satyr/move/satyr-Sheet_2.png',
            'image/enemys/satyr/move/satyr-Sheet_3.png',
            'image/enemys/satyr/move/satyr-Sheet_4.png',
            'image/enemys/satyr/move/satyr-Sheet_5.png',
            'image/enemys/satyr/move/satyr-Sheet_6.png',
            'image/enemys/satyr/move/satyr-Sheet_7.png',
            'image/enemys/satyr/move/satyr-Sheet_8.png',
            'image/enemys/satyr/move/satyr-Sheet_9.png',
            'image/enemys/satyr/move/satyr-Sheet_10.png',
            'image/enemys/satyr/move/satyr-Sheet_11.png',
            'image/enemys/satyr/move/satyr-Sheet_12.png',
            'image/enemys/satyr/move/satyr-Sheet_13.png',
            'image/enemys/satyr/move/satyr-Sheet_14.png',
            'image/enemys/satyr/move/satyr-Sheet_15.png',
            'image/enemys/satyr/move/satyr-Sheet_16.png',
            'image/enemys/satyr/move/satyr-Sheet_17.png',
            'image/enemys/satyr/move/satyr-Sheet_18.png',
            'image/enemys/satyr/move/satyr-Sheet_19.png',
            'image/enemys/satyr/move/satyr-Sheet_20.png',
            'image/enemys/satyr/move/satyr-Sheet_21.png',
        ]

        death_paths = [
            'image/enemys/satyr/depth/satyr death_1.png',
            'image/enemys/satyr/depth/satyr death_2.png',
            'image/enemys/satyr/depth/satyr death_3.png',
            'image/enemys/satyr/depth/satyr death_4.png',
            'image/enemys/satyr/depth/satyr death_5.png',
            'image/enemys/satyr/depth/satyr death_6.png',
            'image/enemys/satyr/depth/satyr death_7.png',
            'image/enemys/satyr/depth/satyr death_8.png',
            'image/enemys/satyr/depth/satyr death_9.png',
        ]

        self.images = ImageCache.get_images(image_paths, (2, 2))
        super().__init__(x, y - 40 * screen_obj.height_scale, range_place)

        self.death_images = ImageCache.get_images(death_paths, (2, 2))
        self.current_hp = 100
        self.const_delay_death_animation = 2
        self.const_delay_animation = 2
        self.speed = (constants.ENEMY_NORMAL_SPEED - 1) * screen_obj.width_scale
