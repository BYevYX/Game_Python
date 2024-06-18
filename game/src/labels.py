"""
This module provides a Label class
for creating text labels with optional background and custom cursor using Pygame.

Classes:
- Label:
    Represents a text label with customizable font, text color, background, and cursor.

    Attributes:
    - font (pygame.font.Font): Font object for rendering the label's text.
    - text_surface (pygame.Surface): Surface containing the rendered text.
    - cursor (pygame.Surface): Surface containing the custom cursor image.
    - background (pygame.Surface or None): Optional background image surface for the label.
    - background_rect (pygame.Rect or None):
        Rectangle object defining background image's position and size.
    - rect (pygame.Rect): Rectangle object defining the label's position and size on the screen.

    Methods:
    - __init__(width, height, font_path, size, text, color=(0, 0, 0), background_path=None):
        Initializes a Label object with specified dimensions, font, text, color,
        and optional background image.
    - draw(screen):
        Draws the label on the specified screen surface.
    - draw_cursor(screen):
        Draws the custom cursor image at the current mouse position on the specified screen.

Dependencies:
- External dependencies:
  - pygame: Library for game development in Python with multimedia capabilities.
"""

import pygame


class Label:
    """
    Label class represents a text label with optional background and custom cursor.

    Attributes:
        font (pygame.font.Font): Font object for the label's text.
        text_surface (pygame.Surface): Surface containing the rendered text.
        cursor (pygame.Surface): Surface containing the custom cursor image.
        background (pygame.Surface or None): Surface containing the background image (optional).
        background_rect (pygame.Rect or None):
            Rectangle object for the background image's position and size.
        rect (pygame.Rect): Rectangle object for the label's position and size.

    Methods:
        __init__(width, height, font_path, size, text, color=(0, 0, 0), background_path=None):
            Initializes a Label object.
        draw(screen):
            Draws the label on the screen.
        draw_cursor(screen):
            Draws the custom cursor on the screen.
    """

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
        """
        self.font = pygame.font.Font(font_path, size)
        self.text_surface = self.font.render(text, True, color)
        self.cursor = pygame.image.load("image/UI/cursor/cursor.png").convert_alpha()

        if background_path:
            self.background = (
                pygame.image.load(background_path).convert_alpha())
            self.background_rect = self.text_surface.get_rect(
                topleft=((width - self.background.get_width()) / 2,
                         (height - self.background.get_height()) / 2))
            self.rect = self.text_surface.get_rect(
                center=(width / 2, height / 2 - self.background.get_height() / 4))
        else:
            self.background = None
            self.rect = self.text_surface.get_rect(center=(width / 2, height / 2 - 100))

    def draw(self, screen):
        """
        Draw the label on the screen.

        :param screen: The screen surface to draw the label on.
        """
        if self.background:
            screen.blit(self.background, self.background_rect)

        screen.blit(self.text_surface, self.rect)

    def draw_cursor(self, screen):
        """
        Draw the custom cursor on the screen.

        :param screen: The screen surface to draw the cursor on.
        """
        screen.blit(self.cursor, pygame.mouse.get_pos())
