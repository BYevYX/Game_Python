import pygame
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import game.src.constants as constants



class Shockwave(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, direction=1):
        super().__init__()
        self.image = pygame.Surface((40, 70), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(direction * dx, dy)
        self.damage_dealt = False
        self.direction = direction
        self.animation_count = 0

        image_paths = [f"image/enemys/fireball/1_{i}.png" for i in range(61)]
        self.images = ImageCache.get_images(image_paths)

        self.main_velocity = constants.VELOCITY
        self.main_direction = 'right'

    def draw(self, screen):
        if self.direction == -1:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.direction == 1:
            screen.blit(self.images[self.animation_count], (self.rect.x, self.rect.y))


        self.animation_count += 1
        if self.animation_count == len(self.images):
            self.animation_count = 0

    def update(self, screen, sprites, player):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.draw(screen)

        self.deal_damage_player(player)

        if self.rect.x > screen_obj.width or self.rect.x < 0:
            self.kill()
            sprites.remove(self)


    def move_sprite(self, direction):
        if direction != self.main_direction:
            self.main_velocity *= -1
            self.main_direction = direction

        self.rect.x += self.main_velocity

    def deal_damage_player(self, player):
        if not self.damage_dealt:
            if pygame.sprite.collide_rect(self, player):
                player.take_damage()
                self.damage_dealt = True
