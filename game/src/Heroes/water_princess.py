from game.src.Heroes.super_player import SuperPlayer
from game.src.cache import ImageCache
import game.src.constants as constants
from game.src.screen import screen_obj


class WaterPrincess(SuperPlayer):
    def __init__(self, x, y):
        run = [f"image/Heros/water_princess/02_walk/walk_{i}.png" for i in range(1, 11)]
        self.run = ImageCache.get_images(run, (1.5, 1.5))

        stay = [f"image/Heros/water_princess/01_idle/idle_{i}.png" for i in range(1, 9)]
        self.stay_images = ImageCache.get_images(stay, (1.5, 1.5))

        jump = ([f"image/Heros/water_princess/04_jump/j_down_{i}.png" for i in range(1, 4)] +
                [f"image/Heros/water_princess/04_jump/j_up_{i}.png" for i in range(1, 4)])
        self.jump = ImageCache.get_images(jump, (1.5, 1.5))

        attack_1 = [f"image/Heros/water_princess/07_1_atk/1_atk_{i}.png" for i in range(1, 8)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.5, 1.5))

        ability_images_paths = [f'image/Heros/water_princess/11_heal/heal_{i}.png' for i in range(1, 13)]
        self.ability_images = ImageCache.get_images(ability_images_paths, (1.5, 1.5))

        ulta_images_paths = [f'image/Heros/water_princess/10_sp_atk/sp_atk_{i}.png' for i in range(1, 33)]
        self.ulta_images = ImageCache.get_images(ulta_images_paths, (1.5, 1.5))

        super().__init__(x, y, 50, 50)

        self.hp = constants.PLAYER_HP_COUNT - 2
        self.current_hp = self.hp

        self.const_delay_animation = 3
        self.const_delay_jump_animation = 11

        self.attack_range = constants.PLAYER_ATTACK_RANGE * 1.3 * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK + 10


    def ability(self, game, *args):
        if self.current_hp < self.hp:
            self.current_hp += 1
