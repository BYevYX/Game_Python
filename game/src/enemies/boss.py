import pygame
from game.src.enemies.enemies_base import Enemy
import game.src.constants as constants
from game.src.screen import screen_obj
from game.src.cache import ImageCache


class StalkingEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.can_fly = False


    def stalk_update(self, player):
        # Вычисляем вектор направления к игроку
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max(1, abs(dx) + abs(dy))  # Чтобы избежать деления на ноль
        dx /= distance
        dy /= distance

        # Перемещаем врага в направлении игрока
        self.rect.x += dx * self.speed

        if self.can_fly:
            self.rect.y += dy * self.speed


class Boss(StalkingEnemy):

    def __init__(self, x, y, image_paths_idle=None, image_paths_run=None, image_paths_attack=None):
        if not image_paths_idle:
            image_paths_idle = [f"image/enemys/boss/idle/hooded knight idle {i}.png" for i in range(1, 9)]

        if not image_paths_run:
            image_paths_run = []
            for i in range(1, 9):
                image_paths_run.append(f"image/enemys/boss/idle/hooded knight idle {i}.png")
                image_paths_run.append(f"image/enemys/boss/idle/run-idle transition {i % 2 + 1}.png")

        if not image_paths_attack:
            image_paths_attack = [f"image/enemys/boss/attack/hooded knight attack_{i}.png" for i in range(1, 18)]

        self.images = ImageCache.get_images(image_paths_idle)
        self.images_idle = ImageCache.get_images(image_paths_idle)
        self.images_attack = ImageCache.get_images(image_paths_attack)

        super().__init__(x, y)
        self.current_hp = constants.BOSS_HP
        self.max_hp = self.current_hp

        self.is_create_gates = True

    def take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
        super().take_damage(damage)
        if self.current_hp < 0:
            self.current_hp = 0

    def draw_boss_hp_bar(self, screen):
        ratio = self.current_hp / self.max_hp
        x = 100 * screen_obj.width_scale
        y = 70 * screen_obj.height_scale
        width = screen_obj.width - 200 * screen_obj.width_scale
        height = 15 * screen_obj.height_scale

        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width * ratio, height))

    def death(self, group, screen):
        super().death(group, screen)

    def update(self, screen, group, game=None):
        super().update(screen, group)
        self.stalk_update(game.player)

        if self.current_hp > 0:
            self.draw_boss_hp_bar(screen)
        else:
            if self.is_create_gates:
                for gate in game.gates:
                    game.platforms.remove(gate)

                game.gates.clear()



