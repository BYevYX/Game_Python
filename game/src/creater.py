"""
Module: game.src.creater

This module contains functions for creating various game elements such as enemies, locations,
platforms, moving platforms, gates, and NPCs using Pygame.

Functions:
- create_enemies():
    Create groups of enemies for the game.

- add_boss(enemies):
    Add a boss to the list of enemies.

- create_location():
    Create the game location with backgrounds and partial backgrounds.

- create_platforms():
    Create and return all static platforms for the game.

- add_moving_platforms(platforms):
    Add moving platforms to the existing group of platforms.

- create_and_add_gates(platforms):
    Create and add gates to the existing group of platforms.

- create_npc():
    Create and return NPCs for the game.

Dependencies:
- External dependencies:
  - pygame: Library for game development in Python with multimedia capabilities.

- Internal dependencies:
  - game.src.enemies.boss: Imports Boss class for creating boss enemies.
  - game.src.enemies.satyr: Imports Satyr class for creating Satyr enemies.
  - game.src.enemies.sculwolf: Imports Sculwolf class for creating Sculwolf enemies.
  - game.src.enemies.snail: Imports Snail class for creating Snail enemies.
  - game.src.locations: Imports Locations and PartialBackground classes for managing game locations.
  - game.src.npc: Imports Blacksmith class for creating NPCs.
  - game.src.platforms: Imports Platform and MovingPlatform classes for managing platforms.
  - game.src.screen: Imports screen_obj for managing screen properties.

Usage:
Import this module to access functions for creating enemies, locations,
platforms, moving platforms, gates,
and NPCs required for initializing and setting up the game environment.
"""

from game.src.enemies.boss import Boss
from game.src.enemies.satyr import Satyr
from game.src.enemies.sculwolf import Sculwolf
from game.src.enemies.snail import Snail
from game.src.locations import Locations, PartialBackground
from game.src.npc import Blacksmith
from game.src.platforms import Platform, MovingPlatform
from game.src.screen import screen_obj
import pygame


def create_enemies():
    """
    Create groups of enemies for the game.

    :rtype: list
    :return: A list containing groups of Sculwolfs, Satyrs, and Snails.
    """
    start = screen_obj.width

    sculwolfs_group = pygame.sprite.Group()
    sculwolfs_tuple = (
        Sculwolf(start + screen_obj.width // 2 - 150 * screen_obj.width_scale,
                 screen_obj.height // 2 - 55 * screen_obj.height_scale, 200 * screen_obj.width_scale),
        Sculwolf(start + 0, screen_obj.height - 225 * screen_obj.height_scale,
                 120 * screen_obj.width_scale),
        Sculwolf(start + screen_obj.width - 200 * screen_obj.width_scale,
                 screen_obj.height - 425 * screen_obj.height_scale, 120 * screen_obj.width_scale),
        Sculwolf(start + screen_obj.width * 3 // 2 + 50 * screen_obj.width_scale,
                 screen_obj.height // 2 + 125 * screen_obj.height_scale, 260 * screen_obj.width_scale),
    )
    sculwolfs_group.add(*sculwolfs_tuple)

    satyr_group = pygame.sprite.Group()
    satyr_tuple = (
        Satyr(start + 700 * screen_obj.width_scale, screen_obj.height - 40 * screen_obj.height_scale,
              160 * screen_obj.width_scale),
        Satyr(start + 0, screen_obj.height - 400 * screen_obj.height_scale, 170 * screen_obj.width_scale),
        Satyr(start + screen_obj.width // 2 - 150 * screen_obj.width_scale,
              screen_obj.height // 2 - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale),
        Satyr(start + screen_obj.width * 2 + 100 * screen_obj.width_scale,
              screen_obj.height - 40 * screen_obj.height_scale, 180 * screen_obj.width_scale),
    )
    satyr_group.add(*satyr_tuple)

    snail_group = pygame.sprite.Group()
    snail_tuple = (
        Snail(start + 200 * screen_obj.width_scale, screen_obj.height - 40 * screen_obj.height_scale,
              160 * screen_obj.width_scale),
        Snail(start + screen_obj.width + 200 * screen_obj.width_scale,
              screen_obj.height - 200 * screen_obj.height_scale, 160 * screen_obj.width_scale),
        Snail(start + screen_obj.width * 2, screen_obj.height - 200 * screen_obj.height_scale,
              170 * screen_obj.width_scale),
        # Snail(start + 200 * screen_obj.width_scale, screen_obj.height - 40,  * screen_obj.width_scale),
    )
    snail_group.add(*snail_tuple)

    return [sculwolfs_group, satyr_group, snail_group]


def add_boss(enemies):
    """
    Add a boss to the list of enemies.

    :rtype: _SpriteSupportsGroup
    :param enemies: List of enemy groups.
    :return: Group containing the boss.
    """
    bosses = pygame.sprite.Group()
    boss_tuple = (
        Boss(screen_obj.width + 400 * screen_obj.width_scale, screen_obj.height - 150 * screen_obj.height_scale),
    )
    bosses.add(*boss_tuple)

    enemies.append(bosses)

    return bosses


def create_location():
    """
    Create the game location with backgrounds and partial backgrounds.

    :rtype: list
    :return: A list containing the main location and partial backgrounds.
    """
    start = screen_obj.width
    main_location = Locations(["image/locations/backgrounds/01 background.png",
                               "image/locations/backgrounds/02 background.png",
                               "image/locations/backgrounds/03 background A.png",
                               "image/locations/backgrounds/03 background B.png",
                               "image/locations/backgrounds/04 background.png",
                               "image/locations/backgrounds/05 background.png"],
                              'sound/bg-sound.mp3', (screen_obj.width, screen_obj.height))

    partial_backgrounds = [

        PartialBackground(screen_obj.width // 2 + 100 * screen_obj.width_scale,
                          screen_obj.height - 330 * screen_obj.height_scale, 250 * screen_obj.width_scale,
                          300 * screen_obj.height_scale, "big_tree"),

        PartialBackground(start + screen_obj.width, 0, 200 * screen_obj.width_scale, 600 * screen_obj.height_scale,
                          "collumn_back"),

        PartialBackground(start + screen_obj.width * 4, 0, 200 * screen_obj.width_scale, 300 * screen_obj.height_scale,
                          "collumn_back"),

        PartialBackground(start + screen_obj.width * 3 + 100 * screen_obj.width_scale, 0,
                          screen_obj.width - 100 * screen_obj.width_scale, screen_obj.height, 'brown_brick_wall'),

        # хата
        PartialBackground(0, screen_obj.height - 130 * screen_obj.height_scale, 450 * screen_obj.width_scale,
                          110 * screen_obj.height_scale, "house_enter"),

        PartialBackground(0, screen_obj.height - 280 * screen_obj.height_scale, 225 * screen_obj.width_scale,
                          150 * screen_obj.height_scale, "house_wall"),

        PartialBackground(225 * screen_obj.width_scale, screen_obj.height - 280 * screen_obj.height_scale,
                          225 * screen_obj.width_scale, 150 * screen_obj.height_scale, "house_wall"),

        PartialBackground(0, screen_obj.height - 380 * screen_obj.height_scale, 225 * screen_obj.width_scale,
                          100 * screen_obj.height_scale, "house_roof"),

        PartialBackground(225 * screen_obj.width_scale, screen_obj.height - 380 * screen_obj.height_scale,
                          225 * screen_obj.width_scale, 100 * screen_obj.height_scale, "house_roof"),

        PartialBackground((225 - 40) * screen_obj.width_scale, screen_obj.height - 408 * screen_obj.height_scale,
                          20 * screen_obj.width_scale, 30 * screen_obj.height_scale, "house_tube"),

        PartialBackground((225 + 40) * screen_obj.width_scale, screen_obj.height - 408 * screen_obj.height_scale,
                          20 * screen_obj.width_scale, 30 * screen_obj.height_scale, "house_tube"),

        # замок
        PartialBackground(start + screen_obj.width * 5 + 220 * screen_obj.width_scale, 0, screen_obj.width,
                          screen_obj.height)

    ]

    return [main_location, partial_backgrounds]


def create_platforms():
    """
    Create and return all static platforms for the game.

    :rtype: _SpriteSupportsGroup
    :return: Group containing all static platforms.
    """
    start = screen_obj.width
    platforms = pygame.sprite.Group()

    for x in range(0, start + 5 * screen_obj.width, int(300 * screen_obj.width_scale)):
        platform = Platform(x, screen_obj.height - 40 * screen_obj.height_scale, int(300 * screen_obj.width_scale),
                            40 * screen_obj.height_scale)
        platforms.add(platform)

    platforms_tuple = (
        # левый столб
        Platform(-start // 1.23, 0, screen_obj.width // 1.2, screen_obj.height, "mountain"),

        Platform(start + 0, screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + 0, screen_obj.height - 400 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),

        # центр
        Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale,
                 screen_obj.height // 2 - 30 * screen_obj.height_scale, 300 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale,
                 screen_obj.height // 2 + 150 * screen_obj.height_scale, 300 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale,
                 screen_obj.height // 2 - 200 * screen_obj.height_scale, 300 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),

        # правый столб
        Platform(start + screen_obj.width - 200 * screen_obj.width_scale,
                 screen_obj.height - 400 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width - 200 * screen_obj.width_scale,
                 screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),

        # между первой и второй
        Platform(start + screen_obj.width, screen_obj.height - 570 * screen_obj.height_scale,
                 30 * screen_obj.width_scale, 400 * screen_obj.height_scale, 'right_wall'),
        Platform(start + screen_obj.width + 170 * screen_obj.width_scale,
                 screen_obj.height - 570 * screen_obj.height_scale, 30 * screen_obj.width_scale,
                 400 * screen_obj.height_scale, 'left_wall'),
        Platform(start + screen_obj.width, 0, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),

        # второй паттерн

        # левый столб
        Platform(start + screen_obj.width + 200 * screen_obj.width_scale,
                 screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width + 200 * screen_obj.width_scale,
                 screen_obj.height - 400 * screen_obj.height_scale, 100 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width + 350 * screen_obj.width_scale,
                 screen_obj.height - 300 * screen_obj.height_scale, 100 * screen_obj.width_scale,
                 20 * screen_obj.height_scale),

        # правый столб
        Platform(start + screen_obj.width * 2, screen_obj.height - 200 * screen_obj.height_scale,
                 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width * 2 + 100 * screen_obj.width_scale,
                 screen_obj.height - 400 * screen_obj.height_scale, 100 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width * 2 - 50 * screen_obj.width_scale,
                 screen_obj.height - 300 * screen_obj.height_scale, 100 * screen_obj.width_scale,
                 20 * screen_obj.height_scale),

        # центр
        Platform(start + screen_obj.width * 3 // 2 + 50 * screen_obj.width_scale,
                 screen_obj.height // 2 + 150 * screen_obj.height_scale, 300 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),

        # мини здание паттерн
        Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale,
                 screen_obj.height - 150 * screen_obj.height_scale, 30 * screen_obj.width_scale,
                 120 * screen_obj.height_scale, 'right_wall'),
        Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale,
                 250 * screen_obj.height_scale, 'right_wall'),
        Platform(start + screen_obj.width * 4, 0, 30 * screen_obj.width_scale, 300 * screen_obj.height_scale,
                 'right_wall'),
        Platform(start + screen_obj.width * 4, 300 * screen_obj.height_scale, 230 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width * 4 + 200 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale,
                 300 * screen_obj.height_scale, 'left_wall'),
        Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale,
                 screen_obj.height - 350 * screen_obj.height_scale, 180 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),
        Platform(start + screen_obj.width * 4 - 180 * screen_obj.width_scale,
                 screen_obj.height - 330 * screen_obj.height_scale, 180 * screen_obj.width_scale,
                 30 * screen_obj.height_scale),

        # босс арена
        Platform(start + screen_obj.width * 5 + 200 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale,
                 400 * screen_obj.height_scale, 'right_wall'),
    )
    platforms.add(*platforms_tuple)

    for x in range(start + screen_obj.width * 3 + int(100 * screen_obj.width_scale), start + 4 * screen_obj.width,
                   int(300 * screen_obj.width_scale)):
        platform = Platform(x, screen_obj.height - 180 * screen_obj.height_scale, int(300 * screen_obj.width_scale),
                            30 * screen_obj.height_scale)
        platforms.add(platform)

    return platforms


def add_moving_platforms(platforms):
    """
    Add moving platforms to the existing group of platforms.

    :rtype: _SpriteSupportsGroup
    :param platforms: Group of existing platforms.
    :return: Group containing both static and moving platforms.
    """
    start = screen_obj.width

    # движущиеся платформы в мини здании
    platforms.add(MovingPlatform(start + screen_obj.width * 3 + 300 * screen_obj.width_scale,
                                 screen_obj.height - 400 * screen_obj.height_scale, 200 * screen_obj.width_scale,
                                 30 * screen_obj.height_scale,
                                 start + screen_obj.width * 3 + 300 * screen_obj.width_scale,
                                 start + screen_obj.width * 4 - 200 * screen_obj.width_scale),

                  MovingPlatform(start + screen_obj.width * 3.5, screen_obj.height - 550 * screen_obj.height_scale,
                                 200 * screen_obj.width_scale, 30 * screen_obj.height_scale,
                                 start + screen_obj.width * 4,
                                 start + screen_obj.width * 3 + 140 * screen_obj.width_scale),

                  # MovingPlatform(start + screen_obj.width * 3.5, screen_obj.height - 200,200, 30,
                  # screen_obj.height * 0.8, screen_obj.height * 0.3, 'y'),
                  )

    return platforms


def create_and_add_gates(platforms):
    """
    Create and add gates to the existing group of platforms.

    :rtype: _SpriteSupportsGroup
    :param platforms: Group of existing platforms.
    :return: Group containing the gates.
    """
    gates = pygame.sprite.Group()
    gates_tuple = (
        Platform(screen_obj.width // 2 - 100 * screen_obj.width_scale, 300, 40, 120, "gate"),
        Platform(screen_obj.width // 2 - 100 * screen_obj.width_scale, 400, 40, 160, "gate"),
        Platform(screen_obj.width * 1.6, 400, 30, 160, "gate"),
    )
    gates.add(*gates_tuple)

    platforms.add(gates)
    return gates


def create_npc():
    """
    Create and return NPCs for the game.

    :rtype: _SpriteSupportsGroup
    :return: Group containing the NPCs.
    """
    npcs = pygame.sprite.Group()
    npcs_tuple = (
        Blacksmith(screen_obj.width // 2 - 200 * screen_obj.width_scale,
                   screen_obj.height - 95 * screen_obj.height_scale),
    )
    npcs.add(*npcs_tuple)

    return npcs
