"""
Module: game.src.Heroes.leaf_ranger

This module defines the LeafRanger class, which represents a character inheriting from SuperPlayer.

Attributes:
- run (list): List of running animation images for the Leaf Ranger.
- stay_images (list): List of idle (standing) animation images for the Leaf Ranger.
- jump (list): List of jumping animation images for the Leaf Ranger.
- attack_1 (list): List of primary attack animation images for the Leaf Ranger.
- ulta_images (list): List of ultimate attack animation images for the Leaf Ranger.
- ability_images (list): List of ability attack animation images for the Leaf Ranger.
- hp (int): Hit points (health) of the Leaf Ranger.
- current_hp (int): Current hit points (health) of the Leaf Ranger.
- const_delay_animation (int): Constant delay between animation frames for the Leaf Ranger.
- const_delay_jump_animation (int):
    Constant delay between jump animation frames for the Leaf Ranger.
- attack_range (float): Range of the Leaf Ranger's normal attack.
- ulta_range (float): Range of the Leaf Ranger's ultimate attack.
- attack_damage (int): Damage inflicted by the Leaf Ranger's attack.
- knockback (int): Knockback effect on enemies when hit by the Leaf Ranger.
- arrows (pygame.sprite.Group): Group containing Arrow sprites for the Leaf Ranger.
- create_arrow (bool): Flag indicating if an arrow should be created by the Leaf Ranger.
- can_use_ability_flying (bool):
    Flag indicating if the ability can be used while the Leaf Ranger is flying.

Methods:
- __init__(self, x, y):
    Initializes the Leaf Ranger with specific attributes and animations.
- ability(self, game, *args):
    Executes the Leaf Ranger's ability action.
- move_environment(direction, game):
    Moves the environment based on the player's movement direction.
- update(self, screen, game):
    Updates the Leaf Ranger's state and actions.

Usage:
from game.src.Heroes.leaf_ranger import LeafRanger

# Example initialization of the Leaf Ranger character
leaf_ranger = LeafRanger(x=150, y=300)

Notes:
- This class assumes that constants, pygame, ImageCache,
Shockwave, SuperPlayer, and other necessary modules are correctly imported and initialized.
- Adjustments to image paths, scaling factors,
and game mechanics should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src import constants
from game.src.Heroes.super_player import SuperPlayer
from game.src.cache import ImageCache
from game.src.screen import screen_obj
from game.src.shokwave import Shockwave
import pygame.sprite


class LeafRanger(SuperPlayer):
    """
    Class representing the Leaf Ranger character, inheriting from SuperPlayer.

    Attributes:
        run (list): List of running animation images.
        stay_images (list): List of idle (standing) animation images.
        jump (list): List of jumping animation images.
        attack_1 (list): List of primary attack animation images.
        ulta_images (list): List of ultimate attack animation images.
        ability_images (list): List of ability attack animation images.
        hp (int): Hit points (health) of the Leaf Ranger.
        current_hp (int): Current hit points (health) of the Leaf Ranger.
        const_delay_animation (int):
            Constant delay between animation frames.
        const_delay_jump_animation (int): Constant delay between jump animation frames.
        attack_range (float): Range of the Leaf Ranger's attack.
        attack_damage (int): Damage inflicted by the Leaf Ranger's attack.
        knockback (int): Knockback effect on enemies when hit by the Leaf Ranger.
        arrows (pygame.sprite.Group): Group containing Arrow sprites.
        create_arrow (bool): Flag indicating if an arrow should be created.
        can_use_ability_flying (bool): Flag indicating if ability can be used while flying.

    Methods:
        __init__(self, x, y):
            Initializes the LeafRanger with specific attributes and animations.

        ability(self, game, *args):
            Executes the Leaf Ranger's ability action.

        move_environment(direction, game):
            Moves the environment based on player's movement direction.

        update(self, screen, game):
            Updates the Leaf Ranger's state and actions.
    """

    def __init__(self, x, y):
        """
        Initialize the Leaf Ranger with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the Leaf Ranger's initial position.
            y (int): The y-coordinate of the Leaf Ranger's initial position.
        """
        run = [f"image/Heros/leaf_ranger/run/run_{i}.png" for i in range(1, 11)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/leaf_ranger/idle/idle_{i}.png" for i in range(1, 13)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = [f"image/Heros/leaf_ranger/jump_full/jump_{i}.png" for i in range(1, 22)]
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/leaf_ranger/1_atk/1_atk_{i}.png" for i in range(1, 11)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        ulta_images_paths = [f'image/Heros/leaf_ranger/sp_atk/sp_atk_{i}.png' for i in range(1, 18)]
        self.ulta_images = ImageCache.get_images(ulta_images_paths, (1.5, 1.5))

        ability_images_paths = [f'image/Heros/leaf_ranger/2_atk/2_atk_{i}.png' for i in range(1, 16)]
        self.ability_images = ImageCache.get_images(ability_images_paths, (1.5, 1.5))

        super().__init__(x, y, 60, 60)

        self.hp = constants.PLAYER_HP_COUNT - 1
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 4

        self.attack_range = constants.PLAYER_ATTACK_RANGE * 1.7 * screen_obj.width_scale
        self.ulta_range = constants.PLAYER_ULTA_RANGE * 1.7 * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK

        self.arrows = pygame.sprite.Group()
        self.create_arrow = False

        self.can_use_ability_flying = True

    def ability(self, game, *args):
        """
        Perform the Leaf Ranger's ability action.

        Args:
            game: The game instance.
            *args: Additional arguments (not used).
        """
        if self.ability_animation_count == 0 and not self.use_ulta:
            self.create_arrow = True

    @staticmethod
    def move_environment(direction, game):
        """
        Move the environment based on the player's movement direction.

        Args:
            direction (str): The direction to move ('left' or 'right').
            game: The game instance.
        """
        super().move_environment(direction, game)

        for arrow in game.player.arrows:
            arrow.move_sprite(direction)

    def update(self, screen, game):
        """
        Update the Leaf Ranger's state and actions.

        Args:
            screen: The Pygame screen surface.
            game: The game instance.
        """
        super().update(screen, game)

        if self.ability_animation_count == len(self.ability_images) // 2 and self.create_arrow:
            arrow = Shockwave(self.rect.centerx, self.rect.centery, 10, 0, self.attack_direction, "arrow")
            self.arrows.add(arrow)
            self.create_arrow = False

        self.arrows.update(screen, self.arrows, game, "enemies")
