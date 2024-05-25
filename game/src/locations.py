import pygame
from game.src.screen import screen_obj
import game.src.constants as constants

pygame.mixer.init()


class Locations:

    def __init__(self, background_paths, sound_path, scale):
        self.backgrounds = [[pygame.transform.scale(pygame.image.load(background_path).convert_alpha(), scale), 0] for background_path in background_paths]

        self.background_speed = constants.BACKGROUND_SPEED * screen_obj.width_scale

        self.sound = pygame.mixer.Sound(sound_path)

    def draw_background(self, screen):
        for background in self.backgrounds:
            screen.blit(background[0], (background[1], 0))
            screen.blit(background[0], (background[1] + screen_obj.width, 0))
            screen.blit(background[0], (background[1] - screen_obj.width, 0))



    def move_background(self, direction):
        if direction == 'right':
            self.background_speed = -constants.BACKGROUND_SPEED * screen_obj.width_scale
        elif direction == 'left':
            self.background_speed = constants.BACKGROUND_SPEED * screen_obj.width_scale

        for (i, background) in enumerate(self.backgrounds):

            if background[1] <= -screen_obj.width or background[1] >= screen_obj.width:
                background[1] = 0

            background[1] += self.background_speed * i


class PartialBackground:
    basesImage = {"brick_wall": pygame.image.load("image/locations/backgrounds/brick background.png").convert_alpha(),
                  "brown_brick_wall": pygame.image.load("image/locations/backgrounds/brick background with brown.png").convert_alpha(),}

    def __init__(self, x, y, width, height, image_name="brick_wall"):
        self.background = pygame.transform.scale(PartialBackground.basesImage[image_name], (width, height))
        self.x = x
        self.y = y
        self.background_speed = constants.PARTIAL_BACKGROUND_SPEED * screen_obj.width_scale

    def draw(self, screen):
        screen.blit(self.background, (self.x, self.y))

    def move_background(self, direction):
        if direction == 'right':
            self.x += -self.background_speed
        elif direction == 'left':
            self.x += self.background_speed









