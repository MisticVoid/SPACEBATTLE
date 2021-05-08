import pygame_menu
import pygame

class WinMenu:
    def __init__(self, menu, sizeX=1920, sizeY=1020):
        self.mainMenu = menu

        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.background_color = (0, 0, 0, 0)

        self.menu = pygame_menu.Menu(sizeY, sizeX, 'You won!', theme=mytheme)
        self.menu.add.button('Next Level', self.nextLevel)
        self.menu.add.button('Main Menu', self.runMainMenu)


    def runMainMenu(self):
        self.menu.disable()


    def runMenu(self):
        self.menu.enable()
        self.menu.mainloop(self.getScreen())


    def nextLevel(self):
        self.menu.disable()
        self.mainMenu.nextLevel()

    def getScreen(self):
        return self.mainMenu.getScreen()