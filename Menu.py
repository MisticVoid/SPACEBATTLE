import pygame_menu
import pygame
from PauseMenu import PauseMenu
from SettingsMenu import SettingsMenu
from WinMenu import WinMenu
from LoseMenu import LoseMenu
from CreditsScreen import CreditsScreen
from GameEngine import *

playerProperties = {"posX": 100, "posY": 100, "speed": 0, "maxSpeedForward": 400, "maxSpeedBackward": 100,
                                "acceleration": 100, "angle": 0,
                                "rotationSpeed": 2 * pi, "sizeX": 50, "sizeY": 25, "maxHealth": 200, "damage": 25,
                                "shotDelayTime": 0.5, "missileSpeed": 1000}

MAX_LEVEL=5

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



        self.pauseMenu = PauseMenu(self, sizeX, sizeY)
        self.settingsMenu = SettingsMenu(self, sizeX, sizeY)
        self.winMenu = WinMenu(self, sizeX, sizeY)
        self.loseMenu = LoseMenu(self, sizeX, sizeY)
        self.creditsScreen = CreditsScreen(self, sizeX, sizeY)

        self.menu.add.button('Play', self.startGame)
        self.menu.add.button('Settings', self.settingsMenu.menu)
        self.lvlSelector = self.menu.add.selector('Level :', [(str(i), i) for i in range(MAX_LEVEL)], onchange=self.setLevel, selector_id='lvl_selector')
        self.menu.add.selector('Difficulty :', [(" Easy ", 0), ("Medium", 1), (" Hard ", 2)], onchange=self.setDifficulty)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def setLevel(self, _, level):
        self.level = level

    def setDifficulty(self, _, val):
        pass

    def nextLevel(self):
        self.level += 1
        self.startGame()

    def startGame(self):
        self.engine = GameEngine(playerProperties, self, self.level, settings = self.settingsMenu.getSettings())
        score = self.engine.run()
        if score == None:
            self.runMenu()
        elif score == 'Win':
            self.win()
        elif score == 'Lose':
            self.lose()

    def runMenu(self):
        self.menu.enable()
        self.menu.mainloop(self.screen)

    def runSettings(self):
        self.settingsMenu.runMenu(self)

    def pause(self):
        self.pauseMenu.runMenu()

    def win(self):
        if self.level+1 < MAX_LEVEL:
            self.winMenu.runMenu()
        else:
            self.creditsScreen.runMenu()

    def lose(self):
        self.loseMenu.runMenu()

    def getScreen(self):
        return self.screen


if __name__ == "__main__":
    pygame.init()
    menu = Menu()
    menu.runMenu()




