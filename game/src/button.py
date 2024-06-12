import pygame


class Button:
    def __init__(self, x, y, width, height, image_path, text=None, hover_image_path=None, sound_path=None):
        """

        :rtype: object
        :param x:
        :param y:
        :param width:
        :param height:
        :param image_path:
        :param text:
        :param hover_image_path:
        :param sound_path:
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
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        if self.text:
            font = pygame.font.Font(None, 36)  # добавить шрифт
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

    def set_pos(self, x, y=None):
        self.x = x
        if y:
            self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
