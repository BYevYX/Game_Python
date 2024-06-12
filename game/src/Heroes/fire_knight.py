import pygame

import game.src.constants as constants
from game.src.Heroes.player import Player
from game.src.cache import ImageCache
from game.src.screen import screen_obj


class FireKnight(Player):
    def __init__(self, x, y):
        """

        :rtype: object
        :param x:
        :param y:
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
        :rtype: object

        """
        super().check_animation_count()

        if self.delay_animation == 0:
            if self.attack_animation_count == 3:
                self.y -= 60
            elif self.attack_animation_count == 7:
                self.y += 60
