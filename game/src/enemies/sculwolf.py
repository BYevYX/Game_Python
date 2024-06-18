"""
Module: game.src.enemies.sculwolf

This module defines the Sculwolf class, representing a Sculwolf enemy in the game.

Attributes:
- images (list): List of movement animation images for the Sculwolf.
- death_images (list): List of death animation images for the Sculwolf.
- jump_height (int): Height of the jump movement for the Sculwolf.
- current_hp (int): Current hit points of the Sculwolf.
- const_delay_death_animation (int): Constant delay for death animation frames.
- const_delay_animation (int): Constant delay for regular animation frames.

Methods:
- __init__(self, x, y, range_place=100 * screen_obj.width_scale):
    Initializes the Sculwolf with specific attributes and animations.
- jump(self):
    Implements the jump movement for the Sculwolf based on animation frame count.
- move(self):
    Moves the Sculwolf and handles jump movement if applicable.

Usage:
from game.src.enemies.sculwolf import Sculwolf

# Example initialization of a Sculwolf enemy
sculwolf = Sculwolf(x=300, y=500)

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


class Sculwolf(CommonEnemy):
    """
    Class representing a Sculwolf enemy in the game.

    Attributes:
        images (list): List of movement animation images for the Sculwolf.
        death_images (list): List of death animation images for the Sculwolf.
        jump_height (int): Height of the jump movement for the Sculwolf.
        current_hp (int): Current hit points of the Sculwolf.
        const_delay_death_animation (int): Constant delay for death animation frames.
        const_delay_animation (int): Constant delay for regular animation frames.

    Methods:
        __init__(self, x, y, range_place=100 * screen_obj.width_scale):
            Initializes the Sculwolf with specific attributes and animations.

        jump(self):
            Implements the jump movement for the Sculwolf based on animation frame count.

        move(self):
            Moves the Sculwolf and handles jump movement if applicable.
    """

    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        """
        Initialize the Sculwolf with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the Sculwolf's initial position.
            y (int): The y-coordinate of the Sculwolf's initial position.
            range_place (int): The range in which the Sculwolf can move horizontally.
        """
        image_paths = [
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_1.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_2.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_3.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_4.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_5.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_6.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_7.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_8.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_9.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_10.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_11.png',
        ]

        death_paths = [
            'image/enemys/sculwolf/deth/Massacre death_1.png',
            'image/enemys/sculwolf/deth/Massacre death_2.png',
            'image/enemys/sculwolf/deth/Massacre death_3.png',
            'image/enemys/sculwolf/deth/Massacre death_4.png',
            'image/enemys/sculwolf/deth/Massacre death_5.png',
            'image/enemys/sculwolf/deth/Massacre death_6.png',
            'image/enemys/sculwolf/deth/Massacre death_7.png',
            'image/enemys/sculwolf/deth/Massacre death_8.png',
        ]

        self.images = ImageCache.get_images(image_paths)
        super().__init__(x, y - 30 * screen_obj.height_scale, range_place)

        self.jump_height = constants.ENEMY_JUMP_HEIGHT * screen_obj.height_scale
        self.death_images = ImageCache.get_images(death_paths)

        self.current_hp = 80
        self.const_delay_death_animation = 1
        self.const_delay_animation = 1

    def jump(self):
        """
        Implements the jump movement for the Sculwolf based on animation frame count.

        Adjusts the y-coordinate of the Sculwolf's bounding rectangle to simulate a jumping motion.
        """
        if 7 <= self.animation_count <= 9:
            self.rect.y -= self.jump_height
        elif 0 <= self.animation_count <= 1 or self.animation_count == 10:
            self.rect.y += self.jump_height

    def move(self):
        """
        Moves the Sculwolf and handles jump movement if applicable.

        Overrides the move method from the base class CommonEnemy.
        """
        super().move()
        self.jump()
