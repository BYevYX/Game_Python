import pygame


class Shockwave(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, direction=1):
        super().__init__()
        self.x = x
        self.image = pygame.Surface((40, 70), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(dx, dy)
        self.damage_dealt = False  # Флаг для проверки, нанесен ли урон

        # Рисуем полумесяц желтого цвета
        self.image.fill((0, 0, 0, 0))  # Очистка поверхности

        if direction == 1:
            pygame.draw.arc(self.image, (255, 255, 0), self.image.get_rect(), -3.14/2, 3.14/2, 5)  # Полумесяц
        elif direction == -1:
            pygame.draw.arc(self.image, (255, 255, 0), self.image.get_rect(), 3.14/2, -3.14/2, 5)  # Полумесяц

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Удаляем волну, если она выходит за пределы экрана
        if self.rect.x > self.x + 50 or self.rect.x < self.x - 100:
            self.kill()

    def deal_damage(self, enemies):
        if not self.damage_dealt:
            for enemy_group in enemies:
                for enemy in enemy_group:
                    if pygame.sprite.collide_rect(self, enemy):
                        enemy.take_damage()
                        self.damage_dealt = True  # Устанавливаем флаг, что урон нанесен
                        break
