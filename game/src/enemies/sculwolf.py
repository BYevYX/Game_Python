from game.src.enemies.enemies_base import CommonEnemy
from game.src.cache import ImageCache
import game.src.constants as constants
from game.src.screen import screen_obj


class Sculwolf(CommonEnemy):
    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        image_paths = [
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_1.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_2.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_3.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_4.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_5.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_6.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_7.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_8.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_9.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_10.png',
            'image/enemys/sculwolf/move/Massacre Sprite Sheet_11.png',
        ]

        death_paths = [
            'image/enemys/sculwolf/deth/Massacre death_1.png',
            'image/enemys/sculwolf/deth/Massacre death_2.png',
            'image/enemys/sculwolf/deth/Massacre death_3.png',
            'image/enemys/sculwolf/deth/Massacre death_4.png',
            'image/enemys/sculwolf/deth/Massacre death_5.png',
            'image/enemys/sculwolf/deth/Massacre death_6.png',
            'image/enemys/sculwolf/deth/Massacre death_7.png',
            'image/enemys/sculwolf/deth/Massacre death_8.png',
        ]

        self.images = ImageCache.get_images(image_paths, (screen_obj.width_scale, screen_obj.height_scale))
        super().__init__(x, y - 30 * screen_obj.height_scale, range_place)

        self.jump_height = constants.ENEMY_JUMP_HEIGHT * screen_obj.height_scale
        self.death_images = ImageCache.get_images(death_paths, (screen_obj.width_scale, screen_obj.height_scale))

        self.current_hp = 80
        self.const_delay_death_animation = 1
        self.const_delay_animation = 1


    def jump(self):
        if 7 <= self.animation_count <= 9:
            self.rect.y -= self.jump_height
        elif 0 <= self.animation_count <= 1 or self.animation_count == 10:
            self.rect.y += self.jump_height

    def move(self):
        super().move()
        self.jump()
