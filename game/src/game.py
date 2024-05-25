def move(self, keys):
    self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > screen_obj.width * 0.03:
        self.x -= self.speed

    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < screen_obj.width * 0.97:
        self.x += self.speed

    if not self.is_jump:
        if keys[pygame.K_SPACE]:
            self.is_jump = True

    else:
        if self.y_velocity >= -self.jump_height:
            if self.y_velocity > 0:
                self.y -= (self.y_velocity ** 2) / 2
            else:
                self.y += (self.y_velocity ** 2) / 2
            self.y_velocity -= 1
        else:
            self.is_jump = False
            self.y_velocity = self.jump_height


def draw(self, screen, keys):
    self.animate_hp(screen)

    if not self.is_jump:
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


def check_collisions(self, platforms, keys):
    player_rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

    for platform in platforms:
        if player_rect.colliderect(platform.rect):
            if self.y_velocity == 8:
                # Определяем сторону столкновения
                if self.x < platform.rect.x:  # Столкновение с левой стороны платформы
                    self.x = platform.rect.x - self.rect.width
                else:  # Столкновение с правой стороны платформы
                    self.x = platform.rect.right
            elif self.y_velocity > 0:  # Падение
                self.y = platform.rect.top - self.rect.height
                self.is_jump = False
                self.y_velocity = self.jump_height

            elif self.y_velocity < 0:  # Прыжок вверх
                self.y = platform.rect.bottom
                self.y_velocity = 0


