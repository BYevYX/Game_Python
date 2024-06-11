from game.src.Heroes.super_player import SuperPlayer
from game.src.cache import ImageCache
import game.src.constants as constants
from game.src.screen import screen_obj


class LeafRanger(SuperPlayer):
    def __init__(self, x, y):
        run = [f"image/Heros/leaf_ranger/run/run_{i}.png" for i in range(1, 11)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/leaf_ranger/idle/idle_{i}.png" for i in range(1, 13)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = [f"image/Heros/leaf_ranger/jump_full/jump_{i}.png" for i in range(1, 22)]
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/leaf_ranger/1_atk/1_atk_{i}.png" for i in range(1, 11)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        super().__init__(x, y, 60, 60)

        self.hp = constants.PLAYER_HP_COUNT - 1
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 4

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK
