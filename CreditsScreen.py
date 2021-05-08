import pygame_menu
import pygame

class CreditsScreen:
    def __init__(self, menu, sizeX=1920, sizeY=1020):
        self.mainMenu = menu

        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.background_color = (0, 0, 0, 0)

        self.menu = pygame_menu.Menu(sizeY, sizeX, 'Credits', theme=mytheme)
        self.menu.add.label('Congratulations!')
        self.menu.add.vertical_margin(100)
        self.menu.add.label('GG')
        self.menu.add.label('WP')
        self.menu.add.vertical_margin(100)

        self.menu.add.button('Main Menu', self.runMainMenu)


    def runMainMenu(self):
        self.menu.disable()


    def runMenu(self):
        self.menu.enable()
        self.menu.mainloop(self.getScreen())

    def getScreen(self):
        return self.mainMenu.getScreen()