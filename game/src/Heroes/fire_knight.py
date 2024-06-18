"""
Module: game.src.Heroes.fire_knight

This module defines the FireKnight class, which represents a character inheriting from Player.

Attributes:
- run (list): List of running animation images for the Fire Knight.
- stay_images (list): List of idle (standing) animation images for the Fire Knight.
- jump (list): List of jumping animation images for the Fire Knight.
- attack_1 (list): List of primary attack animation images for the Fire Knight.
- hp (int): Hit points (health) of the Fire Knight.
- current_hp (int): Current hit points (health) of the Fire Knight.
- const_delay_animation (int): Constant delay between animation frames for the Fire Knight.
- const_delay_jump_animation (int):
    Constant delay between jump animation frames for the Fire Knight.
- attack_range (float): Range of the Fire Knight's attack.
- attack_damage (int): Damage inflicted by the Fire Knight's attack.
- knockback (int): Knockback effect on enemies when hit by the Fire Knight.
- rect (pygame.Rect): Rectangle representing the Fire Knight's position and size.

Methods:
- __init__(self, x, y):
    Initializes the Fire Knight with specific attributes and animations.
- check_animation_count(self):
    Checks and updates the animation count, and adjusts position during attack animations.

Usage:
from game.src.Heroes.fire_knight import FireKnight

# Example initialization of the Fire Knight character
fire_knight = FireKnight(x=150, y=300)

Notes:
- This class assumes that constants, pygame,
ImageCache, Player, and other necessary modules are correctly imported and initialized.
- Adjustments to image paths, scaling factors,
and game mechanics should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src import constants
from game.src.Heroes.player import Player
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import pygame


class FireKnight(Player):
    """
    Class representing the Fire Knight character, inheriting from Player.

    Attributes:
        run (list): List of running animation images.
        stay_images (list): List of idle (standing) animation images.
        jump (list): List of jumping animation images.
        attack_1 (list): List of primary attack animation images.
        hp (int): Hit points (health) of the Fire Knight.
        current_hp (int): Current hit points (health) of the Fire Knight.
        const_delay_animation (int): Constant delay between animation frames.
        const_delay_jump_animation (int): Constant delay between jump animation frames.
        attack_range (float): Range of the Fire Knight's attack.
        attack_damage (int): Damage inflicted by the Fire Knight's attack.
        knockback (int): Knockback effect on enemies when hit by the Fire Knight.
        rect (pygame.Rect): Rectangle representing the Fire Knight's position and size.

    Methods:
        __init__(self, x, y):
            Initializes the FireKnight with specific attributes and animations.

        check_animation_count(self):
            Checks and updates the animation count, and adjusts position during attack animations.
    """

    def __init__(self, x, y):
        """
        Initialize the Fire Knight with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the Fire Knight's initial position.
            y (int): The y-coordinate of the Fire Knight's initial position.
        """
        super().__init__(x, y)

        self.hp = constants.PLAYER_HP_COUNT
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 4

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK - 10

        run = [f"image/Heros/Fire-knight/02_run/run_{i}.png" for i in range(1, 9)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/Fire-knight/01_idle/idle_{i}.png" for i in range(1, 9)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = [f"image/Heros/Fire-knight/03_jump/jump_{i}.png" for i in range(1, 21)]
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/Fire-knight/05_1_atk/1_atk_{i}.png" for i in range(1, 12)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

    def check_animation_count(self):
        """
        Check and update the animation count, and adjust position during attack animations.

        Overrides the base class method to add specific behavior for
        Fire Knight's attack animations.
        """
        super().check_animation_count()

        if self.delay_animation == 0:
            if self.attack_animation_count == 3:
                self.y -= 60
            elif self.attack_animation_count == 7:
                self.y += 60
                