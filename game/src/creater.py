import pygame
from game.src.screen import screen_obj
from game.src.enemies.sculwolf import Sculwolf
from game.src.enemies.satyr import Satyr
from game.src.enemies.snail import Snail
from game.src.locations import Locations, PartialBackground
from game.src.platforms import Platform, MovingPlatform
from game.src.npc import Blacksmith



def create_enemies():
    start = screen_obj.width
    sculwolfs_group = pygame.sprite.Group()
    sculwolfs_group.add(Sculwolf(start + screen_obj.width // 2 - 150 * screen_obj.width_scale, screen_obj.height // 2 - 55 * screen_obj.height_scale, 200 * screen_obj.width_scale),
                        Sculwolf(start + 0, screen_obj.height - 225 * screen_obj.height_scale, 120 * screen_obj.width_scale),
                        Sculwolf(start + screen_obj.width - 200 * screen_obj.width_scale, screen_obj.height - 425  * screen_obj.height_scale, 120 * screen_obj.width_scale),
                        Sculwolf(start + screen_obj.width * 3 // 2 + 50 * screen_obj.width_scale, screen_obj.height // 2 + 125  * screen_obj.height_scale, 260 * screen_obj.width_scale),

                        )

    satyr_group = pygame.sprite.Group()
    satyr_group.add(Satyr(start + 700 * screen_obj.width_scale, screen_obj.height - 40 * screen_obj.height_scale, 160 * screen_obj.width_scale),
                    Satyr(start + 0, screen_obj.height - 400 * screen_obj.height_scale, 170 * screen_obj.width_scale),
                    Satyr(start + screen_obj.width // 2 - 150 * screen_obj.width_scale, screen_obj.height // 2 - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale),
                    Satyr(start + screen_obj.width * 2 + 100 * screen_obj.width_scale, screen_obj.height - 40 * screen_obj.height_scale, 180 * screen_obj.width_scale),
                    )

    snail_group = pygame.sprite.Group()
    snail_group.add(Snail(start + 200 * screen_obj.width_scale, screen_obj.height - 40 * screen_obj.height_scale, 160 * screen_obj.width_scale),
                    Snail(start + screen_obj.width + 200 * screen_obj.width_scale, screen_obj.height - 200 * screen_obj.height_scale, 160 * screen_obj.width_scale),
                    Snail(start + screen_obj.width * 2, screen_obj.height - 200 * screen_obj.height_scale, 170 * screen_obj.width_scale),
                    #Snail(start + 200 * screen_obj.width_scale, screen_obj.height - 40,  * screen_obj.width_scale),
                    )

    return [sculwolfs_group, satyr_group, snail_group]



def create_location():
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
    start = screen_obj.width
    platforms = pygame.sprite.Group()

    for x in range(0, start + 5 * screen_obj.width, int(300 * screen_obj.width_scale)):
        platforms.add(Platform(x, screen_obj.height - 40 * screen_obj.height_scale, int(300 * screen_obj.width_scale), 40 * screen_obj.height_scale))

        # левый столб
    platforms.add(Platform(-start // 1.23, 0, screen_obj.width // 1.2, screen_obj.height, "mountain"),

                  Platform(start + 0, screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + 0, screen_obj.height - 400 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # центр
                  Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale, screen_obj.height // 2 - 30 * screen_obj.height_scale, 300 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale, screen_obj.height // 2 + 150 * screen_obj.height_scale, 300 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width // 2 - 150 * screen_obj.width_scale, screen_obj.height // 2 - 200 * screen_obj.height_scale, 300 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # правый столб
                  Platform(start + screen_obj.width - 200 * screen_obj.width_scale, screen_obj.height - 400 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start +screen_obj.width - 200 * screen_obj.width_scale, screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # между первой и второй
                  Platform(start + screen_obj.width, screen_obj.height - 570 * screen_obj.height_scale, 30 * screen_obj.width_scale, 400 * screen_obj.height_scale, 'right_wall'),
                  Platform(start + screen_obj.width + 170 * screen_obj.width_scale, screen_obj.height - 570 * screen_obj.height_scale, 30 * screen_obj.width_scale, 400 * screen_obj.height_scale, 'left_wall'),
                  Platform(start + screen_obj.width, 0, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # второй паттерн

                  # левый столб
                  Platform(start + screen_obj.width + 200 * screen_obj.width_scale, screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width + 200 * screen_obj.width_scale, screen_obj.height - 400 * screen_obj.height_scale, 100 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width + 350 * screen_obj.width_scale, screen_obj.height - 300 * screen_obj.height_scale, 100 * screen_obj.width_scale, 20 * screen_obj.height_scale),

                  # правый столб
                  Platform(start + screen_obj.width * 2, screen_obj.height - 200 * screen_obj.height_scale, 200 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width * 2 + 100 * screen_obj.width_scale, screen_obj.height - 400 * screen_obj.height_scale, 100 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width * 2 - 50 * screen_obj.width_scale, screen_obj.height - 300 * screen_obj.height_scale, 100 * screen_obj.width_scale, 20 * screen_obj.height_scale),

                  # центр
                  Platform(start + screen_obj.width * 3 // 2 + 50 * screen_obj.width_scale, screen_obj.height // 2 + 150 * screen_obj.height_scale, 300 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # мини здание паттерн
                  Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale, screen_obj.height - 150 * screen_obj.height_scale, 30 * screen_obj.width_scale, 120 * screen_obj.height_scale, 'right_wall'),
                  Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale, 250 * screen_obj.height_scale, 'right_wall'),
                  Platform(start + screen_obj.width * 4, 0, 30 * screen_obj.width_scale, 300 * screen_obj.height_scale, 'right_wall'),
                  Platform(start + screen_obj.width * 4, 300 * screen_obj.height_scale, 230 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width * 4 + 200 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale, 300 * screen_obj.height_scale, 'left_wall'),
                  Platform(start + screen_obj.width * 3 + 100 * screen_obj.width_scale, screen_obj.height - 350 * screen_obj.height_scale, 180 * screen_obj.width_scale, 30 * screen_obj.height_scale),
                  Platform(start + screen_obj.width * 4 - 180 * screen_obj.width_scale, screen_obj.height - 330 * screen_obj.height_scale, 180 * screen_obj.width_scale, 30 * screen_obj.height_scale),

                  # босс арена
                  Platform(start + screen_obj.width * 5 + 200 * screen_obj.width_scale, 0, 30 * screen_obj.width_scale, 400 * screen_obj.height_scale, 'right_wall'),

                  )

    for x in range(start + screen_obj.width * 3 + int(100 * screen_obj.width_scale), start + 4 * screen_obj.width, int(300 * screen_obj.width_scale)):
        platforms.add(Platform(x, screen_obj.height - 180 * screen_obj.height_scale, int(300 * screen_obj.width_scale), 30 * screen_obj.height_scale))


    return platforms

def add_moving_platforms(platforms):
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

                  # MovingPlatform(start + screen_obj.width * 3.5, screen_obj.height - 200,200, 30, screen_obj.height * 0.8, screen_obj.height * 0.3, 'y'),
                 )

    return platforms


def create_npc():
    npcs = pygame.sprite.Group()

    npcs.add(
        Blacksmith(screen_obj.width // 2 - 200 * screen_obj.width_scale, screen_obj.height - 95 * screen_obj.height_scale),

    )

    return npcs


