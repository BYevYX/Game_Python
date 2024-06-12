import sys

import pygame

import game.src.constants as constants
from game.src.screen import screen_obj


class Npc(pygame.sprite.Sprite):
    animation_images = None

    def __init__(self, x, y):
        """

        :rtype: object
        :param x: 
        :param y: 
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

        :rtype: object
        :param screen: 
        """
        screen.blit(self.animation_images[self.animation_count], (self.rect.x, self.rect.y))

    def check_animation_count(self):
        """
        :rtype: object

        """
        self.delay += 1

        if self.animation_count == len(self.animation_images) - 1:
            self.animation_count = 0
        elif self.delay == self.const_delay:
            self.delay = 0
            self.animation_count += 1

    def move_npc(self, direction):
        """

        :rtype: object
        :param direction: 
        """
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

        self.rect.x += self.velocity

    def update(self, screen):
        """

        :rtype: object
        :param screen: 
        """
        self.animation(screen)
        self.check_animation_count()


class Blacksmith(Npc):
    def __init__(self, x, y):
        """

        :rtype: object
        :param x: 
        :param y: 
        """
        self.animation_images = [
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_1.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_2.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_3.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_4.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_5.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_6.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_7.png').convert_alpha(),
        ]

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

        :rtype: object
        :param screen: 
        :param player: 
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

        :rtype: object
        :param player: 
        :param item: 
        """
        if item in self.shop_items:
            price = self.shop_items[item]
            if player.coins >= price:
                player.coins -= price
                player.inventory.append(item)
                print(f"Bought {item} for {price} coins")
            else:
                print("Not enough coins")
