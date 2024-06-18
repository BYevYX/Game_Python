"""
This module defines enemies for a Pygame-based game.

Classes:
- StalkingEnemy(Enemy): Represents an enemy that stalks the player.
- Boss(StalkingEnemy): Represents a boss enemy inheriting from StalkingEnemy.

Attributes:
- constants (module): Constants and configurations for the game.
- ImageCache (class): Caches and manages images for efficient loading.
- pygame (module): Library for game development in Python.
- screen_obj (module): Screen configuration and scaling information.
- Shockwave (class): Represents projectiles or special attacks.

StalkingEnemy Class:
Represents an enemy that moves towards the player.

Attributes:
- can_fly (bool): Indicates if the enemy can fly.
- distance (float): Distance between the enemy and the player.

Methods:
- __init__(self, x, y):
    Initializes the StalkingEnemy with initial coordinates (x, y).
- stalk_update(self, player):
    Updates the enemy's position based on the player's location.

Boss Class:
Represents a boss enemy that inherits from StalkingEnemy.

Attributes:
- images (list): List of pygame.Surface objects for running animation.
- images_idle (list): List of pygame.Surface objects for idle animation.
- images_attack (list): List of pygame.Surface objects for attack animation.
- death_images (list): List of pygame.Surface objects for death animation.
- images_hit (list): List of pygame.Surface objects for hit animation.
- current_hp (int): Current hit points of the boss.
- max_hp (int): Maximum hit points of the boss.
- is_create_gates (bool): Flag indicating if gates should be created upon death.
- is_stop (bool): Flag indicating if the boss is currently stopped.
- stop_timer (int): Duration for which the boss remains stopped.
- current_stop_timer (int): Current timer count for stop duration.
- const_delay_animation (int): Constant delay between animation frames.
- const_delay_death_animation (int): Constant delay between death animation frames.
- idle_animation_count (int): Current frame index for idle animation.
- is_hit (bool): Flag indicating if the boss is currently hit.
- hit_animation_count (int): Current frame index for hit animation.
- attack_animation_count (int): Current frame index for attack animation.
- attacking (None or object): Object representing the current attack state.
- fireballs (pygame.sprite.Group): Group of Shockwave objects representing fireball attacks.

Methods:
- __init__(self, x, y, image_paths_idle=None, image_paths_run=None, image_paths_attack=None,
           image_paths_death=None, image_paths_hit=None):
    Initializes the Boss with initial coordinates (x, y) and optional image paths for animations.
- take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
    Reduces the boss's current hit points by a specified amount and sets hit animation.
- fireball_attack(self):
    Initiates a fireball attack if the boss is not stopped.
- move_sprites(self, direction):
    Moves all fireballs in the specified direction.
- update_animation(self):
    Updates the boss's animation frames based on the delay.
- attack(self, screen):
    Draws the boss's attack animation on the screen.
- idle(self, screen):
    Draws the boss's idle animation on the screen.
- draw(self, screen):
    Draws the boss on the screen based on its current state.
- draw_boss_hp_bar(self, screen):
    Draws the boss's health bar on the screen.
- draw_hit(self, screen):
    Draws the boss's hit animation on the screen and updates the animation frame.
- update(self, screen, group, game=None):
    Updates the boss's state, movement, and animations.
"""

from game.src import constants
from game.src.cache import ImageCache
from game.src.enemies.enemies_base import Enemy
from game.src.screen import screen_obj
from game.src.shokwave import Shockwave
import pygame


class StalkingEnemy(Enemy):
    """
    Represents a stalking enemy in the game, which moves towards the player.

    Attributes:
        can_fly (bool): Indicates if the enemy can fly.
        distance (float): Distance between the enemy and the player.

    Methods:
        __init__(self, x, y):
            Initializes the StalkingEnemy with initial coordinates (x, y).

        stalk_update(self, player):
            Updates the enemy's position based on the player's location.

    """

    def __init__(self, x, y):
        """
        Initializes the StalkingEnemy with initial coordinates (x, y).

        Args:
            x (int): Initial x-coordinate of the StalkingEnemy.
            y (int): Initial y-coordinate of the StalkingEnemy.
        """
        super().__init__(x, y)
        self.can_fly = False
        self.distance = 0

    def stalk_update(self, player):
        """
        Updates the enemy's position based on the player's location.

        Args:
            player (pygame.sprite.Sprite): The player object to stalk.
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

        self.rect.x += dx * self.speed

        if self.can_fly:
            self.rect.y += dy * self.speed


class Boss(StalkingEnemy):
    """
    Represents a boss enemy in the game, which inherits from StalkingEnemy.

    Attributes:
        images (list): List of pygame.Surface objects for running animation.
        images_idle (list): List of pygame.Surface objects for idle animation.
        images_attack (list): List of pygame.Surface objects for attack animation.
        death_images (list): List of pygame.Surface objects for death animation.
        images_hit (list): List of pygame.Surface objects for hit animation.
        current_hp (int): Current hit points of the boss.
        max_hp (int): Maximum hit points of the boss.
        is_create_gates (bool): Flag indicating if gates should be created upon death.
        is_stop (bool): Flag indicating if the boss is currently stopped.
        stop_timer (int): Duration for which the boss remains stopped.
        current_stop_timer (int): Current timer count for stop duration.
        const_delay_animation (int): Constant delay between animation frames.
        const_delay_death_animation (int): Constant delay between death animation frames.
        idle_animation_count (int): Current frame index for idle animation.
        is_hit (bool): Flag indicating if the boss is currently hit.
        hit_animation_count (int): Current frame index for hit animation.
        attack_animation_count (int): Current frame index for attack animation.
        attacking (None or object): Object representing the current attack state.
        fireballs (pygame.sprite.Group): Group of Shockwave objects representing fireball attacks.

    Methods:
        __init__(self, x, y, image_paths_idle=None, image_paths_run=None, image_paths_attack=None,
                 image_paths_death=None, image_paths_hit=None):
            Initializes the Boss with initial coordinates (x, y)
            and optional image paths for animations.

        take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
            Reduces the boss's current hit points by a specified amount and sets hit animation.

        fireball_attack(self):
            Initiates a fireball attack if the boss is not stopped.

        move_sprites(self, direction):
            Moves all fireballs in the specified direction.

        update_animation(self):
            Updates the boss's animation frames based on the delay.

        attack(self, screen):
            Draws the boss's attack animation on the screen.

        idle(self, screen):
            Draws the boss's idle animation on the screen.

        draw(self, screen):
            Draws the boss on the screen based on its current state.

        draw_boss_hp_bar(self, screen):
            Draws the boss's health bar on the screen.

        draw_hit(self, screen):
            Draws the boss's hit animation on the screen and updates the animation frame.

        update(self, screen, group, game=None):
            Updates the boss's state, movement, and animations.

    """

    def __init__(self, x, y, image_paths_idle=None, image_paths_run=None, image_paths_attack=None,
                 image_paths_death=None, image_paths_hit=None):
        """
        Initializes the Boss with initial coordinates (x, y) and
        optional image paths for animations.

        Args:
            x (int): Initial x-coordinate of the Boss.
            y (int): Initial y-coordinate of the Boss.
            image_paths_idle (list, optional): List of paths to idle animation frames.
            image_paths_run (list, optional): List of paths to running animation frames.
            image_paths_attack (list, optional): List of paths to attack animation frames.
            image_paths_death (list, optional): List of paths to death animation frames.
            image_paths_hit (list, optional): List of paths to hit animation frames.
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
        Reduces the boss's current hit points by a specified amount and sets hit animation.

        Args:
            damage (int, optional): Amount of damage to inflict
            (default is constants.PLAYER_ATTACK_DAMAGE).
        """
        super().take_damage(damage)
        self.is_hit = True
        if self.current_hp < 0:
            self.current_hp = 0

    def fireball_attack(self):
        """
        Initiates a fireball attack if the boss is not stopped.
        """
        if not self.is_stop:
            return

        if self.current_stop_timer % (self.stop_timer - 10) == 0:
            fireball = Shockwave(self.rect.centerx, self.rect.centery, 5, 0, self.attack_direction, 'fireball')
            self.fireballs.add(fireball)

    def move_sprites(self, direction):
        """
        Moves all fireballs in the specified direction.

        Args:
            direction (int): Direction of movement (-1 for left, 1 for right).
        """
        for fireball in self.fireballs:
            fireball.move_sprite(direction)

    def update_animation(self):
        """
        Updates the boss's animation frames based on the delay.
        """
        super().update_animation()

        if self.delay_animation == 0:
            if self.is_hit:
                self.hit_animation_count += 1

            self.attack_animation_count += 1

        if self.hit_animation_count >= len(self.images_hit):
            self.hit_animation_count = 0
            self.is_hit = False

        if self.attack_animation_count >= len(self.images_attack):
            self.attack_animation_count = 0

    def attack(self, screen):
        """
        Draws the boss's attack animation on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_attack[self.attack_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_attack[self.attack_animation_count], (self.rect.x, self.rect.y))

    def idle(self, screen):
        """
        Draws the boss's idle animation on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_idle[self.idle_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_idle[self.idle_animation_count], (self.rect.x, self.rect.y))

    def draw(self, screen):
        """
        Draws the boss on the screen based on its current state.

        Args:
            screen (pygame.Surface): The surface to draw on.
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
        Draws the boss's health bar on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
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
        Draws the boss's hit animation on the screen and updates the animation frame.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images_hit[self.hit_animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images_hit[self.hit_animation_count], (self.rect.x, self.rect.y))

        self.update_animation()

    def update(self, screen, group, game=None):
        """
        Updates the boss's state, movement, and animations.

        Args:
            screen (pygame.Surface): The surface to draw on.
            group (pygame.sprite.Group): The group containing all enemies.
            game (object, optional): The game object containing additional state (default is None).
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
