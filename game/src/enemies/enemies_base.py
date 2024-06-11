import pygame
import game.src.constants as constants
from game.src.screen import screen_obj


class Enemy(pygame.sprite.Sprite):
    images = None
    death_images = []

    def __init__(self, x, y):
        super().__init__()
        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.ENEMY_NORMAL_SPEED * screen_obj.width_scale
        self.animation_count = 0
        self.death_animation_count = 0
        self.is_dead = False
        self.velocity = constants.VELOCITY * screen_obj.width_scale
        self.velocity_direction = "right"
        self.current_hp = constants.ENEMY_HP
        self.const_delay_death_animation = 0
        self.delay_death_animation = 0
        self.const_delay_animation = 0
        self.delay_animation = 0
        self.damage = 1
        self.attack_direction = 1

        self.damage_texts = []
        self.font = pygame.font.Font(None, 30)

    def update_animation(self):
        if self.delay_animation == self.const_delay_animation:
            self.delay_animation = 0
            self.animation_count += 1
        else:
            self.delay_animation += 1

        if self.animation_count >= len(self.images):
            self.animation_count = 0

    def draw(self, screen):

        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False), (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images[self.animation_count], (self.rect.x, self.rect.y))

        for dmg, time in self.damage_texts:
            damage_surface = self.font.render(str(dmg), True, (139, 0, 0))
            screen.blit(damage_surface, (self.rect.x, self.rect.y - 30 - 10))

        self.update_animation()

    def take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
        self.current_hp -= damage
        self.damage_texts.append((damage, 30))

    def death(self, group, screen):
        if self.current_hp > 0:
            return

        self.is_dead = True
        if len(self.death_images):
            screen.blit(self.death_images[self.death_animation_count], (self.rect.x, self.rect.y))
            if self.delay_death_animation == self.const_delay_death_animation:
                self.delay_death_animation = 0
                self.death_animation_count += 1
            else:
                self.delay_death_animation += 1

        if self.death_animation_count == len(self.death_images):
            self.death_animation_count = 0
            group.remove(self)

    def change_direction(self, direction):
        if direction != self.velocity_direction:
            self.velocity *= -1
            self.velocity_direction = direction

    def update(self, screen, group, game=None):
        self.damage_texts = [(dmg, time - 1) for dmg, time in self.damage_texts if time > 0]

        if not self.is_dead:
            self.draw(screen)

        self.death(group, screen)

    @staticmethod
    def move_group(direction, groups):
        for group in groups:
            for enemy in group:
                enemy.change_direction(direction)
                enemy.rect.x += enemy.velocity

                if isinstance(enemy, CommonEnemy):
                    enemy.left += enemy.velocity
                    enemy.right += enemy.velocity


class CommonEnemy(Enemy):

    def __init__(self, x, y, range_place=200 * screen_obj.width_scale):
        super().__init__(x, y)

        self.left = x
        self.right = x + range_place

    def move(self):
        if self.rect.x >= self.right:
            self.speed = -self.speed
            self.attack_direction = -1
        elif self.rect.x <= self.left:
            self.speed = abs(self.speed)
            self.attack_direction = 1

        self.rect.x += self.speed

    def update(self, screen, group, game=None):
        super().update(screen, group)

        self.move()
