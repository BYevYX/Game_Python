from game.src.enemies.enemies_base import Enemy
import game.src.constants as constants
from game.src.cache import ImageCache
from game.src.screen import screen_obj


class Satyr(Enemy):

    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        image_paths = [
            'image/enemys/satyr/move/satyr-Sheet_1.png',
            'image/enemys/satyr/move/satyr-Sheet_2.png',
            'image/enemys/satyr/move/satyr-Sheet_3.png',
            'image/enemys/satyr/move/satyr-Sheet_4.png',
            'image/enemys/satyr/move/satyr-Sheet_5.png',
            'image/enemys/satyr/move/satyr-Sheet_6.png',
            'image/enemys/satyr/move/satyr-Sheet_7.png',
            'image/enemys/satyr/move/satyr-Sheet_8.png',
            'image/enemys/satyr/move/satyr-Sheet_9.png',
            'image/enemys/satyr/move/satyr-Sheet_10.png',
            'image/enemys/satyr/move/satyr-Sheet_11.png',
            'image/enemys/satyr/move/satyr-Sheet_12.png',
            'image/enemys/satyr/move/satyr-Sheet_13.png',
            'image/enemys/satyr/move/satyr-Sheet_14.png',
            'image/enemys/satyr/move/satyr-Sheet_15.png',
            'image/enemys/satyr/move/satyr-Sheet_16.png',
            'image/enemys/satyr/move/satyr-Sheet_17.png',
            'image/enemys/satyr/move/satyr-Sheet_18.png',
            'image/enemys/satyr/move/satyr-Sheet_19.png',
            'image/enemys/satyr/move/satyr-Sheet_20.png',
            'image/enemys/satyr/move/satyr-Sheet_21.png',
        ]

        death_paths = [
            'image/enemys/satyr/depth/satyr death_1.png',
            'image/enemys/satyr/depth/satyr death_2.png',
            'image/enemys/satyr/depth/satyr death_3.png',
            'image/enemys/satyr/depth/satyr death_4.png',
            'image/enemys/satyr/depth/satyr death_5.png',
            'image/enemys/satyr/depth/satyr death_6.png',
            'image/enemys/satyr/depth/satyr death_7.png',
            'image/enemys/satyr/depth/satyr death_8.png',
            'image/enemys/satyr/depth/satyr death_9.png',
        ]

        self.images = ImageCache.get_images(image_paths, (2 * screen_obj.width_scale, 2 * screen_obj.height_scale))
        super().__init__(x, y - 40 * screen_obj.height_scale, range_place)

        self.death_images = ImageCache.get_images(death_paths, (2 * screen_obj.width_scale, 2 * screen_obj.height_scale))
        self.current_hp = 100
        self.const_delay_death_animation = 2
        self.const_delay_animation = 2
        self.speed = (constants.ENEMY_NORMAL_SPEED - 1) * screen_obj.width_scale

