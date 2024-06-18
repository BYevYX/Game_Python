"""
Module: game.src.Heroes.wind_hashahin

This module defines the WindHashahin character class,
inheriting from Player, with specific attributes and animations.

Attributes:
- hp (int): The health points of the WindHashahin character.
- current_hp (int): The current health points of the WindHashahin character.
- const_delay_animation (int): Constant delay for animations.
- const_delay_jump_animation (int): Constant delay for jump animations.
- attack_range (float): Attack range of the WindHashahin character.
- attack_damage (int): Damage inflicted by the WindHashahin character's attacks.
- knockback (int): Knockback effect of the WindHashahin character's attacks.
- run (list): List of images for running animation.
- stay_images (list): List of images for idle animation.
- jump (list): List of images for jumping animation.
- attack_1 (list): List of images for attack animation.
- rect (Rect): Rectangle representing the position and size of the character on the screen.

Methods:
- __init__(self, x, y):
    Initializes the WindHashahin character with specific attributes and animations.

Usage:
from game.src.Heroes.wind_hashahin import WindHashahin

# Example initialization of the WindHashahin character
wind_hashahin = WindHashahin(x=100, y=200)

Notes:
- This class assumes that the constants, ImageCache,
Player class, and screen_obj are correctly imported and initialized.
- Adjustments to image paths or scaling factors
in ImageCache.get_images calls should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src import constants
from game.src.Heroes.player import Player
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import pygame


class WindHashahin(Player):
    """
        A class representing the WindHashahin character, inheriting from Player.

        Attributes:
            hp (int): The health points of the WindHashahin character.
            current_hp (int): The current health points of the WindHashahin character.
            const_delay_animation (int): Constant delay for animations.
            const_delay_jump_animation (int): Constant delay for jump animations.
            attack_range (float): Attack range of the WindHashahin character.
            attack_damage (int): Damage inflicted by the WindHashahin character's attacks.
            knockback (int): Knockback effect of the WindHashahin character's attacks.
            run (list): List of images for running animation.
            stay_images (list): List of images for idle animation.
            jump (list): List of images for jumping animation.
            attack_1 (list): List of images for attack animation.
            rect (Rect):
                Rectangle representing the position and size of the character on the screen.

        Methods:
            __init__(self, x, y):
                Initializes the WindHashahin character with specific attributes and animations.
        """

    def __init__(self, x, y):
        """
        Initialize the WindHashahin character with specific attributes and animations.

        :param x: The x-coordinate of the WindHashahin's initial position.
        :param y: The y-coordinate of the WindHashahin's initial position.
        :rtype: object
        """
        super().__init__(x, y)

        self.hp = constants.PLAYER_HP_COUNT - 1
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 10

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK + 10

        run = [f"image/Heros/Wind_hashahin/run/run_{i}.png" for i in range(1, 9)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/Wind_hashahin/idle/idle_{i}.png" for i in range(1, 9)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = ([f"image/Heros/Wind_hashahin/jump/j_up_{i}.png" for i in range(1, 4)] +
                [f"image/Heros/Wind_hashahin/jump/j_down_{i}.png" for i in range(1, 4)])
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/Wind_hashahin/1_atk/1_atk_{i}.png" for i in range(1, 9)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.rect.width - 30 * screen_obj.width_scale, self.rect.height)
