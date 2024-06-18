"""
Module: game.src.enemies.snail

This module defines the Snail class, which represents an enemy Snail in the game.

Attributes:
- images (list): List of walking animation images for the snail.
- sniff (list): List of sniffing animation images for the snail.
- is_walk (bool): Flag indicating if the snail is currently walking.
- sniff_animation_count (int): Counter for sniffing animation frames.
- walk_count (int): Counter for walk cycles.
- const_delay_animation (int): Constant delay between animation frames.

Methods:
- __init__(self, x, y, range_place=100 * screen_obj.width_scale):
    Initializes the Snail with specific attributes and animations.
- move(self):
    Moves the snail if it is currently in walking mode.
- draw(self, screen):
    Draws the snail on the screen, handling walking and sniffing animations.

Usage:
from game.src.enemies.snail import Snail

# Example initialization of a Snail enemy
snail = Snail(x=200, y=400)

Notes:
- This class assumes that constants, pygame,
ImageCache, CommonEnemy, and other necessary modules are correctly imported and initialized.
- Adjustments to image paths, scaling factors,
and game mechanics should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src.cache import ImageCache
from game.src.enemies.enemies_base import CommonEnemy
from game.src.screen import screen_obj
import pygame


class Snail(CommonEnemy):
    """
    Class representing a Snail enemy in the game.

    Attributes:
        images (list): List of walking animation images for the snail.
        sniff (list): List of sniffing animation images for the snail.
        is_walk (bool): Flag indicating if the snail is currently walking.
        sniff_animation_count (int): Counter for sniffing animation frames.
        walk_count (int): Counter for walk cycles.
        const_delay_animation (int): Constant delay between animation frames.

    Methods:
        __init__(self, x, y, range_place=100 * screen_obj.width_scale):
            Initializes the Snail with specific attributes and animations.

        move(self):
            Moves the snail if it is currently in walking mode.

        draw(self, screen):
            Draws the snail on the screen, handling walking and sniffing animations.
    """

    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        """
        Initialize the Snail with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the Snail's initial position.
            y (int): The y-coordinate of the Snail's initial position.
            range_place (int): The range in which the snail can move horizontally.
        """
        images_paths = [
            'image/enemys/ramses_snail/Walk/Spr_Walk_1.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_2.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_3.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_4.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_5.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_6.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_7.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_8.png',
        ]

        sniff_paths = [
            'image/enemys/ramses_snail/Track/Spr_Track_1.png',
            'image/enemys/ramses_snail/Track/Spr_Track_2.png',
            'image/enemys/ramses_snail/Track/Spr_Track_3.png',
            'image/enemys/ramses_snail/Track/Spr_Track_4.png',
        ]

        self.images = ImageCache.get_images(images_paths, (2, 2))
        super().__init__(x, y - 30 * screen_obj.height_scale, range_place)
        self.current_hp = 60

        self.sniff = ImageCache.get_images(sniff_paths, (2, 2))
        self.is_walk = True
        self.sniff_animation_count = 0
        self.walk_count = 0

        self.const_delay_animation = 2

    def move(self):
        """
        Move the snail if it is currently walking.

        Overrides the method from the base class CommonEnemy.
        """
        if self.is_walk:
            super().move()

    def draw(self, screen):
        """
        Draw the snail on the screen, handling walking and sniffing animations.

        Args:
            screen (pygame.Surface): The Pygame screen surface to draw on.
        """
        if self.is_walk:
            super().draw(screen)
            if self.animation_count == 0:
                self.walk_count += 1
            if self.walk_count == 3:
                self.walk_count = 0
                self.is_walk = False
        else:
            if self.speed < 0:
                screen.blit(
                    pygame.transform.flip(self.sniff[self.sniff_animation_count % len(self.sniff)], True, False),
                    (self.rect.x, self.rect.y))
            else:
                screen.blit(self.sniff[self.sniff_animation_count % len(self.sniff)], (self.rect.x, self.rect.y))

            self.sniff_animation_count += 1
            if self.sniff_animation_count == len(self.sniff) * 4:
                self.sniff_animation_count = 0
                self.is_walk = True
