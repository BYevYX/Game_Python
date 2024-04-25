import pygame


class Locations():
    def __init__(self, background_path, sound_path, scale):
        self.background = pygame.transform.scale(pygame.image.load(background_path).convert_alpha(), scale)
        self.background_x = 0

        self.sound = pygame.mixer.Sound(sound_path)


class FirstLocation(Locations):
    def __init__(self, background_path, sound_path, scale):
        super().__init__(background_path, sound_path, scale)
