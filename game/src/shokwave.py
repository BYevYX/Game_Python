import pygame
from game.src.cache import ImageCache
from game.src.screen import screen_obj
import game.src.constants as constants



class Shockwave(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, direction=1, type="fireball"):
        super().__init__()
        self.velocity = pygame.Vector2(direction * dx, dy)
        self.damage_dealt = False
        self.direction = direction
        self.animation_count = 0

        if type == "fireball":
            image_paths = [f"image/enemys/fireball/1_{i}.png" for i in range(61)]
        else:
            image_paths = ["image/Heros/leaf_ranger/arrow/arrow_.png"]

        self.images = ImageCache.get_images(image_paths)

        self.main_velocity = constants.VELOCITY
        self.main_direction = 'right'

        image_rect = self.images[0].get_rect()
        image_rect.center = (x + 20 * screen_obj.width_scale, y - 15 * screen_obj.height_scale)

        rect_x = 20
        rect_y = 20

        small_rect_size = (rect_x * screen_obj.width_scale, rect_y * screen_obj.height_scale)
        self.position = [image_rect.x, image_rect.y]
        self.rect = pygame.Rect(0, 0, *small_rect_size)
        self.rect.center = image_rect.center

    def draw(self, screen):
        if self.direction == -1:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False),
                        self.position)
        elif self.direction == 1:
            screen.blit(self.images[self.animation_count], self.position)


        self.animation_count += 1
        if self.animation_count == len(self.images):
            self.animation_count = 0

    def update(self, screen, sprites, game, damage_to="player"):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.position[0] += self.velocity.x
        self.position[1] += self.velocity.y


        self.draw(screen)
        if damage_to == "player":
            self.deal_damage_player(game.player)
        else:
            self.deal_damage_enemy(game.enemies)


        if self.rect.x > screen_obj.width or self.rect.x < 0:
            self.kill()
            sprites.remove(self)

        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))


    def move_sprite(self, direction):
        if direction != self.main_direction:
            self.main_velocity *= -1
            self.main_direction = direction

        self.rect.x += self.main_velocity
        self.position[0] += self.main_velocity

    def deal_damage_player(self, player):
        if not self.damage_dealt:
            if pygame.sprite.collide_rect(self, player):
                player.take_damage()
                self.damage_dealt = True

    def deal_damage_enemy(self, enemies):
        if not self.damage_dealt:
            for group in enemies:
                for enemy in group:
                    if pygame.sprite.collide_rect(self, enemy):
                        enemy.take_damage()
                        self.damage_dealt = True
