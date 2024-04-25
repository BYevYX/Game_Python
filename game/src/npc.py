import pygame


class Npc():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.animation_count = 0

        self.animation_images = []

    def animation(self, screen):
        screen.blit(self.animation_images[self.animation_count], (self.x, self.y))

    def check_animation_count(self):
        if self.animation_count == len(self.animation_images) - 1:
            self.animation_count = 0
        else:
            self.animation_count += 1


class Blacksmith(Npc):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.animation_images = [
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_1.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_2.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_3.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_4.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_5.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_6.png').convert_alpha(),
            pygame.image.load('image/npc/blacksmith/BLACKSMITH_7.png').convert_alpha(),
        ]
