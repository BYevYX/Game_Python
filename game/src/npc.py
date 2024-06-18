"""
This module defines classes for non-playable characters (NPCs) in a Pygame-based game.

Classes:
- Npc: Represents a basic NPC with movement and animation capabilities.
- Blacksmith: Represents a specialized NPC with additional shop interface functionality.

Attributes and Methods:
- Npc Class:
    Attributes:
    - animation_images: List of images for animating the NPC.
    - direction: Current direction of movement ('right' or 'left').
    - velocity: Speed of movement.
    - animation_count: Index of the current animation frame.
    - const_delay: Constant delay between animation frames.
    - delay: Current delay count for animation frame change.
    - rect: Rectangle defining the position and size of the NPC.
    - has_shop: Boolean indicating if the NPC has a shop interface.

    Methods:
    - __init__(self, x, y): Initializes the NPC object.
    - animation(self, screen): Animates the NPC by blitting the current frame onto the screen.
    - check_animation_count(self): Updates the animation frame count based on the delay.
    - move_npc(self, direction): Moves the NPC in the specified direction.
    - update(self, screen): Updates the NPC's animation and position.

- Blacksmith Class (Inherits from Npc):
    Attributes:
    - animation_images: List of images for animating the blacksmith.
    - const_delay: Constant delay between animation frames.
    - has_shop: Boolean indicating if the blacksmith has a shop interface.
    - shop_items: Dictionary mapping items available for sale to their prices.

    Methods:
    - __init__(self, x, y): Initializes the Blacksmith object.
    - open_shop(self, screen, player): Opens the shop interface for the player to buy items.
    - buy_item(self, player, item): Handles the logic for buying an item from the shop.
"""

# Import statements for game dependencies (constants, screen_obj, ImageCache, sys, pygame)
import sys
from game.src import constants
from game.src.screen import screen_obj
from game.src.cache import ImageCache
import pygame


class Npc(pygame.sprite.Sprite):
    """
        A class representing a non-playable character (NPC) in a Pygame-based game.

        Attributes:
        - animation_images: List of images for animating the NPC.
        - direction: Current direction of movement ('right' or 'left').
        - velocity: Speed of movement.
        - animation_count: Index of the current animation frame.
        - const_delay: Constant delay between animation frames.
        - delay: Current delay count for animation frame change.
        - rect: Rectangle defining the position and size of the NPC.
        - has_shop: Boolean indicating if the NPC has a shop interface.

        Methods:
        - __init__(self, x, y): Initializes the NPC object.
        - animation(self, screen): Animates the NPC by blitting the current frame onto the screen.
        - check_animation_count(self): Updates the animation frame count based on the delay.
        - move_npc(self, direction): Moves the NPC in the specified direction.
        - update(self, screen): Updates the NPC's animation and position.
        """

    animation_images = None

    def __init__(self, x, y):
        """
        Initialize the NPC object.

        :param x: Initial x-coordinate of the NPC.
        :param y: Initial y-coordinate of the NPC.
        :rtype: object
        """
        super().__init__()

        self.direction = 'right'
        self.velocity = constants.VELOCITY * screen_obj.width_scale

        self.animation_count = 0
        self.const_delay = 0
        self.delay = 0

        self.rect = self.animation_images[0].get_rect()
        self.rect.x = x
        self.rect.y = y

        self.has_shop = False

    def animation(self, screen):
        """
        Animate the NPC by blitting the current frame onto the screen.

        :param screen: The screen surface to draw on.
        :rtype: None
        """
        screen.blit(self.animation_images[self.animation_count], (self.rect.x, self.rect.y))

    def check_animation_count(self):
        """
        Update the animation frame count based on the delay.

        :rtype: None
        """
        self.delay += 1

        if self.animation_count == len(self.animation_images) - 1:
            self.animation_count = 0
        elif self.delay == self.const_delay:
            self.delay = 0
            self.animation_count += 1

    def move_npc(self, direction):
        """
        Move the NPC in the specified direction.

        :param direction: The direction to move the NPC.
        :rtype: None
        """
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

        self.rect.x += self.velocity

    def update(self, screen):
        """
        Update the NPC's animation and position.

        :param screen: The screen surface to draw on.
        :rtype: None
        """
        self.animation(screen)
        self.check_animation_count()


class Blacksmith(Npc):
    """
        A class representing a blacksmith NPC with a shop interface in a Pygame-based game.

        Attributes:
        - animation_images: List of images for animating the blacksmith.
        - const_delay: Constant delay between animation frames.
        - has_shop: Boolean indicating if the blacksmith has a shop interface.
        - shop_items: Dictionary mapping items available for sale to their prices.

        Methods:
        - __init__(self, x, y): Initializes the Blacksmith object.
        - open_shop(self, screen, player): Opens the shop interface for the player to buy items.
        - buy_item(self, player, item): Handles the logic for buying an item from the shop.
        """

    def __init__(self, x, y):
        """
        Initialize the Blacksmith object.

        :param x: Initial x-coordinate of the blacksmith.
        :param y: Initial y-coordinate of the blacksmith.
        :rtype: object
        """

        animation_images = [f'image/npc/blacksmith/BLACKSMITH_{i}.png' for i in range(1, 8)]
        self.animation_images = ImageCache.get_images(animation_images)

        super().__init__(x, y)

        self.const_delay = 3

        self.has_shop = True
        self.shop_items = {
            'Sword': 100,
            'Shield': 150,
            'Potion': 50,
        }

    def open_shop(self, screen, player):
        """
        Open the shop interface, allowing the player to buy items.

        :param screen: The screen surface to draw the shop interface on.
        :param player: The player object interacting with the shop.
        :rtype: None
        """
        font = pygame.font.Font(None, 36)
        y_offset = 50
        for item, price in self.shop_items.items():
            item_text = font.render(f"{item}: {price} coins", True, (255, 255, 255))
            screen.blit(item_text, (50, y_offset))
            y_offset += 40

        pygame.display.flip()

        buying = True
        while buying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        buying = False
                    elif event.key == pygame.K_1:
                        self.buy_item(player, 'Sword')
                    elif event.key == pygame.K_2:
                        self.buy_item(player, 'Shield')
                    elif event.key == pygame.K_3:
                        self.buy_item(player, 'Potion')

    def buy_item(self, player, item):
        """
        Handle the logic for buying an item from the shop.

        :param player: The player object buying the item.
        :param item: The item to be bought.
        :rtype: None
        """
        if item in self.shop_items:
            price = self.shop_items[item]
            if player.coins >= price:
                player.coins -= price
                player.inventory.append(item)
                print(f"Bought {item} for {price} coins")
            else:
                print("Not enough coins")
