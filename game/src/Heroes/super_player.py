"""
Module: game.src.Heroes.super_player

This module defines the SuperPlayer character class,
inheriting from Player, with enhanced abilities and animations.

Attributes:
- ability_images (list): List of images for the SuperPlayer's ability animation.
- ulta_images (list): List of images for the SuperPlayer's ultimate attack animation.
- use_ability (bool): Flag indicating if the ability is currently in use.
- last_ability_time (int): Timestamp of the last time the ability was used.
- ability_cooldown (int): Cooldown time for using the ability again.
- can_use_ability_flying (bool): Flag indicating if the ability can be used while jumping/flying.
- use_ulta (bool): Flag indicating if the ultimate attack is currently in use.
- last_ulta_time (int): Timestamp of the last time the ultimate attack was used.
- ulta_cooldown (int): Cooldown time for using the ultimate attack again.
- ulta_range (float): Range of the ultimate attack.
- ulta_damage (int): Damage inflicted by the ultimate attack.
- ability_animation_count (int): Animation frame counter for ability animation.
- ulta_animation_count (int): Animation frame counter for ultimate attack animation.

Methods:
- __init__(self, x, y, rect_x, rect_y):
    Initializes the SuperPlayer with specific attributes and animations.

- draw(self, screen, keys, position=None):
    Draws the SuperPlayer on the screen, handling ability and ultimate attack animations.

- check_animation_count(self):
    Updates the animation frame counters for abilities and ultimate attacks.

- ability(self, game, *args):
    Perform the SuperPlayer's ability. Should be overridden in subclasses.

- ulta(self, enemies):
    Perform the SuperPlayer's ultimate attack, dealing damage to enemies within range.

- move(self, keys, game):
    Move the SuperPlayer based on input keys and
    game state, handling ability and ultimate attack activation.

Usage:
from game.src.Heroes.super_player import SuperPlayer

# Example initialization of the SuperPlayer character
super_player = SuperPlayer(x=200, y=300, rect_x=50, rect_y=50)

Notes:
- This class assumes that the constants, Player class,
ImageCache, and screen_obj are correctly imported and initialized.
- Adjustments to image paths or scaling factors
in ImageCache.get_images calls should be made as per specific game requirements.
- Ensure all necessary image files are correctly linked and available in the specified paths.

"""
from game.src import constants
from game.src.Heroes.player import Player
from game.src.screen import screen_obj
import pygame


class SuperPlayer(Player):
    """
        A class representing a super player character, inheriting from Player.

        Attributes:
            ability_images (list): List of images for the SuperPlayer's ability animation.
            ulta_images (list): List of images for the SuperPlayer's ultimate attack animation.
            use_ability (bool): Flag indicating if the ability is currently in use.
            last_ability_time (int): Timestamp of the last time the ability was used.
            ability_cooldown (int): Cooldown time for using the ability again.
            can_use_ability_flying (bool):
                Flag indicating if the ability can be used while jumping/flying.
            use_ulta (bool): Flag indicating if the ultimate attack is currently in use.
            last_ulta_time (int): Timestamp of the last time the ultimate attack was used.
            ulta_cooldown (int): Cooldown time for using the ultimate attack again.
            ulta_range (float): Range of the ultimate attack.
            ulta_damage (int): Damage inflicted by the ultimate attack.
            ability_animation_count (int): Animation frame counter for ability animation.
            ulta_animation_count (int): Animation frame counter for ultimate attack animation.

        Methods:
            __init__(self, x, y, rect_x, rect_y):
                Initializes the SuperPlayer with specific attributes and animations.

            draw(self, screen, keys, position=None):
                Draws the SuperPlayer on the screen,
                handling ability and ultimate attack animations.

            check_animation_count(self):
                Updates the animation frame counters for abilities and ultimate attacks.

            ability(self, game, *args):
                Perform the SuperPlayer's ability. Should be overridden in subclasses.

            ulta(self, enemies):
                Perform the SuperPlayer's ultimate attack, dealing damage to enemies within range.

            move(self, keys, game):
                Move the SuperPlayer based on input keys and game state,
                handling ability and ultimate attack activation.
        """

    ability_images = []
    ulta_images = []

    def __init__(self, x, y, rect_x, rect_y):
        """
        Initialize the SuperPlayer with specific attributes and animations.

        :param x: The x-coordinate of the SuperPlayer's initial position.
        :param y: The y-coordinate of the SuperPlayer's initial position.
        :param rect_x: The width of the SuperPlayer's collision rectangle.
        :param rect_y: The height of the SuperPlayer's collision rectangle.
        :rtype: object
        """
        super().__init__(x, y)

        image_rect = self.run[0].get_rect()
        # Center the image
        image_rect.center = (screen_obj.width // 2, screen_obj.height - 200 * screen_obj.height_scale)

        small_rect_size = (rect_x * screen_obj.width_scale, rect_y * screen_obj.height_scale)
        self.rect = pygame.Rect(0, 0, *small_rect_size)
        self.rect.center = image_rect.center

        self.dx = self.run[0].get_width() // 2 - rect_x // 2 * screen_obj.width_scale
        self.dy = self.run[0].get_height() - rect_y * screen_obj.height_scale

        self.use_ability = False
        self.last_ability_time = 0
        self.ability_cooldown = constants.PLAYER_ABILITY_COOLDOWN
        self.can_use_ability_flying = False

        self.use_ulta = False
        self.last_ulta_time = 0
        self.ulta_cooldown = constants.PLAYER_ULTA_COOLDOWN
        self.ulta_range = constants.PLAYER_ULTA_RANGE * screen_obj.width_scale
        self.ulta_damage = constants.PLAYER_ULTA_DAMAGE

        self.ability_animation_count = 0
        self.ulta_animation_count = 0

    def draw(self, screen, keys, position=None):
        """
        Draw the SuperPlayer on the screen, handling ability and ulta animations.

        :param screen: The screen surface to draw the SuperPlayer on.
        :param keys: The current state of all keyboard buttons.
        :param position: The position to draw the SuperPlayer. Defaults to None.
        :rtype: object
        """
        if not self.use_ability and not self.use_ulta:
            super().draw(screen, keys, (self.rect.x - self.dx, self.rect.y - self.dy))
            return

        self.animate_hp(screen)

        if not position:
            position = (self.rect.x - self.dx, self.rect.y - self.dy)

        if self.use_ability and not self.use_ulta:
            if self.attack_direction == 1:
                image = self.ability_images[self.ability_animation_count]
                self.blink(image)
                screen.blit(image, position)
            else:
                image = pygame.transform.flip(self.ability_images[self.ability_animation_count], True, False)
                self.blink(image)
                screen.blit(image, position)

        if self.use_ulta and not self.use_ability:
            if self.attack_direction == 1:
                image = self.ulta_images[self.ulta_animation_count]
                self.blink(image)
                screen.blit(image, position)
            else:
                image = pygame.transform.flip(self.ulta_images[self.ulta_animation_count], True, False)
                self.blink(image)
                screen.blit(image, position)

        self.check_animation_count()

    def check_animation_count(self):
        """
        Update the animation frame counters for abilities and ulta.

        :rtype: object
        """
        super().check_animation_count()

        if self.delay_animation == 0:
            if self.use_ability:
                self.ability_animation_count += 1

            elif self.use_ulta:
                self.ulta_animation_count += 1

        if self.ulta_animation_count >= len(self.ulta_images):
            self.ulta_animation_count = 0
            self.use_ulta = False

        elif self.ability_animation_count >= len(self.ability_images):
            self.ability_animation_count = 0
            self.use_ability = False

    def ability(self, game, *args):
        """
        Perform the SuperPlayer's ability.
        By default, this does nothing and should be overridden in subclasses.

        :param game: The game context in which the ability is used.
        :param args: Additional arguments for the ability.
        :rtype: object
        """
        self.use_ability = False

    def ulta(self, enemies):
        """
        Perform the SuperPlayer's ulta attack, dealing damage to enemies within range.

        :param enemies: A list of enemy groups to check for collisions with the ulta attack.
        :rtype: object
        """
        self.last_ulta_time = pygame.time.get_ticks()

        if self.attack_direction == 1:
            attack_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width + self.ulta_range, self.rect.height)
        else:
            attack_rect = pygame.Rect(self.rect.x, self.rect.y, -self.ulta_range, self.rect.height)

        for group in enemies:
            for enemy in group:
                if attack_rect.colliderect(enemy.rect):
                    enemy.take_damage(self.ulta_damage)

    def move(self, keys, game):
        """
        Move the SuperPlayer based on input keys and game state,
        handling ability and ulta activation.

        :param keys: The current state of all keyboard buttons.
        :param game: The game context.
        :rtype: None
        """
        super().move(keys, game)

        if (keys[pygame.K_r] and not self.use_ulta and not self.use_ability and
                (not self.is_jump or self.can_use_ability_flying) and
                pygame.time.get_ticks() - self.last_ability_time > self.ability_cooldown):
            self.use_ability = True
            self.ability(game)

        if (keys[pygame.K_q] and not self.is_attacking and not self.use_ability and not self.use_ulta and
                pygame.time.get_ticks() - self.last_ulta_time > self.ulta_cooldown):
            self.use_ulta = True
            self.ulta(game.enemies)
