import pygame


class Player():
    def __init__(self):
        self.x = 150
        self.y = 270
        self.speed = 5

        self.run_animation_count = 0
        self.stay_animation_count = 0
        self.jump_animation_count = 0

        self.is_jump = False
        self.jump_height = 7

        self.run = [
            pygame.image.load('image/Hero/Run/run-1.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-2.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-3.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-4.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-5.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-6.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-7.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-8.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-9.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-10.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-11.png').convert_alpha(),
            pygame.image.load('image/Hero/Run/run-12.png').convert_alpha(),
        ]

        self.stay_images = [
            pygame.image.load('image/Hero/stay/idle-1.png').convert_alpha(),
            pygame.image.load('image/Hero/stay/idle-2.png').convert_alpha(),
            pygame.image.load('image/Hero/stay/idle-3.png').convert_alpha(),
            pygame.image.load('image/Hero/stay/idle-4.png').convert_alpha(),
            pygame.image.load('image/Hero/stay/idle-5.png').convert_alpha(),
            pygame.image.load('image/Hero/stay/idle-6.png').convert_alpha(),
        ]

        self.jump = [
            pygame.image.load('image/Hero/Jump/jump-1.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-2.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-3.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-4.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-5.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-6.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-7.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-8.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-9.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-10.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-11.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-12.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-13.png').convert_alpha(),
            pygame.image.load('image/Hero/Jump/jump-14.png').convert_alpha(),
        ]

        # !!! цикл !!!

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))

    def change_rect(self):
        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))

    def walk_right(self, screen):
        screen.blit(self.run[self.run_animation_count], (self.x, self.y))

    def walk_left(self, screen):
        screen.blit(pygame.transform.flip(self.run[self.run_animation_count], True, False), (self.x, self.y))

    def stay(self, screen):
        screen.blit(self.stay_images[self.stay_animation_count], (self.x, self.y))

    def jump_right(self, screen):
        screen.blit(self.jump[self.jump_animation_count], (self.x, self.y))

    def jump_left(self, screen):
        screen.blit(pygame.transform.flip(self.jump[self.jump_animation_count], True, False), (self.x, self.y))


    def check_animation_count(self):
        if self.run_animation_count == 11:
            self.run_animation_count = 0
        else:
            self.run_animation_count += 1

        if self.stay_animation_count == 5:
            self.stay_animation_count = 0
        else:
            self.stay_animation_count += 1

        if self.jump_animation_count == 13:
            self.jump_animation_count = 0
        else:
            self.jump_animation_count += 1
