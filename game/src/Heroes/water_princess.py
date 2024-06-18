"""
Module: game.src.Heroes.water_princess

This module defines the WaterPrincess character class,
inheriting from SuperPlayer, with specific attributes and animations.

Attributes:
- run (list): List of images for running animation.
- stay_images (list): List of images for idle animation.
- jump (list): List of images for jumping animation.
- attack_1 (list): List of images for attack animation.
- ability_images (list): List of images for the WaterPrincess's ability animation.
- ulta_images (list): List of images for the WaterPrincess's ultimate attack animation.
- hp (int): The health points of the WaterPrincess character.
- current_hp (int): The current health points of the WaterPrincess character.
- const_delay_animation (int): Constant delay for animations.
- const_delay_jump_animation (int): Constant delay for jump animations.
- attack_range (float): Attack range of the WaterPrincess character.
- attack_damage (int): Damage inflicted by the WaterPrincess character's attacks.
- knockback (int): Knockback effect of the WaterPrincess character's attacks.

Methods:
- __init__(self, x, y):
    Initializes the WaterPrincess character with specific attributes and animations.

- ability(self, game, *args):
    Perform the WaterPrincess's ability, which heals her if her current HP is below her maximum HP.

Usage:
from game.src.Heroes.water_princess import WaterPrincess

# Example initialization of the WaterPrincess character
water_princess = WaterPrincess(x=150, y=250)

Notes:
- This class assumes that the constants, ImageCache,
SuperPlayer class, and screen_obj are correctly imported and initialized.
- Adjustments to image paths or scaling factors
in ImageCache.get_images calls should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""

from game.src import constants
from game.src.Heroes.super_player import SuperPlayer
from game.src.cache import ImageCache
from game.src.screen import screen_obj


class WaterPrincess(SuperPlayer):
    """
    A class representing the WaterPrincess character, inheriting from SuperPlayer.

    Attributes:
        run (list): List of images for running animation.
        stay_images (list): List of images for idle animation.
        jump (list): List of images for jumping animation.
        attack_1 (list): List of images for attack animation.
        ability_images (list): List of images for the WaterPrincess's ability animation.
        ulta_images (list): List of images for the WaterPrincess's ultimate attack animation.
        hp (int): The health points of the WaterPrincess character.
        current_hp (int): The current health points of the WaterPrincess character.
        const_delay_animation (int): Constant delay for animations.
        const_delay_jump_animation (int): Constant delay for jump animations.
        attack_range (float): Attack range of the WaterPrincess character.
        attack_damage (int): Damage inflicted by the WaterPrincess character's attacks.
        knockback (int): Knockback effect of the WaterPrincess character's attacks.

    Methods:
        __init__(self, x, y):
            Initializes the WaterPrincess character with specific attributes and animations.

        ability(self, game, *args):
            Perform the WaterPrincess's ability,
            which heals her if her current HP is below her maximum HP.
    """

    def __init__(self, x, y):
        """
        Initialize the WaterPrincess character with specific attributes and animations.

        :param x: The x-coordinate of the WaterPrincess's initial position.
        :param y: The y-coordinate of the WaterPrincess's initial position.
        :rtype: object
        """
        run = [f"image/Heros/water_princess/02_walk/walk_{i}.png" for i in range(1, 11)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/water_princess/01_idle/idle_{i}.png" for i in range(1, 9)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = ([f"image/Heros/water_princess/04_jump/j_up_{i}.png" for i in range(1, 4)] +
                [f"image/Heros/water_princess/04_jump/j_down_{i}.png" for i in range(1, 4)])
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/water_princess/07_1_atk/1_atk_{i}.png" for i in range(1, 8)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        ability_images_paths = [f'image/Heros/water_princess/11_heal/heal_{i}.png' for i in range(1, 13)]
        self.ability_images = ImageCache.get_images(ability_images_paths, (1.5, 1.5))

        ulta_images_paths = [f'image/Heros/water_princess/10_sp_atk/sp_atk_{i}.png' for i in range(1, 33)]
        self.ulta_images = ImageCache.get_images(ulta_images_paths, (1.5, 1.5))

        super().__init__(x, y, 50, 50)

        self.hp = constants.PLAYER_HP_COUNT - 2
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 11

        self.attack_range = constants.PLAYER_ATTACK_RANGE * 1.3 * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK + 10

    def ability(self, game, *args):
        """
        Perform the WaterPrincess's ability, which heals her
        if her current HP is below her maximum HP.

        :param game: The game context in which the ability is used.
        :param args: Additional arguments for the ability.
        :rtype: None
        """
        if self.current_hp < self.hp:
            self.current_hp += 1
