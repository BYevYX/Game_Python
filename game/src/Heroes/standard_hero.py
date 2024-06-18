"""
Module: game.src.Heroes.standard_hero

This module defines the StandardHero character class,
inheriting from Player, with specific attributes and animations.

Attributes:
- run (list): List of images for the standard hero's running animation.
- stay_images (list): List of images for the standard hero's idle animation.
- jump (list): List of images for the standard hero's jumping animation.
- attack_1 (list): List of images for the standard hero's attack animation.
- hp (int): Maximum health points of the standard hero.
- current_hp (int): Current health points of the standard hero.
- const_delay_animation (int): Animation delay for standard hero's general animations.
- const_delay_jump_animation (int): Animation delay for standard hero's jump animation.
- attack_range (float): Attack range of the standard hero.
- attack_damage (int): Damage inflicted by the standard hero's attacks.
- knockback (int): Knockback effect of the standard hero's attacks.
- rect (pygame.Rect): Rectangle representing the standard hero's position and size on screen.

Methods:
- __init__(self, x, y):
    Initializes the StandardHero with specific attributes and animations.

Usage:
from game.src.Heroes.standard_hero import StandardHero

# Example initialization of the StandardHero character
standard_hero = StandardHero(x=100, y=200)

Notes:
- This class assumes that the constants, Player class,
ImageCache, and screen_obj are correctly imported and initialized.
- Adjustments to image paths or scaling factors
in ImageCache.get_images calls should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src.Heroes.player import Player
from game.src.cache import ImageCache
from game.src import constants
from game.src.screen import screen_obj


class StandardHero(Player):
    """
        A class representing a standard hero character, inheriting from Player.

        Attributes:
            run (list): List of images for the standard hero's running animation.
            stay_images (list): List of images for the standard hero's idle animation.
            jump (list): List of images for the standard hero's jumping animation.
            attack_1 (list): List of images for the standard hero's attack animation.
            hp (int): Maximum health points of the standard hero.
            current_hp (int): Current health points of the standard hero.
            const_delay_animation (int): Animation delay for standard hero's general animations.
            const_delay_jump_animation (int): Animation delay for standard hero's jump animation.
            attack_range (float): Attack range of the standard hero.
            attack_damage (int): Damage inflicted by the standard hero's attacks.
            knockback (int): Knockback effect of the standard hero's attacks.
            rect (pygame.Rect):
                Rectangle representing the standard hero's position and size on screen.

        Methods:
            __init__(self, x, y):
                Initializes the StandardHero with specific attributes and animations.
        """

    def __init__(self, x, y):
        """
        Initialize the StandardHero with specific attributes and animations.

        :param x: The x-coordinate of the StandardHero's initial position.
        :param y: The y-coordinate of the StandardHero's initial position.
        :rtype: object
        """
        super().__init__(x, y)

        self.hp = constants.PLAYER_HP_COUNT - 1
        self.current_hp = self.hp

        self.const_delay_animation = 2
        self.const_delay_jump_animation = 5

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK

        run = [f"image/Heros/standard hero/Run/run-{i}.png" for i in range(1, 13)]
        self.run = ImageCache.get_images(run, (1.2, 1.2))

        stay = [f"image/Heros/standard hero/stay/idle-{i}.png" for i in range(1, 7)]
        self.stay_images = ImageCache.get_images(stay, (1.2, 1.2))

        jump = [f"image/Heros/standard hero/Jump/jump-{i}.png" for i in range(1, 15)]
        self.jump = ImageCache.get_images(jump, (1.2, 1.2))

        attack_1 = [f"image/Heros/standard hero/Attack/attack-A{i}.png" for i in range(1, 8)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.2, 1.2))

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))
