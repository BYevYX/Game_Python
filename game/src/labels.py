import pygame


class Label:
    def __init__(self, width, height, font_path, size, text, color=(0, 0, 0), background_path=None):
        """
        Initialize a Label object.

        :param width: The width of the label's bounding box.
        :param height: The height of the label's bounding box.
        :param font_path: The path to the font file to be used for the label's text.
        :param size: The size of the font.
        :param text: The text to be displayed on the label.
        :param color: The color of the text (default is black).
        :param background_path: The path to the background image file (optional).
        :rtype: object
        """
        self.font = pygame.font.Font(font_path, size)
        self.text_surface = self.font.render(text, True, color)

        self.cursor = pygame.image.load("image/UI/cursor/cursor.png").convert_alpha()

        if background_path:
            self.background = pygame.image.load(background_path).convert_alpha()
            self.background_rect = self.text_surface.get_rect(topleft=((width - self.background.get_width()) / 2,
                                                                       (height - self.background.get_height()) / 2))
            self.rect = self.text_surface.get_rect(center=(width / 2, height / 2 - self.background.get_height() / 4))
        else:
            self.background = None
            self.rect = self.text_surface.get_rect(center=(width / 2, height / 2 - 100))

    def draw(self, screen):
        """
        Draw the label on the screen.

        :param screen: The screen surface to draw the label on.
        :rtype: None
        """
        if self.background:
            screen.blit(self.background, self.background_rect)

        screen.blit(self.text_surface, self.rect)

    def draw_cursor(self, screen):
        """
        Draw the custom cursor on the screen.

        :param screen: The screen surface to draw the cursor on.
        :rtype: None
        """
        screen.blit(self.cursor, pygame.mouse.get_pos())
