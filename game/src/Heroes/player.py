import time

import pygame

import game.src.constants as constants
from game.src.enemies.enemies_base import CommonEnemy
from game.src.screen import screen_obj


class Player(pygame.sprite.Sprite):
    run = []
    stay_images = []
    jump = []
    attack_1 = []

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.attack_direction = constants.PLAYER_ATTACK_DIRECTION
        self.hp = constants.PLAYER_HP_COUNT
        self.current_hp = self.hp
        self.heart_scale = constants.PLAYER_HEART_IMAGE_SCALE

        self.run_animation_count = 0
        self.stay_animation_count = 0
        self.jump_animation_count = 0
        self.attack_animation_count = 0

        self.const_delay_animation = 0
        self.const_delay_jump_animation = 0
        self.delay_animation = self.const_delay_animation
        self.delay_jump_animation = self.const_delay_jump_animation

        self.is_attacking = False
        self.attack_cooldown = constants.PLAYER_ATTACK_COOLDOWN
        self.last_attack_time = 0
        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE
        self.knockback = constants.PLAYER_MAIN_KNOCKBACK

        self.invincible = False
        self.invincibility_duration = constants.PLAYER_INVISIBILITY_DURATION  # В секундах
        self.last_hit_time = 0

        self.is_jump = False
        self.on_ground = True
        self.jump_height = constants.PLAYER_JUMP_HEIGHT * screen_obj.height_scale
        self.y_velocity = 0
        self.max_fall_speed = constants.PLAYER_MAX_FALL_SPEED * screen_obj.height_scale

        self.can_left = True
        self.can_right = True

        self.coins = 200
        self.inventory = []

        self.hp_image = (
            pygame.transform.scale(pygame.image.load('image/Heros/heart/Empty_heart.png').convert_alpha(),
                                   (16 * self.heart_scale, 15 * self.heart_scale)),
            pygame.transform.scale(pygame.image.load('image/Heros/heart/Heart.png').convert_alpha(),
                                   (12 * self.heart_scale, 11 * self.heart_scale)),
            pygame.transform.scale(pygame.image.load('image/Heros/heart/Metal_heart.png').convert_alpha(),
                                   (12 * self.heart_scale, 11 * self.heart_scale))
        )

        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def animate_hp(self, screen):
        for i in range(self.hp):
            screen.blit(self.hp_image[0], (40 + i * 50, 30))
            if i < self.current_hp:
                screen.blit(self.hp_image[1], (2 * self.heart_scale + 40 + i * 50, 30 + 2 * self.heart_scale))

    def check_animation_count(self):
        self.delay_animation += 1
        self.delay_jump_animation += 1

        if self.delay_animation == self.const_delay_animation:
            self.delay_animation = 0

            if self.run_animation_count == len(self.run) - 1:
                self.run_animation_count = 0
            else:
                self.run_animation_count += 1

            if self.stay_animation_count == len(self.stay_images) - 1:
                self.stay_animation_count = 0
            else:
                self.stay_animation_count += 1

            if self.attack_animation_count == len(self.attack_1) - 1:
                self.attack_animation_count = 0
                self.is_attacking = False
            elif self.is_attacking:
                self.attack_animation_count += 1

        if self.delay_jump_animation == self.const_delay_jump_animation:
            self.delay_jump_animation = 0

            if self.jump_animation_count == len(self.jump) - 1:
                self.jump_animation_count = 0
            elif self.is_jump:
                self.jump_animation_count += 1
            else:
                self.jump_animation_count = 0

    def correction(self):
        if not self.can_right and not self.can_left:
            self.can_left = True
            self.can_right = True

        if self.x == screen_obj.width // 2:
            return

        if self.x > screen_obj.width // 2:
            self.x -= 1

        else:
            self.x += 1

    def take_damage(self, damage=1, enemy=None):
        current_time = time.time()
        if not self.invincible:
            self.current_hp -= damage
            self.invincible = True
            self.last_hit_time = current_time

            if enemy:
                if self.rect.left <= enemy.rect.left:
                    self.x -= self.knockback
                elif self.rect.right >= enemy.rect.right:
                    self.x += self.knockback

                if self.rect.bottom <= enemy.rect.bottom:
                    self.y -= self.knockback
                elif self.rect.top >= enemy.rect.top:
                    self.y += self.knockback

    def check_invincibility(self):
        current_time = time.time()
        if self.invincible and (current_time - self.last_hit_time) > self.invincibility_duration:
            self.invincible = False

    def blink(self, image):
        if self.invincible:
            # Мерцание
            current_time = time.time()
            if int(current_time * 10) % 2 == 0:
                image.set_alpha(255)  # Полностью видимый
            else:
                image.set_alpha(0)  # Полностью прозрачный
        else:
            image.set_alpha(255)  # Полностью видимый в обычном состоянии

    def check_damage(self, enemies):
        for group_enemies in enemies:
            collided_enemy = pygame.sprite.spritecollideany(self, group_enemies)
            if collided_enemy:
                self.take_damage(collided_enemy.damage, collided_enemy)

    def attack(self, enemies):
        self.last_attack_time = pygame.time.get_ticks()

        if self.attack_direction == 1:

            attack_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width + self.attack_range, self.rect.height)
        else:
            attack_rect = pygame.Rect(self.rect.x, self.rect.y, -self.attack_range, self.rect.height)

        for group in enemies:
            for enemy in group:
                if attack_rect.colliderect(enemy.rect):
                    enemy.take_damage(self.attack_damage)

    def draw(self, screen, keys, position=None):
        self.animate_hp(screen)

        if not position:
            position = (self.x, self.y)

        if self.is_attacking:
            if self.attack_direction == 1:
                image = self.attack_1[self.attack_animation_count]
                self.blink(image)
                screen.blit(image, position)
            else:
                image = pygame.transform.flip(self.attack_1[self.attack_animation_count], True, False)
                self.blink(image)
                screen.blit(image, position)
        elif not self.is_jump:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > screen_obj.width * 0.03:
                image = pygame.transform.flip(self.run[self.run_animation_count], True, False)
                self.blink(image)
                screen.blit(image, position)
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < screen_obj.width * 0.97:
                image = self.run[self.run_animation_count]
                self.blink(image)
                screen.blit(image, position)
            else:
                if self.attack_direction == 1:
                    image = self.stay_images[self.stay_animation_count]
                else:
                    image = pygame.transform.flip(self.stay_images[self.stay_animation_count], True, False)

                self.blink(image)
                screen.blit(image, position)
        else:
            if self.attack_direction == -1:
                image = pygame.transform.flip(self.jump[self.jump_animation_count], True, False)
                self.blink(image)
                screen.blit(image, position)
            else:
                image = self.jump[self.jump_animation_count]
                self.blink(image)
                screen.blit(image, position)

        self.check_animation_count()

    @staticmethod
    def move_environment(direction, game):
        game.main_location.move_background(direction)
        for platform in game.platforms:
            platform.move_platform(direction)

        for part_back in game.partial_backgrounds:
            part_back.move_background(direction)

        for npc in game.npcs:
            npc.move_npc(direction)

        CommonEnemy.move_group(direction, game.enemies)

        if game.bosses:
            for boss in game.bosses:
                boss.move_sprites(direction)

    def move(self, keys, game):
        self.correction()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.can_left:
            self.can_right = True
            self.attack_direction = -constants.PLAYER_ATTACK_DIRECTION
            game.change_absolute_x(constants.VELOCITY)

            Player.move_environment("left", game)

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.can_right:
            self.can_left = True
            self.attack_direction = constants.PLAYER_ATTACK_DIRECTION
            game.change_absolute_x(-constants.VELOCITY)

            Player.move_environment("right", game)

        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and not self.is_jump:
            self.is_jump = True
            self.on_ground = False
            self.y_velocity = -self.jump_height

        if keys[
            pygame.K_f] and not self.is_attacking and pygame.time.get_ticks() - self.last_attack_time > self.attack_cooldown:
            self.is_attacking = True
            self.attack(game.enemies)

        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

        if not self.on_ground:
            if self.y_velocity < self.max_fall_speed:
                self.y_velocity += constants.GRAVITY * screen_obj.height_scale ** 0.8

            self.y += self.y_velocity

    def check_collisions(self, platforms):
        player_rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

        self.on_ground = False

        for platform in platforms:
            if player_rect.colliderect(platform.rect):

                if self.y_velocity > 0 and platform.rect.y > self.y + self.rect.height // 10:  # Падение
                    self.y = platform.rect.top - self.rect.height
                    self.is_jump = False
                    self.y_velocity = 0
                    self.on_ground = True

                elif self.y_velocity < 0:  # Прыжок вверх
                    self.y = platform.rect.bottom
                    self.y_velocity = 0

                else:
                    # Определяем сторону столкновения
                    if self.x <= platform.rect.x:  # Столкновение с левой стороны платформы
                        if platform.rect.y < self.y + self.rect.height // 10:
                            self.x = platform.rect.x - self.rect.width
                            self.can_right = False

                    else:  # Столкновение с правой стороны платформы
                        self.x = platform.rect.right
                        self.can_left = False

    def update(self, screen, game):
        keys = pygame.key.get_pressed()

        self.move(keys, game)
        self.check_collisions(game.platforms)
        self.draw(screen, keys)
        self.check_damage(game.enemies)
        self.check_invincibility()

        # pygame.draw.rect(screen, (255, 255, 255), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
