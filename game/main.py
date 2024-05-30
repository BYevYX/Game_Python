import pygame
from game.src.menus import Menu, MainMenu
from game.src.screen import screen_obj

pygame.init()


pygame.display.set_caption("CS-3")
pygame.display.set_icon(pygame.image.load("image/icon_game.webp"))


# проработать шрифт
myfont = pygame.font.Font("fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf", 30)
text_surface = myfont.render('Long time ago...', True, 'orange')


# создание меню
main_menu = MainMenu()



if __name__ == "__main__":
    Menu.draw_menu(main_menu, screen_obj.screen)

