"""
Module: game.src.constants

This module defines constants used throughout the game for
various purposes such as player attributes,
enemy attributes, game physics, attack parameters, and cooldown times.

Constants:
- VELOCITY (int): Default velocity for movement.
- BACKGROUND_SPEED (int): Speed of the background scrolling.
- PARTIAL_BACKGROUND_SPEED (int): Speed of partial background scrolling.

- MAX_FPS (int): Maximum frames per second for the game loop.
- DELAY (int): Delay time in milliseconds between game loops.
- GRAVITY (float): Gravity constant affecting player and enemy falls.

- PLAYER_ATTACK_DIRECTION (int): Default direction of player's attack.
- PLAYER_HP_COUNT (int): Initial hit points (HP) of the player.
- PLAYER_HEART_IMAGE_SCALE (int): Scale factor for player's heart image.
- PLAYER_JUMP_HEIGHT (int): Height of the player's jump.
- PLAYER_MAX_FALL_SPEED (int): Maximum speed of the player's fall.
- PLAYER_ATTACK_COOLDOWN (int): Cooldown time between player's attacks.
- PLAYER_ATTACK_RANGE (int): Range of player's attack.
- PLAYER_ATTACK_DAMAGE (int): Damage inflicted by player's attack.
- PLAYER_MAIN_KNOCKBACK (int): Knockback distance caused by player's attack.
- PLAYER_INVISIBILITY_DURATION (int): Duration of player's invisibility after being hit.
- PLAYER_ABILITY_COOLDOWN (int): Cooldown time for player's special ability.
- PLAYER_ULTA_COOLDOWN (int): Cooldown time for player's ultimate ability.
- PLAYER_ULTA_RANGE (int): Range of player's ultimate ability.
- PLAYER_ULTA_DAMAGE (int): Damage inflicted by player's ultimate ability.

- ENEMY_NORMAL_SPEED (int): Default speed of normal enemies.
- ENEMY_JUMP_HEIGHT (int): Height of jump for enemies.
- ENEMY_HP (int): Hit points (HP) of enemies.

- BOSS_HP (int): Hit points (HP) of the boss enemy.

Usage:
Import this module to access constants that are used across different parts of the game,
such as controlling gameplay mechanics, character attributes, and game physics parameters.
"""

VELOCITY = -5
BACKGROUND_SPEED = 1
PARTIAL_BACKGROUND_SPEED = 5

MAX_FPS = 60
DELAY = 30
GRAVITY = 0.3

PLAYER_ATTACK_DIRECTION = 1
PLAYER_HP_COUNT = 5
PLAYER_HEART_IMAGE_SCALE = 2
PLAYER_JUMP_HEIGHT = 9
PLAYER_MAX_FALL_SPEED = 30
PLAYER_ATTACK_COOLDOWN = 500
PLAYER_ATTACK_RANGE = 50
PLAYER_ATTACK_DAMAGE = 20
PLAYER_MAIN_KNOCKBACK = 30
PLAYER_INVISIBILITY_DURATION = 2
PLAYER_ABILITY_COOLDOWN = 1000
PLAYER_ULTA_COOLDOWN = 1500
PLAYER_ULTA_RANGE = 150
PLAYER_ULTA_DAMAGE = 60

ENEMY_NORMAL_SPEED = 3
ENEMY_JUMP_HEIGHT = 10
ENEMY_HP = 100

BOSS_HP = 600
