import pygame


class Label():
    def __init__(self, width, height, font_path, size, text, color=(0, 0, 0), background_path=None):

        self.font = pygame.font.Font(font_path, size)
        self.text_surface = self.font.render(text, True, color)

        self.cursor = pygame.image.load("image/UI/cursor/cursor.png").convert_alpha()


        if background_path:
            self.background = pygame.image.load(background_path).convert_alpha()
            self.background_rect = self.text_surface.get_rect(topleft=((width - self.background.get_width()) / 2,
                                                                      (height - self.background.get_height()) / 2))
            self.rect = self.text_surface.get_rect(center=(width / 2, height / 2 - self.background.get_height() / 4))
        else:
            self.rect = self.text_surface.get_rect(center=(width / 2, height / 2 - 100))

    def draw(self, screen):
        if self.background:
            screen.blit(self.background, self.background_rect)

        screen.blit(self.text_surface, self.rect)

    def draw_cursor(self, screen):
        screen.blit(self.cursor, pygame.mouse.get_pos())




