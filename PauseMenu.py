import pygame_menu
import pygame

class PauseMenu:
    def __init__(self, menu, sizeX=1920, sizeY=1020):
        self.engine = None
        self.mainMenu = menu

        mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
        mytheme.background_color = (0, 0, 0, 0)

        self.menu = pygame_menu.Menu(sizeY, sizeX, 'Paused', theme=mytheme)
        self.menu.add.button('Resume', self.resumeGame)
        self.menu.add.button('Main Menu', self.runMainMenu)


    def runMainMenu(self):
        self.mainMenu.runMainMenu()


    def runMenu(self):
        self.menu.mainloop(self.mainMenu.screen, clear_surface=False)


    def resumeGame(self):
        self.mainMenu.engine.run()