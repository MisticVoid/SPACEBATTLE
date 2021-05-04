import pygame_menu
import pygame
from PauseMenu import PauseMenu
from GameEngine import *

playerProperties = {"posX": 100, "posY": 100, "speed": 0, "maxSpeedForward": 400, "maxSpeedBackward": 100,
                                "acceleration": 100, "angle": 0,
                                "rotationSpeed": 2 * pi, "sizeX": 50, "sizeY": 25, "maxHealth": 100, "damage": 10,
                                "shotDelayTime": 1, "missileSpeed": 1000}



class Menu:
    def __init__(self,  sizeX=1920, sizeY=1020):
        pygame.init()
        self.level=0
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.engine = None
        self.screen = pygame.display.set_mode((sizeX, sizeY))

        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.background_color = (0,0,0,0)
        self.menu = pygame_menu.Menu(sizeY, sizeX, 'Main menu', theme=mytheme)

        self.menu.add.button('Play', self.startGame)
        self.menu.add.button('Settings', self.setSettings)
        self.menu.add.selector('Level :', [(str(i), i) for i in range(10)], onchange=self.setLevel)
        self.menu.add.selector('Level :', [(" Easy ", 0), ("Medium", 1), (" Hard ", 2)], onchange=self.setDifficulty)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.pauseMenu = PauseMenu(self, sizeX, sizeY)

    def setSettings(self):
        pass

    def setLevel(self, _, level):
        self.level = level

    def setDifficulty(self, _, val):
        pass

    def startGame(self):
        self.engine = GameEngine(playerProperties, self, self.level)
        self.engine.run()

    def runMenu(self):
        self.menu.mainloop(self.screen)


    def pause(self):
        self.pauseMenu.runMenu()


if __name__ == "__main__":
    pygame.init()
    menu = Menu()
    menu.runMenu()




