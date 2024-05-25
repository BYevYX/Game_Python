import pygame
import game.src.constants as constants
from game.src.screen import screen_obj


class Enemy(pygame.sprite.Sprite):
    images = []
    death_images = []

    def __init__(self, x, y, range_place=200 * screen_obj.width_scale, platform=None):
        super().__init__()
        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.ENEMY_NORMAL_SPEED * screen_obj.width_scale
        self.left = x
        self.right = x + range_place
        self.animation_count = 0
        self.death_animation_count = 0
        self.is_dead = False
        self.direction = "right"
        self.velocity = constants.VELOCITY * screen_obj.width_scale
        self.current_hp = constants.ENEMY_HP

    def change_direction(self, direction):
        if direction != self.direction:
            self.velocity *= -1
            self.direction = direction

    def move(self):
        if self.rect.x >= self.right:
            self.speed = -self.speed
        elif self.rect.x <= self.left:
            self.speed = abs(self.speed)

        self.rect.x += self.speed

    def update_animation(self):
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0

    def draw(self, screen):
        if self.speed < 0:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False), (self.rect.x, self.rect.y))
        else:
            screen.blit(self.images[self.animation_count], (self.rect.x, self.rect.y))

        self.update_animation()

    def death(self, group, screen):
        if self.current_hp <= 0:
            self.is_dead = True

            if len(self.death_images):
                screen.blit(self.death_images[self.death_animation_count], (self.rect.x, self.rect.y))
                self.death_animation_count += 1

            if self.death_animation_count == len(self.death_images):
                self.death_animation_count = 0
                group.remove(self)

    def update(self, screen, group):
        if not self.is_dead:
            self.move()
            self.draw(screen)

        self.death(group, screen)

    @staticmethod
    def move_group(direction, groups):
        for group in groups:
            for enemy in group:
                enemy.change_direction(direction)
                enemy.rect.x += enemy.velocity
                enemy.left += enemy.velocity
                enemy.right += enemy.velocity




class StalkingEnemy(Enemy):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)


    def stalk_update(self, player):
        # Вычисляем вектор направления к игроку
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max(1, abs(dx) + abs(dy))  # Чтобы избежать деления на ноль
        dx /= distance
        dy /= distance

        # Перемещаем врага в направлении игрока
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed


