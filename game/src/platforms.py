import pygame
import game.src.constants as constants
from game.src.screen import screen_obj
# from random import randint




class Platform(pygame.sprite.Sprite):
    platform_images = {
        "main_platform": pygame.image.load("image/locations/platforms/big platform.png").convert_alpha(),
        "left_wall": pygame.image.load("image/locations/platforms/left_wall.png").convert_alpha(),
        "right_wall": pygame.image.load("image/locations/platforms/right_wall.png").convert_alpha(),
        "moving_platform": pygame.image.load("image/locations/platforms/moving_platform.png").convert_alpha(),
        "mountain": pygame.image.load("image/locations/obstacles/big_mountain.png").convert_alpha(),
    }

    def __init__(self, x, y, width, height, image_type="main_platform"):
        super().__init__()

        self.image = pygame.transform.scale(Platform.platform_images[image_type], (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = constants.VELOCITY * screen_obj.width_scale
        self.direction = "right"


    def move_platform(self, direction):
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

        self.rect.x += self.velocity



class MovingPlatform(Platform):
    def __init__(self, x, y, width, height, up, to, slide_direction='x', image_type="moving_platform"):
        super().__init__(x, y, width, height, image_type)

        self.up = up
        self.to = to
        self.slide_direction = slide_direction
        self.slide_velocity = constants.VELOCITY // 2

    def slide(self):
        if self.slide_direction == 'x':
            self.rect.x += self.slide_velocity
            if self.rect.right > max(self.to, self.up) or self.rect.left < min(self.up, self.to):
                self.slide_velocity *= -1

        elif self.slide_direction == 'y':
            self.rect.y += self.slide_velocity
            if self.rect.top > max(self.to, self.up) or self.rect.bottom < min(self.up, self.to):
                self.slide_velocity *= -1

    def move_platform(self, direction):
        super().move_platform(direction)

        if self.slide_direction == 'x':
            self.up += self.velocity
            self.to += self.velocity


    # @staticmethod
    # def grouper_random(levels, group=None):
    #     platforms = pygame.sprite.Group()
    #     if group:
    #         platforms.add(group)
    #
    #     for x in range(0, screen_obj.width, 300):
    #         platforms.add(Platform(x, screen_obj.height - 40, 300, 40))
    #
    #     for i in range(levels):
    #         for j in range(0, screen_obj.width, 330):
    #             platforms.add(Platform(j + randint(-70, 70), (i + 0.7) * randint(130, 140), 20 * randint(9, 10), 30))
    #
    #
    #     return platforms



