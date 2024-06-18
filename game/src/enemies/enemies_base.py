"""
This module defines classes representing enemies in a Pygame-based game.

Classes:
- Enemy(pygame.sprite.Sprite): Represents a basic enemy in the game.
- CommonEnemy(Enemy): Represents a common type of enemy with movement range.

Attributes (Enemy class):
- images (list): List of pygame.Surface objects for animation frames.
- death_images (list): List of pygame.Surface objects for death animation frames.
- rect (pygame.Rect): Rectangle defining position and size on screen.
- speed (int): Movement speed of the enemy.
- animation_count (int): Current frame index for regular animation.
- death_animation_count (int): Current frame index for death animation.
- is_dead (bool): Flag indicating if the enemy is dead.
- velocity (int): Velocity of movement.
- velocity_direction (str): Direction of movement ('right' or 'left').
- current_hp (int): Current hit points.
- const_delay_death_animation (int): Constant delay between death animation frames.
- delay_death_animation (int): Current delay count for death animation frames.
- const_delay_animation (int): Constant delay between regular animation frames.
- delay_animation (int): Current delay count for regular animation frames.
- damage (int): Damage dealt by the enemy.
- attack_direction (int): Direction the enemy is facing or moving (-1 for left, 1 for right).
- damage_texts (list): List of tuples (damage, duration) for displaying damage.
- font (pygame.font.Font): Font object for rendering damage numbers.

Methods (Enemy class):
- __init__(self, x, y): Initialize with coordinates (x, y).
- update_animation(self): Update animation frame.
- draw(self, screen): Draw enemy on the screen.
- take_damage(self, damage): Reduce hit points by specified damage.
- death(self, group, screen): Handle death animation and removal from group.
- change_direction(self, direction): Change movement direction.
- update(self, screen, group, game=None): Update state and draw on screen.
- move_group(direction, groups): Change movement direction of all enemies in groups.

Methods (CommonEnemy class, inherits Enemy):
- __init__(self, x, y, range_place): Initialize with specific attributes.
- move(self): Move horizontally within defined range.
- update(self, screen, group, game=None): Update state and draw on screen.
"""

from game.src import constants
from game.src.screen import screen_obj
import pygame


class Enemy(pygame.sprite.Sprite):
    """
        Represents an enemy in the game.

        Attributes:
            images (list):
                A list of pygame.Surface objects representing animation frames for the enemy.
            death_images (list):
                A list of pygame.Surface objects representing death animation frames for the enemy.
            rect (pygame.Rect):
                The rectangle representing the position and size of the enemy on the screen.
            speed (int): The speed of movement of the enemy.
            animation_count (int): Current frame index for animation.
            death_animation_count (int): Current frame index for death animation.
            is_dead (bool): Flag indicating if the enemy is dead.
            velocity (int): The velocity of movement of the enemy.
            velocity_direction (str): The direction of movement ('right' or 'left').
            current_hp (int): Current hit points of the enemy.
            const_delay_death_animation (int): Constant delay between death animation frames.
            delay_death_animation (int): Current delay count for death animation frames.
            const_delay_animation (int): Constant delay between regular animation frames.
            delay_animation (int):
                Current delay count for regular animation frames.
            damage (int):
                Amount of damage the enemy deals.
            attack_direction (int):
                Direction the enemy is facing or moving towards (-1 for left, 1 for right).
            damage_texts (list):
                List of tuples containing damage values and their display durations.
            font (pygame.font.Font): Font object for rendering damage numbers.

        Methods:
            __init__(self, x, y):
                Initializes the Enemy with initial coordinates (x, y).

            update_animation(self):
                Updates the animation frame of the Enemy.

            draw(self, screen):
                Draws the Enemy on the screen.

            take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
                Reduces the current hit points of the Enemy by a specified amount.

            death(self, group, screen):
                Handles the death animation and removal of the Enemy from the group upon death.

            change_direction(self, direction):
                Changes the movement direction of the Enemy.

            update(self, screen, group, game=None):
                Updates the state of the Enemy and draws it on the screen.

            move_group(direction, groups):
                Changes the movement direction of all enemies in the specified groups.

        """

    images = None
    death_images = []

    def __init__(self, x, y):
        """
        Initialize the Enemy with specific attributes.

        Args:
            x (int): Initial x-coordinate of the Enemy.
            y (int): Initial y-coordinate of the Enemy.
        """
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
        """
        Update the animation frame of the Enemy.
        """
        if self.delay_animation == self.const_delay_animation:
            self.delay_animation = 0
            self.animation_count += 1
        else:
            self.delay_animation += 1

        if self.animation_count >= len(self.images):
            self.animation_count = 0

    def draw(self, screen):
        """
        Draw the Enemy on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the Enemy on.
        """
        if self.attack_direction == -1:
            screen.blit(pygame.transform.flip(self.images[self.animation_count], True, False),
                        (self.rect.x, self.rect.y))
        elif self.attack_direction == 1:
            screen.blit(self.images[self.animation_count], (self.rect.x, self.rect.y))

        for dmg, time in self.damage_texts:
            damage_surface = self.font.render(str(dmg), True, (139, 0, 0))
            screen.blit(damage_surface, (self.rect.x, self.rect.y - 30 - 10))

        self.update_animation()

    def take_damage(self, damage=constants.PLAYER_ATTACK_DAMAGE):
        """
        Reduce the current hit points of the Enemy by a specified amount.

        Args:
            damage (int): Amount of damage to be subtracted from current hit points.
        """
        self.current_hp -= damage
        self.damage_texts.append((damage, 30))

    def death(self, group, screen):
        """
        Handle the death animation and removal of the Enemy from the group.

        Args:
            group (pygame.sprite.Group): The group from which the Enemy will be removed upon death.
            screen (pygame.Surface): The surface to draw the death animation on.
        """
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
        """
        Change the movement direction of the Enemy.

        Args:
            direction (str):
                Direction to which the Enemy will change its movement ('left' or 'right').
        """
        if direction != self.velocity_direction:
            self.velocity *= -1
            self.velocity_direction = direction

    def update(self, screen, group, game=None):
        """
        Update the Enemy's state and draw it on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the Enemy on.
            group (pygame.sprite.Group): The group containing all enemies.
            game (Game): The instance of the Game class.
        """
        self.damage_texts = [(dmg, time - 1) for dmg, time in self.damage_texts if time > 0]

        if not self.is_dead:
            self.draw(screen)

        self.death(group, screen)

    @staticmethod
    def move_group(direction, groups):
        """

        :rtype: None
        :param direction:
        :param groups:
        """
        for group in groups:
            for enemy in group:
                enemy.change_direction(direction)
                enemy.rect.x += enemy.velocity

                if isinstance(enemy, CommonEnemy):
                    enemy.left += enemy.velocity
                    enemy.right += enemy.velocity


class CommonEnemy(Enemy):
    """
    Class representing a common type of Enemy in the game.

    Attributes:
        left (int): Left boundary of movement range for the CommonEnemy.
        right (int): Right boundary of movement range for the CommonEnemy.

    Methods:
        __init__(self, x, y, range_place=200 * screen_obj.width_scale):
            Initializes a CommonEnemy with specific attributes and animations.

        move(self):
            Moves the CommonEnemy horizontally within its defined range.

        update(self, screen, group, game=None):
            Updates the state of the CommonEnemy and draws it on the screen.
    """

    def __init__(self, x, y, range_place=200 * screen_obj.width_scale):
        """
        Initializes a CommonEnemy with specific attributes and animations.

        Args:
            x (int): The x-coordinate of the CommonEnemy's initial position.
            y (int): The y-coordinate of the CommonEnemy's initial position.
            range_place (int): The range in which the CommonEnemy can move horizontally.
        """
        super().__init__(x, y)

        self.left = x
        self.right = x + range_place

    def move(self):
        """
        Move the CommonEnemy horizontally within its defined range.

        If the CommonEnemy reaches the boundaries of its range, it changes direction.
        """
        if self.rect.x >= self.right:
            self.speed = -self.speed
            self.attack_direction = -1
        elif self.rect.x <= self.left:
            self.speed = abs(self.speed)
            self.attack_direction = 1

        self.rect.x += self.speed

    def update(self, screen, group, game=None):
        """
        Update the state of the CommonEnemy and draw it on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the CommonEnemy on.
            group (pygame.sprite.Group): The group containing all enemies.
            game (Game): The instance of the Game class.
        """
        super().update(screen, group)

        self.move()
