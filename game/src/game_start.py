import pygame
import sys
from game.src.screen import screen_obj
from game.src.button import Button
from game.src.labels import Label
from game.src.platforms import MovingPlatform
import game.src.constants as constants
import game.src.creater as creater


class GameOn:
    def __init__(self, player):
        self.clock = pygame.time.Clock()
        self.main_location, self.partial_backgrounds = creater.create_location()
        self.platforms = creater.create_platforms()
        self.enemies = creater.create_enemies()
        self.waves = pygame.sprite.Group()

        creater.add_moving_platforms(self.platforms)

        # self.player = FireKnight(screen_obj.width // 2, screen_obj.height - 120 * screen_obj.height_scale)
        self.player = player
        self.npcs = creater.create_npc()

        self.gameplay = True
        self.pause = False
        self.running = True

        self.is_restart = False

        self.lose_label = Label(screen_obj.width, screen_obj.height, None, 72, 'You Lose!',
                                (193, 196, 199), "image/UI/Panel/Window/Medium.png")
        self.pause_label = Label(screen_obj.width, screen_obj.height, None, 72, 'Pause',
                                 (193, 196, 199), "image/UI/Panel/Window/Medium.png")

        self.restart_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100,
                                     "image/UI/Buttons/PlayText/Default@3x.png", "Restart",
                                     "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

        self.continue_button = Button((screen_obj.width - 450) / 2, screen_obj.height / 2, 200, 100,
                                      "image/UI/Buttons/PlayText/Default@3x.png", "Continue",
                                      "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

        self.menu_defeat_button = Button((screen_obj.width + 50) / 2, screen_obj.height / 2, 200, 100,
                                         "image/UI/Buttons/PlayText/Default@3x.png",
                                         "Menu", "image/UI/Buttons/PlayText/Hover@3x.png", "sound/knopka-schelchok.mp3")

    def handle_events(self, screen, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if self.gameplay and event.key == pygame.K_ESCAPE:
                    self.pause = True

                if event.key == pygame.K_e:
                    collided_npc = pygame.sprite.spritecollideany(self.player, self.npcs)
                    if collided_npc and collided_npc.has_shop:
                        collided_npc.open_shop(screen, self.player)

            elif event.type == pygame.USEREVENT:
                if event.button == self.restart_button or event.button == self.menu_defeat_button:
                    self.main_location.sound.play()
                    self.gameplay = True
                    self.player.x = screen_obj.width // 2
                    self.player.y = screen_obj.height - 100 * screen_obj.height_scale
                    self.player.current_hp = 5

                if event.button == self.menu_defeat_button:
                    self.running = False

                if event.button == self.restart_button:
                    self.is_restart = True

                if event.button == self.continue_button:
                    self.main_location.sound.play()
                    self.pause = False

            if self.pause:
                for btn in [self.menu_defeat_button, self.continue_button]:
                    btn.handle_event(event)
            elif not self.gameplay:
                for btn in [self.menu_defeat_button, self.restart_button]:
                    btn.handle_event(event)

    def draw_back_platforms(self, screen):
        self.main_location.draw_background(screen)

        for part_back in self.partial_backgrounds:
            part_back.draw(screen)

        self.platforms.draw(screen)

    def start(self, screen):
        self.main_location.sound.play(-1)

        while self.running:

            self.draw_back_platforms(screen)

            for platform in self.platforms:
                if isinstance(platform, MovingPlatform):
                    platform.slide()

            if self.gameplay and not self.pause:

                for enemy_group in self.enemies:
                    enemy_group.update(screen, enemy_group)

                for wave in self.waves:
                    wave.deal_damage(self.enemies)

                self.npcs.update(screen)

                if self.player.current_hp <= 0:
                    self.gameplay = False

                self.player.update(screen, self.main_location, self.partial_backgrounds, self.platforms, self.enemies, self.npcs)

                # self.waves.update()
                # self.waves.draw(screen)

            else:
                self.main_location.sound.stop()

                if self.pause:
                    self.pause_label.draw(screen)
                    self.continue_button.draw(screen)
                else:
                    self.lose_label.draw(screen)
                    self.restart_button.draw(screen)

                self.menu_defeat_button.draw(screen)

                for btn in [self.restart_button, self.menu_defeat_button, self.continue_button]:
                    btn.check_hover(pygame.mouse.get_pos())

                self.lose_label.draw_cursor(screen)


            pygame.display.update()

            self.handle_events(screen, pygame.event.get())

            if self.is_restart:
                return self.is_restart

            pygame.time.delay(constants.DELAY)
            self.clock.tick(constants.MAX_FPS)

            pygame.display.flip()
