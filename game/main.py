import pygame
import sys
from game.src.menus import Menu, MainMenu
from game.src.screen import screen_obj
from game.src.button import Button
from game.src.player import Player
from game.src.locations import Locations
from game.src.labels import Label
from game.src import npc

pygame.init()


pygame.display.set_caption("Mega-Igra")
pygame.display.set_icon(pygame.image.load("image/icon_game.webp"))


# проработать шрифт
myfont = pygame.font.Font("fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf", 30)
text_surface = myfont.render('Long time ago...', True, 'orange')




# создание персонажа
player = Player()

# создание npc
blacksmith = npc.Blacksmith(270, 270)

# создание меню
main_menu = MainMenu()



def game_on(screen):
    clock = pygame.time.Clock()

    location = Locations('image/back.jpg', 'sound/bg-sound.mp3')
    location.sound.play()

    ghost = pygame.image.load('image/ghost.png').convert_alpha()
    ghost_list = []

    ghost_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(ghost_timer, 5000)

    gameplay = True

    lose_label = Label(screen_obj.width, screen_obj.height, None, 72, 'You Lose!', (193, 196, 199), "image/UI/Panel/Window/Medium.png")
    restart_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100, "image/UI/Buttons/PlayText/Default@3x.png", "Restart",
                            "image/UI/Buttons/PlayText/Hover@3x.png", "sound/japan.mp3")

    menu_defeat_button = Button((screen_obj.width + 50) / 2, screen_obj.height / 2, 200, 100, "image/UI/Buttons/PlayText/Default@3x.png",
                            "Menu","image/UI/Buttons/PlayText/Hover@3x.png", "sound/japan.mp3")


    bullets_left = 10
    bullet = pygame.image.load('image/bullet.png').convert_alpha()
    bullets = []

    MAX_FPS = 60

    running = True

    while running:

        screen.blit(location.background, (location.background_x, 0))
        screen.blit(location.background, (location.background_x + 641, 0))

        if gameplay:
            player.change_rect()

            blacksmith.animation(screen)
            blacksmith.check_animation_count()

            if ghost_list:
                for (i, el) in enumerate(ghost_list):
                    screen.blit(ghost, el)
                    el.x -= 7

                    if el.x < -10:
                        ghost_list.pop(i)

                    if player.rect.colliderect(el):
                        gameplay = False

            location.background_x -= 3
            if location.background_x == -639:
                location.background_x = 0

            keys = pygame.key.get_pressed()

            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x > 50:
                player.x -= player.speed
                if not player.is_jump:
                    player.walk_left(screen)

            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x < 600:
                player.x += player.speed
                if not player.is_jump:
                    player.walk_right(screen)

            elif not player.is_jump:
                player.stay(screen)

            player.check_animation_count()

            if not player.is_jump:
                if keys[pygame.K_SPACE]:
                    player.is_jump = True
            else:
                player.jump_right(screen)
                if player.jump_height >= -7:
                    if player.jump_height > 0:
                        player.y -= (player.jump_height ** 2) / 2
                    else:
                        player.y += (player.jump_height ** 2) / 2
                    player.jump_height -= 1
                else:
                    player.is_jump = False
                    player.jump_height = 7

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
            location.sound.stop()
            lose_label.draw(screen)

            restart_button.draw(screen)
            menu_defeat_button.draw(screen)

            for btn in [restart_button, menu_defeat_button]:
                btn.check_hover(pygame.mouse.get_pos())

            lose_label.draw_cursor(screen)
            MAX_FPS = 60

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == restart_button:
                location.sound.play()
                gameplay = True
                player.x = 150
                ghost_list.clear()
                bullets.clear()
                bullets_left = 10

            if event.type == pygame.USEREVENT and event.button == menu_defeat_button:
                gameplay = True
                player.x = 150
                ghost_list.clear()
                bullets.clear()
                bullets_left = 10

                running = False


            for btn in [restart_button, menu_defeat_button]:
                btn.handle_event(event)

            if event.type == ghost_timer:
                ghost_list.append(ghost.get_rect(topleft=(650, 300)))

            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_e and bullets_left > 0:
                bullets.append(bullet.get_rect(topleft=(player.x + 15, player.y + 10)))
                bullets_left -= 1

        clock.tick(MAX_FPS)

        pygame.display.flip()



Menu.draw_menu(main_menu, screen_obj.screen, game_on)

