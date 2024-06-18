"""
A script to initialize a Pygame application for a game called 'CS-3'.

It sets up the main display window, initializes Pygame modules,
and creates a main menu using imported classes from game.src.menus
and game.src.screen modules.

Modules imported:
- Menu, MainMenu: Classes for handling menus from game.src.menus
- screen_obj: Object managing the screen from game.src.screen
- pygame: Pygame library for game development

Initialization steps:
1. Sets the window caption to "CS-3".
2. Sets the window icon using an image loaded from "image/icon_game.webp".
3. Loads a custom font from "fonts/Honk-Regular-VariableFont_MORF,SHLN.ttf" with a size of 30.
4. Renders a text surface with the text 'Long time ago...' using the loaded font and orange color.
5. Creates an instance of MainMenu() to initialize the main menu.

Execution:
- If this script is run directly (__name__ == "__main__"), it calls Menu.draw_menu() 
  to draw the main menu
  on the screen managed by screen_obj.screen.

Note: The paths and specific functionalities are assumed based on the provided code snippet.
"""
from game.src.menus import Menu, MainMenu
from game.src.screen import screen_obj

import pygame

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
