"""
Module: game.src.button

This module defines a clickable button class `Button` for Pygame applications.

Attributes:
- x (int): The x-coordinate of the button's top-left corner.
- y (int): The y-coordinate of the button's top-left corner.
- width (int): The width of the button.
- height (int): The height of the button.
- text (str or None): Optional text displayed on the button.
- image (Surface): The main image displayed on the button.
- hover_image (Surface): The image displayed when the button is hovered over.
- rect (Rect): The rectangular area occupied by the button on the screen.
- sound (Sound or None): Optional sound played when the button is clicked.
- is_hovered (bool): Flag indicating if the mouse is currently hovering over the button.

Methods:
- __init__(self, x, y, width, height, image_path, text=None,
           hover_image_path=None, sound_path=None):
    Initializes a button with given attributes.

- draw(self, screen):
    Draws the button on a given Pygame screen.

- check_hover(self, mouse_pos):
    Checks if the mouse cursor is hovering over the button.

- handle_event(self, event):
    Handles Pygame events, specifically mouse clicks on the button.

- set_pos(self, x, y=None):
    Sets the position of the button on the screen.

Usage:
from game.src.button import Button
import pygame

# Example initialization of a button
button = Button(x=100, y=100, width=150, height=50,
                image_path="path/to/button_image.png",
                text="Click Me",
                hover_image_path="path/to/hover_image.png",
                sound_path="path/to/click_sound.wav")

# Example usage in a Pygame event loop
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        button.handle_event(event)

# Drawing the button on the screen
button.draw(screen)

Notes:
- Ensure that Pygame and necessary modules are
correctly imported and initialized before using this module.
- Provide paths to image and sound files to fully utilize button functionalities.
- Adjust the font and text rendering specifics according to your
game's requirements in the `draw` method.

"""
import pygame


class Button:
    """
        A class representing a clickable button in Pygame.

        Attributes:
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            text (str or None): Optional text displayed on the button.
            image (Surface): The main image displayed on the button.
            hover_image (Surface): The image displayed when the button is hovered over.
            rect (Rect): The rectangular area occupied by the button on the screen.
            sound (Sound or None): Optional sound played when the button is clicked.
            is_hovered (bool): Flag indicating if the mouse is currently hovering over the button.

        Methods:
            __init__(self, x, y, width, height, image_path, text=None,
                     hover_image_path=None, sound_path=None):
                Initializes a button with given attributes.

            draw(self, screen):
                Draws the button on a given Pygame screen.

            check_hover(self, mouse_pos):
                Checks if the mouse cursor is hovering over the button.

            handle_event(self, event):
                Handles Pygame events, specifically mouse clicks on the button.

            set_pos(self, x, y=None):
                Sets the position of the button on the screen.
        """

    def __init__(self, x, y, width, height, image_path, text=None, hover_image_path=None, sound_path=None):
        """
        Initialize a button object with position, size, images, optional text,
        hover image, and sound.

        :param x: The x-coordinate of the button's position.
        :param y: The y-coordinate of the button's position.
        :param width: The width of the button.
        :param height: The height of the button.
        :param image_path: The path to the button's image.
        :param text: Optional text to display on the button.
        :param hover_image_path: Optional path to the hover state image of the button.
        :param sound_path: Optional path to the sound to play on button click.
        :rtype: object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path).convert_alpha()
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))

        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, screen):
        """
        Draw the button on the screen.

        :param screen: The Pygame screen to draw the button on.
        :rtype: None
        """
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        if self.text:
            font = pygame.font.Font(None, 36)  # добавить шрифт
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """
        Check if the mouse is hovering over the button.

        :param mouse_pos: The current position of the mouse.
        :rtype: None
        """
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        """
        Handle the button click event and play the click sound if the button is clicked.

        :param event: The Pygame event to handle.
        :rtype: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

    def set_pos(self, x, y=None):
        """
        Set the position of the button.

        :param x: The new x-coordinate of the button.
        :param y: The new y-coordinate of the button. If None, the y-coordinate remains unchanged.
        :rtype: None
        """
        self.x = x
        if y:
            self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
