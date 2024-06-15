import sys
import pygame

import game.src.constants as constants
from game.src.screen import screen_obj
from game.src.cache import ImageCache


class Npc(pygame.sprite.Sprite):
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
    def __init__(self, x, y):
        """
        Initialize the Blacksmith object.

        :param x: Initial x-coordinate of the blacksmith.
        :param y: Initial y-coordinate of the blacksmith.
        :rtype: object
        """

        animation_images = [f'image/npc/blacksmith/BLACKSMITH_{i}.png' for i in range (1, 8)]
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
