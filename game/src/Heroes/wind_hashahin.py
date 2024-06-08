import pygame
from game.src.Heroes.player import Player
from game.src.cache import ImageCache
import game.src.constants as constants
from game.src.screen import screen_obj


class WindHashahin(Player):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.hp = constants.PLAYER_HP_COUNT - 1

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 10
        self.delay_animation = self.const_delay_animation
        self.delay_jump_animation = self.const_delay_jump_animation

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK - 10





        run = [f"image/Heros/Wind_hashahin/run/run_{i}.png" for i in range(1, 9)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/Wind_hashahin/idle/idle_{i}.png" for i in range(1, 9)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = ([f"image/Heros/Wind_hashahin/jump/j_up_{i}.png" for i in range(1, 4)] +
                [f"image/Heros/Wind_hashahin/jump/j_down_{i}.png" for i in range(1, 4)])
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/Wind_hashahin/1_atk/1_atk_{i}.png" for i in range(1, 9)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.rect.width - 30 * screen_obj.width_scale, self.rect.height)




