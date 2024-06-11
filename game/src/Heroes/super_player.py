import pygame
from game.src.Heroes.player import Player
from game.src.screen import screen_obj



class SuperPlayer(Player):
    def __init__(self, x, y, rect_x, rect_y):
        super().__init__(x, y)

        image_rect = self.run[0].get_rect()
        # Центрирование изображения
        image_rect.center = (screen_obj.width // 2, screen_obj.height - 200 * screen_obj.height_scale)

        small_rect_size = (rect_x * screen_obj.width_scale, rect_y * screen_obj.height_scale)
        self.rect = pygame.Rect(0, 0, *small_rect_size)
        self.rect.center = image_rect.center

        self.dx = self.run[0].get_width() // 2 - rect_x // 2 * screen_obj.width_scale
        self.dy = self.run[0].get_height() - rect_y * screen_obj.height_scale

    def draw(self, screen, keys, position=None):
        super().draw(screen, keys, (self.rect.x - self.dx, self.rect.y - self.dy))