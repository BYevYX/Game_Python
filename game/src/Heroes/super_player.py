import pygame

import game.src.constants as constants
from game.src.Heroes.player import Player
from game.src.screen import screen_obj


class SuperPlayer(Player):
    ability_images = []
    ulta_images = []

    def __init__(self, x, y, rect_x, rect_y):
        """

        :rtype: object
        :param x:
        :param y:
        :param rect_x:
        :param rect_y:
        """
        super().__init__(x, y)

        image_rect = self.run[0].get_rect()
        # Центрирование изображения
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

        :rtype: object
        :param screen:
        :param keys:
        :param position:
        :return:
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

        :rtype: object
        :param game:
        :param args:
        """
        self.use_ability = False

    def ulta(self, enemies):
        """

        :rtype: object
        :param enemies:
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

        :rtype: None
        :param keys:
        :param game:
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
