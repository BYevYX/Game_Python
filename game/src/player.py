import pygame
from game.src.screen import screen_obj
import game.src.constants as constants
from game.src.enemies.enemies_base import Enemy


class Player(pygame.sprite.Sprite):

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
        self.delay_animation = 0

        self.is_attacking = False
        self.attack_cooldown = constants.PLAYER_ATTACK_COOLDOWN
        self.last_attack_time = 0
        self.attack_range = constants.PLAYER_ATTACK_RANGE * screen_obj.width_scale
        self.attack_damage = constants.PLAYER_ATTACK_DAMAGE

        self.is_jump = False
        self.on_ground = True
        self.jump_height = constants.PLAYER_JUMP_HEIGHT * screen_obj.height_scale
        self.y_velocity = 0
        self.max_fall_speed = constants.PLAYER_MAX_FALL_SPEED * screen_obj.height_scale

        self.can_left = True
        self.can_right = True

        self.hp_image = (
            pygame.transform.scale(pygame.image.load('image/Hero/heart/Empty_heart.png').convert_alpha(),
                                   (16 * self.heart_scale, 15 * self.heart_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/heart/Heart.png').convert_alpha(),
                                   (12 * self.heart_scale, 11 * self.heart_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/heart/Metal_heart.png').convert_alpha(),
                                   (12 * self.heart_scale, 11 * self.heart_scale))
        )

        self.run = (
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-1.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-2.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-3.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-4.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-5.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-6.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-7.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-8.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-9.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-10.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-11.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Run/run-12.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
        )

        self.stay_images = (
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-1.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-2.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-3.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-4.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-5.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/stay/idle-6.png').convert_alpha(),
                                                    (23 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
        )

        self.jump = (
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-1.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-2.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-3.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-4.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-5.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-6.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-7.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-8.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-9.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-10.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-11.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-12.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-13.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Jump/jump-14.png').convert_alpha(),
                                                    (31 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
        )

        self.attack_images = (
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A1.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A2.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A3.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A4.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A5.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
            pygame.transform.scale(pygame.image.load('image/Hero/Attack/attack-A6.png').convert_alpha(),
                                                    (38 * 1.2 * screen_obj.width_scale, 60 * 1.2 * screen_obj.height_scale)),
        )

        self.rect = self.run[0].get_rect(topleft=(self.x, self.y))

    def animate_hp(self, screen):
        for i in range(self.hp):
            screen.blit(self.hp_image[0], (40 + i * 50, 30))
            if i < self.current_hp:
                screen.blit(self.hp_image[1], (2 * self.heart_scale + 40 + i * 50, 30 + 2 * self.heart_scale))

    def check_animation_count(self):
        self.delay_animation += 1

        if self.run_animation_count == len(self.run) - 1:
            self.run_animation_count = 0
        else:
            self.run_animation_count += 1

        if self.delay_animation == 2:
            self.delay_animation = 0

            if self.stay_animation_count == len(self.stay_images) - 1:
                self.stay_animation_count = 0
            else:
                self.stay_animation_count += 1

            if self.jump_animation_count == len(self.jump) - 1:
                self.jump_animation_count = 0
            elif self.is_jump:
                self.jump_animation_count += 1

            if self.attack_animation_count == len(self.attack_images) - 1:
                self.attack_animation_count = 0
                self.is_attacking = False
            elif self.is_attacking:
                self.attack_animation_count += 1



    # def sliding_window(self):
    #
    #     if self.speed < 5 and screen_obj.width // 2 - 115 <= self.x <= screen_obj.width // 2 + 120:
    #         self.speed += 1
    #     elif self.speed > 0 and (self.x <= screen_obj.width // 2 - 100 or self.x >= screen_obj.width // 2 + 100):
    #         self.speed -= 1

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

    def attack(self, enemies):
        self.last_attack_time = pygame.time.get_ticks()

        attack_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width + self.attack_range, self.rect.height)
        for group in enemies:
            for enemy in group:
                if attack_rect.colliderect(enemy.rect):
                    enemy.current_hp -= self.attack_damage

    def draw(self, screen, keys):
        self.animate_hp(screen)

        if self.is_attacking:
            if self.attack_direction == 1:
                screen.blit(self.attack_images[self.attack_animation_count], (self.x, self.y))
            else:
                screen.blit(pygame.transform.flip(self.attack_images[self.attack_animation_count], True, False), (self.x, self.y))
        elif not self.is_jump:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > screen_obj.width * 0.03:
                screen.blit(pygame.transform.flip(self.run[self.run_animation_count], True, False), (self.x, self.y))
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < screen_obj.width * 0.97:
                screen.blit(self.run[self.run_animation_count], (self.x, self.y))
            else:
                screen.blit(self.stay_images[self.stay_animation_count], (self.x, self.y))
        else:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > screen_obj.width * 0.03:
                screen.blit(pygame.transform.flip(self.jump[self.jump_animation_count], True, False), (self.x, self.y))
            else:
                screen.blit(self.jump[self.jump_animation_count], (self.x, self.y))

        self.check_animation_count()

    @staticmethod
    def move_environment(direction, main_location, partial_backgrounds, platforms, enemies):
        main_location.move_background(direction)
        for platform in platforms:
            platform.move_platforms(direction)

        for part_back in partial_backgrounds:
            part_back.move_background(direction)

        Enemy.move_group(direction, enemies)

    def move(self, keys, main_location, partial_backgrounds, platforms, enemies):
        self.correction()
        # self.sliding_window()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.can_left:
            self.can_right = True
            self.attack_direction = -constants.PLAYER_ATTACK_DIRECTION

            Player.move_environment("left", main_location, partial_backgrounds, platforms, enemies)

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.can_right:
            self.can_left = True
            self.attack_direction = constants.PLAYER_ATTACK_DIRECTION

            Player.move_environment("right", main_location, partial_backgrounds, platforms, enemies)

        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and not self.is_jump:
            self.is_jump = True
            self.on_ground = False
            self.y_velocity = -self.jump_height

        if keys[pygame.K_f] and not self.is_attacking and pygame.time.get_ticks() - self.last_attack_time > self.attack_cooldown:
            self.is_attacking = True
            self.attack(enemies)

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

    def update(self, screen, main_location, partial_backgrounds, platforms, enemies):
        keys = pygame.key.get_pressed()

        self.move(keys, main_location, partial_backgrounds, platforms, enemies)
        self.check_collisions(platforms)
        self.draw(screen, keys)


