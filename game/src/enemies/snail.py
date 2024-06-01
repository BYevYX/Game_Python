import pygame
from game.src.enemies.enemies_base import CommonEnemy
from game.src.cache import ImageCache
from game.src.screen import screen_obj


class Snail(CommonEnemy):

    def __init__(self, x, y, range_place=100 * screen_obj.width_scale):
        images_paths = [
            'image/enemys/ramses_snail/Walk/Spr_Walk_1.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_2.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_3.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_4.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_5.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_6.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_7.png',
            'image/enemys/ramses_snail/Walk/Spr_Walk_8.png',
        ]

        sniff_paths = [
            'image/enemys/ramses_snail/Track/Spr_Track_1.png',
            'image/enemys/ramses_snail/Track/Spr_Track_2.png',
            'image/enemys/ramses_snail/Track/Spr_Track_3.png',
            'image/enemys/ramses_snail/Track/Spr_Track_4.png',
        ]

        self.images = ImageCache.get_images(images_paths, (2 * screen_obj.width_scale, 2 * screen_obj.height_scale))
        super().__init__(x, y - 30 * screen_obj.height_scale, range_place)
        self.current_hp = 60

        self.sniff = ImageCache.get_images(sniff_paths, (2 * screen_obj.width_scale, 2 * screen_obj.height_scale))
        self.is_walk = True
        self.sniff_animation_count = 0
        self.walk_count = 0

        self.const_delay_animation = 2

    def move(self):
        if self.is_walk:
            super().move()

    def draw(self, screen):
        if self.is_walk:
            super().draw(screen)
            if self.animation_count == 0:
                self.walk_count += 1
            if self.walk_count == 3:
                self.walk_count = 0
                self.is_walk = False

        else:
            if self.speed < 0:
                screen.blit(pygame.transform.flip(self.sniff[self.sniff_animation_count % len(self.sniff)], True, False),
                            (self.rect.x, self.rect.y))
            else:
                screen.blit(self.sniff[self.sniff_animation_count % len(self.sniff)], (self.rect.x, self.rect.y))

            self.sniff_animation_count += 1
            if self.sniff_animation_count == len(self.sniff) * 4:
                self.sniff_animation_count = 0
                self.is_walk = True
