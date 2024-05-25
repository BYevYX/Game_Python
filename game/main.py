import pygame
import sys
from game.src.menus import Menu, MainMenu
from game.src.screen import screen_obj
from game.src.button import Button
from game.src.player import Player
from game.src.labels import Label
from game.src import npc
from game.src.platforms import MovingPlatform
import game.src.constants as constants
import game.src.creater as creater

pygame.init()


pygame.display.set_caption("CS-3")
pygame.display.set_icon(pygame.image.load("image/icon_game.webp"))


# проработать шрифт
myfont = pygame.font.Font("fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf", 30)
text_surface = myfont.render('Long time ago...', True, 'orange')



# создание npc
blacksmith = npc.Blacksmith(270, 270)

# создание меню
main_menu = MainMenu()



def game_on(screen):
    print(screen_obj.height, screen_obj.width, screen_obj.height_scale, screen_obj.width_scale)
    clock = pygame.time.Clock()

    main_location, partial_backgrounds = creater.create_location()
    platforms = creater.create_platforms()
    enemies = creater.create_enemies()

    creater.create_moving_platforms(platforms)

    # создание персонажа
    player = Player(screen_obj.width // 2, screen_obj.height - (40 + 60) * screen_obj.height_scale)

    main_location.sound.play(-1)

    ghost = pygame.image.load('image/ghost.png').convert_alpha()
    ghost_list = []

    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 5000)

    gameplay = True
    pause = False

    lose_label = Label(screen_obj.width, screen_obj.height, None, 72, 'You Lose!', (193, 196, 199), "image/UI/Panel/Window/Medium.png")
    pause_label = Label(screen_obj.width, screen_obj.height, None, 72, 'Pause', (193, 196, 199), "image/UI/Panel/Window/Medium.png")

    restart_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100, "image/UI/Buttons/PlayText/Default@3x.png", "Restart",
                            "image/UI/Buttons/PlayText/Hover@3x.png", "sound/japan.mp3")

    continue_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100,
                             "image/UI/Buttons/PlayText/Default@3x.png", "Continue", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/japan.mp3")

    menu_defeat_button = Button((screen_obj.width + 50) / 2, screen_obj.height / 2, 200, 100, "image/UI/Buttons/PlayText/Default@3x.png",
                                "Menu", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/japan.mp3")




    bullets_left = 10
    bullet = pygame.image.load('image/bullet.png').convert_alpha()
    bullets = []


    running = True

    while running:

        main_location.draw_background(screen)

        for part_back in partial_backgrounds:
            part_back.draw(screen)

        platforms.draw(screen)
        for platform in platforms:
            if isinstance(platform, MovingPlatform):
                platform.slide()

        if gameplay and not pause:

            blacksmith.animation(screen)
            blacksmith.check_animation_count()


            for enemy_group in enemies:
                for enemy in enemy_group:
                    enemy.update(screen, enemy_group)


            if ghost_list:
                for (i, el) in enumerate(ghost_list):
                    screen.blit(ghost, el)
                    el.x -= 7

                    if el.x < -10:
                        ghost_list.pop(i)

                    if player.rect.colliderect(el):
                        gameplay = False

            player.update(screen, main_location, partial_backgrounds, platforms, enemies)


            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 4

                    if el.x > 641:
                        bullets.pop(i)

                    if ghost_list:
                        for (index, ghost_el) in enumerate(ghost_list):
                            if el.colliderect(ghost_el):
                                ghost_list.pop(index)
                                bullets.pop(i)

        else:
            main_location.sound.stop()

            if pause:
                pause_label.draw(screen)
                continue_button.draw(screen)
            else:
                lose_label.draw(screen)
                restart_button.draw(screen)

            menu_defeat_button.draw(screen)

            for btn in [restart_button, menu_defeat_button, continue_button]:
                btn.check_hover(pygame.mouse.get_pos())

            lose_label.draw_cursor(screen)



        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                pause = True


            if event.type == pygame.USEREVENT:
                if event.button == restart_button or event.button == menu_defeat_button:
                    main_location.sound.play()
                    gameplay = True
                    player.x = screen_obj.width // 2
                    player.y = screen_obj.height - (40 + 60) * screen_obj.height_scale
                    ghost_list.clear()
                    bullets.clear()
                    bullets_left = 10

                if event.button == menu_defeat_button:
                    running = False

                if event.button == continue_button:
                    main_location.sound.play()
                    pause = False

            if pause:
                for btn in [menu_defeat_button, continue_button]:
                    btn.handle_event(event)
            else:
                for btn in [menu_defeat_button, restart_button]:
                    btn.handle_event(event)

            if event.type == ghost_timer:
                ghost_list.append(ghost.get_rect(topleft=(650, 300)))

            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_e and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player.x + 15, player.y + 10)))
                bullets_left -= 1


        pygame.time.delay(constants.DELAY)
        clock.tick(constants.MAX_FPS)

        pygame.display.flip()




if __name__ == "__main__":
    Menu.draw_menu(main_menu, screen_obj.screen, game_on)

