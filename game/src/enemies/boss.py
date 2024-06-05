import pygame
from game.src.enemies.enemies_base import Enemy
import game.src.constants as constants
from game.src.screen import screen_obj


class StalkingEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)


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


class Boss(StalkingEnemy):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.current_hp = constants.BOSS_HP