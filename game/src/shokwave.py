"""
A class representing a shockwave sprite in a Pygame-based game.

Attributes:
- velocity: A vector indicating the movement speed and direction of the shockwave.
- damage_dealt: Boolean indicating if damage has already been dealt by the shockwave.
- direction: Direction of the shockwave (1 for right, -1 for left).
- animation_count: Counter for animation frames of the shockwave.

Methods:
- __init__(self, x, y, dx, dy, direction=1, type_image="fireball"):
    Initializes the shockwave with given parameters.
- draw(self, screen): Draws the shockwave on the specified screen surface.
- update(self, screen, sprites, game, damage_to="player"):
    Updates the position of the shockwave and checks for collisions.
- move_sprite(self, direction): Moves the shockwave sprite in the specified direction.
- deal_damage_player(self, player): Deals damage to the player if collision occurs.
- deal_damage_enemy(self, enemies): Deals damage to enemies if collision occurs.
"""

from game.src import constants
from game.src.cache import ImageCache
from game.src.screen import screen_obj

import pygame


class Shockwave(pygame.sprite.Sprite):
    """
    A class representing a shockwave sprite in a Pygame-based game.

    Attributes:
    - velocity: A vector indicating the movement speed and direction of the shockwave.
    - damage_dealt: Boolean indicating if damage has already been dealt by the shockwave.
    - direction: Direction of the shockwave (1 for right, -1 for left).
    - animation_count: Counter for animation frames of the shockwave.

    Methods:
    - __init__(self, x, y, dx, dy, direction=1, type_image="fireball"):
        Initializes the shockwave with given parameters.
    - draw(self, screen): Draws the shockwave on the specified screen surface.
    - update(self, screen, sprites, game, damage_to="player"):
        Updates the position of the shockwave and checks for collisions.
    - move_sprite(self, direction): Moves the shockwave sprite in the specified direction.
    - deal_damage_player(self, player): Deals damage to the player if collision occurs.
    - deal_damage_enemy(self, enemies): Deals damage to enemies if collision occurs.
    """

    def __init__(self, x, y, dx, dy, direction=1, type_image="fireball"):
        """
        Initialize the Shockwave object.

        :param x: Initial x-coordinate of the shockwave.
        :param y: Initial y-coordinate of the shockwave.
        :param dx: Change in x-coordinate per update.
        :param dy: Change in y-coordinate per update.
        :param direction: Direction of the shockwave (1 for right, -1 for left).
        :param type_image: Type of image for the shockwave ("fireball" or other).
        """
        super().__init__()
        self.velocity = pygame.Vector2(direction * dx, dy)
        self.damage_dealt = False
        self.direction = direction
        self.animation_count = 0

        if type_image == "fireball":
            image_paths = [f"image/enemys/fireball/1_{i}.png" for i in range(61)]
        else:
            image_paths = ["image/Heros/leaf_ranger/arrow/arrow_.png"]

        self.images = ImageCache.get_images(image_paths)

        self.main_velocity = constants.VELOCITY * screen_obj.width_scale
        self.main_direction = 'right'

        image_rect = self.images[0].get_rect()
        image_rect.center = (x + 20 * screen_obj.width_scale, y - 15 * screen_obj.height_scale)

        rect_x = 20 * screen_obj.width_scale
        rect_y = 20 * screen_obj.height_scale

        small_rect_size = (rect_x, rect_y)
        self.position = [image_rect.x, image_rect.y]
        self.rect = pygame.Rect(0, 0, *small_rect_size)
        self.rect.center = image_rect.center

    def draw(self, screen):
        """
        Draw the shockwave on the screen.

        :param screen: The screen surface to draw on.
        :rtype: None
        """
        if self.direction == -1:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False),
                        self.position)
        elif self.direction == 1:
            screen.blit(self.images[self.animation_count], self.position)

        self.animation_count += 1
        if self.animation_count == len(self.images):
            self.animation_count = 0

    def update(self, screen, sprites, game, damage_to="player"):
        """
        Update the shockwave's position and check for collisions.

        :param screen: The screen surface to draw on.
        :param sprites: The group of sprites to which the shockwave belongs.
        :param game: The game object containing game state and entities.
        :param damage_to: The type of entity to deal damage to ("player" or "enemy").
        :rtype: None
        """
        self.rect.x += self.velocity.x * screen_obj.width_scale
        self.rect.y += self.velocity.y * screen_obj.height_scale

        self.position[0] += self.velocity.x * screen_obj.width_scale
        self.position[1] += self.velocity.y * screen_obj.height_scale

        self.draw(screen)
        if damage_to == "player":
            self.deal_damage_player(game.player)
        else:
            self.deal_damage_enemy(game.enemies)

        if self.rect.x > screen_obj.width or self.rect.x < 0:
            self.kill()
            sprites.remove(self)

    def move_sprite(self, direction):
        """
        Move the shockwave in the specified direction.

        :param direction: The direction to move the shockwave.
        :rtype: None
        """
        if direction != self.main_direction:
            self.main_velocity *= -1
            self.main_direction = direction

        self.rect.x += self.main_velocity
        self.position[0] += self.main_velocity

    def deal_damage_player(self, player):
        """
        Deal damage to the player if the shockwave collides with them.

        :param player: The player object to potentially deal damage to.
        :rtype: None
        """
        if not self.damage_dealt:
            if pygame.sprite.collide_rect(self, player):
                player.take_damage()
                self.damage_dealt = True

    def deal_damage_enemy(self, enemies):
        """
        Deal damage to enemies if the shockwave collides with them.

        :param enemies: The group of enemies to potentially deal damage to.
        :rtype: None
        """
        if not self.damage_dealt:
            for group in enemies:
                for enemy in group:
                    if pygame.sprite.collide_rect(self, enemy):
                        enemy.take_damage()
                        self.damage_dealt = True
