import pygame
import game.src.constants as constants
from game.src.screen import screen_obj


class Npc(pygame.sprite.Sprite):
    animation_images = None

    def __init__(self, x, y):
        super().__init__()

        self.direction = 'right'
        self.velocity = constants.VELOCITY * screen_obj.width_scale

        self.animation_count = 0
        self.const_delay = 0
        self.delay = 0

        self.rect = self.animation_images[0].get_rect()
        self.rect.x = x
        self.rect.y = y

    def animation(self, screen):
        screen.blit(self.animation_images[self.animation_count], (self.rect.x, self.rect.y))

    def check_animation_count(self):
        self.delay += 1

        if self.animation_count == len(self.animation_images) - 1:
            self.animation_count = 0
        elif self.delay == self.const_delay:
            self.delay = 0
            self.animation_count += 1

    def move_npc(self, direction):
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

        self.rect.x += self.velocity

    def update(self, screen):
        self.animation(screen)
        self.check_animation_count()


class Blacksmith(Npc):
    def __init__(self, x, y):
        self.animation_images = [
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_1.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_2.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_3.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_4.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_5.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_6.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_7.png').convert_alpha(),
        ]

        super().__init__(x, y)

        self.const_delay = 3

