from game.src.Heroes.player import Player
from game.src.cache import ImageCache
import game.src.constants as constants
from game.src.screen import screen_obj


class StandardHero(Player):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.hp = constants.PLAYER_HP_COUNT - 1
        self.current_hp = self.hp

        self.const_delay_animation = 2
        self.const_delay_jump_animation = 5
        self.delay_animation = self.const_delay_animation
        self.delay_jump_animation = self.const_delay_jump_animation

        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK

        run = [f"image/Heros/standard hero/Run/run-{i}.png" for i in range(1, 13)]
        self.run = ImageCache.get_images(run, (1.2, 1.2))

        stay = [f"image/Heros/standard hero/stay/idle-{i}.png" for i in range(1, 7)]
        self.stay_images = ImageCache.get_images(stay, (1.2, 1.2))

        jump = [f"image/Heros/standard hero/Jump/jump-{i}.png" for i in range(1, 15)]
        self.jump = ImageCache.get_images(jump, (1.2, 1.2))

        attack_1 = [f"image/Heros/standard hero/Attack/attack-A{i}.png" for i in range(1, 8)]
        self.attack_1 = ImageCache.get_images(attack_1, (1.2, 1.2))

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))


