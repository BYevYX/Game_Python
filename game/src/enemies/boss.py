import pygame

import game.src.constants as constants
from game.src.cache import ImageCache
from game.src.enemies.enemies_base import Enemy
from game.src.screen import screen_obj
from game.src.shokwave import Shockwave


class StalkingEnemy(Enemy):
    def __init__(self, x, y):
        """

        :param x: 
        :param y: 
        :rtype: object
        """
        super().__init__(x, y)
        self.can_fly = False
        self.distance = 0

    def stalk_update(self, player):
        """

        :rtype: object
        :param player: 
        """
        # Вычисляем вектор направления к игроку
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max(1, abs(dx) + abs(dy))  # Чтобы избежать деления на ноль
        self.distance = distance
        dx /= distance
        dy /= distance

        if dx < 0:
            self.attack_direction = -1
        else:
            self.attack_direction = 1

        # Перемещаем врага в направлении игрока
        self.rect.x += dx * self.speed

        if self.can_fly:
            self.rect.y += dy * self.speed


class Boss(StalkingEnemy):

    def __init__(self, x, y, image_paths_idle=None, image_paths_run=None, image_paths_attack=None,
                 image_paths_death=None, image_paths_hit=None):
        """

        :rtype: object
        :param x: 
        :param y: 
        :param image_paths_idle: 
        :param image_paths_run: 
        :param image_paths_attack: 
        :param image_paths_death: 
        :param image_paths_hit: 
        """
        if not image_paths_idle:
            image_paths_idle = [f"image/enemys/boss/idle/Idle_{i}.png" for i in range(1, 9)]

        if not image_paths_run:
            image_paths_run = [f"image/enemys/boss/move/Move_{i}.png" for i in range(1, 9)]

        if not image_paths_attack:
            image_paths_attack = [f"image/enemys/boss/attack/Attack_{i}.png" for i in range(1, 9)]

        if not image_paths_death:
            image_paths_death = [f"image/enemys/boss/death/Death_{i}.png" for i in range(1, 6)]

        if not image_paths_hit:
            image_paths_hit = [f"image/enemys/boss/hit/Take Hit_{i}.png" for i in range(1, 5)]

        self.images = ImageCache.get_images(image_paths_run, (1.8, 1.8))
        self.images_idle = ImageCache.get_images(image_paths_idle, (1.8, 1.8))
        self.images_attack = ImageCache.get_images(image_paths_attack, (1.8, 1.8))
        self.death_images = ImageCache.get_images(image_paths_death, (1.8, 1.8))

        super().__init__(x, y)
        self.images_hit = ImageCache.get_images(image_paths_hit, (1.8, 1.8))
        self.current_hp = constants.BOSS_HP
        self.max_hp = self.current_hp

        self.is_create_gates = True
        self.is_stop = False
        self.stop_timer = 90
        self.current_stop_timer = 0

        self.const_delay_animation = 3
        self.const_delay_death_animation = 3

        self.idle_animation_count = 0
        self.is_hit = False
        self.hit_animation_count = 0
        self.attack_animation_count = 0

        self.attacking = None

        self.fireballs = pygame.sprite.Group()

    def take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
        """

        :param damage: 
        :rtype: None
        """
        super().take_damage(damage)
        self.is_hit = True
        if self.current_hp < 0:
            self.current_hp = 0

    def fireball_attack(self):
        """

        :rtype: None
        """
        if not self.is_stop:
            return

        if self.current_stop_timer % (self.stop_timer - 10) == 0:
            fireball = Shockwave(self.rect.centerx, self.rect.centery, 5, 0, self.attack_direction, 'fireball')
            self.fireballs.add(fireball)

    def move_sprites(self, direction):
        """

        :rtype: None
        :param direction:
        """
        for fireball in self.fireballs:
            fireball.move_sprite(direction)

    def update_animation(self):
        """
        :rtype: None

        """
        super().update_animation()

        if self.delay_animation == 0:
            self.hit_animation_count += 1
            self.attack_animation_count += 1

        if self.hit_animation_count >= len(self.images_hit):
            self.hit_animation_count = 0
            self.is_hit = False

        if self.attack_animation_count >= len(self.images_attack):
            self.attack_animation_count = 0

    def attack(self, screen):
        """

        :rtype: None
        :param screen:
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_attack[self.attack_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_attack[self.attack_animation_count], (self.rect.x, self.rect.y))

    def idle(self, screen):
        """

        :rtype: None
        :param screen:
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_idle[self.idle_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_idle[self.idle_animation_count], (self.rect.x, self.rect.y))

    def draw(self, screen):
        """

        :rtype: None
        :param screen:
        """
        if self.is_hit:
            self.draw_hit(screen)
            return

        if not self.is_stop:
            super().draw(screen)
            return

        if self.distance > 250:
            self.idle(screen)
        else:
            self.attack(screen)

        self.update_animation()

    def draw_boss_hp_bar(self, screen):
        """

        :rtype: None
        :param screen:
        """
        ratio = self.current_hp / self.max_hp
        x = 100 * screen_obj.width_scale
        y = 70 * screen_obj.height_scale
        width = screen_obj.width - 200 * screen_obj.width_scale
        height = 15 * screen_obj.height_scale

        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width * ratio, height))

    def draw_hit(self, screen):
        """

        :rtype: None
        :param screen:
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_hit[self.hit_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_hit[self.hit_animation_count], (self.rect.x, self.rect.y))

        if self.delay_animation == self.const_delay_animation:
            self.hit_animation_count += 1

        if self.hit_animation_count >= len(self.images_hit):
            self.hit_animation_count = 0
            self.is_hit = False

        self.update_animation()

    def update(self, screen, group, game=None):
        """

        :rtype: None
        :param screen:
        :param group:
        :param game:
        """
        super().update(screen, group)

        if not self.is_stop and not self.is_hit:
            self.stalk_update(game.player)

        self.fireball_attack()
        self.fireballs.update(screen, self.fireballs, game)

        self.current_stop_timer += 1
        if self.current_stop_timer == self.stop_timer:
            self.current_stop_timer = 0
            self.is_stop = not self.is_stop

        if self.current_hp > 0:
            self.draw_boss_hp_bar(screen)
        else:
            if self.is_create_gates:
                for gate in game.gates:
                    game.platforms.remove(gate)

                game.gates.empty()
