import pygame_menu
import pygame

class LoseMenu:
    def __init__(self, menu, sizeX=1920, sizeY=1020):
        self.mainMenu = menu

        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.background_color = (0, 0, 0, 0)

        self.menu = pygame_menu.Menu(sizeY, sizeX, 'You lost', theme=mytheme)
        self.menu.add.button('Retry', self.retry)
        self.menu.add.button('Main Menu', self.runMainMenu)

    def runMainMenu(self):
        self.menu.disable()
        self.mainMenu.runMenu()

    def runMenu(self):
        self.menu.enable()
        self.menu.mainloop(self.getScreen)

    def retry(self):
        self.menu.disable()
        self.mainMenu.startGame()

    def getScreen(self):
        return self.mainMenu.getScreen
