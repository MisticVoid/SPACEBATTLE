import pygame_menu
import pygame
from PauseMenu import PauseMenu
from SettingsMenu import SettingsMenu
from WinMenu import WinMenu
from LoseMenu import LoseMenu
from CreditsScreen import CreditsScreen
from GameEngine import *

playerDefaultProperties = {"posX": 100, "posY": 100, "speed": 0, "maxSpeedForward": 400, "maxSpeedBackward": 100,
                                "acceleration": 100, "angle": 0,
                                "rotationSpeed": 2 * pi, "sizeX": 50, "sizeY": 25, "maxHealth": 200, "damage": 25,
                                "shotDelayTime": 0.5, "missileSpeed": 1000}



class Menu:
    MAX_LEVEL = 6

    def __init__(self,  sizeX=1920, sizeY=1020):
        self.CURRENT_LMAX = 1
        pygame.init()
        pygame.mixer.init()
        self.level=1
        self.difficulty = 1.3
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
        self.lvlSelector = self.menu.add.selector('Level :', [(str(i), i) for i in range(1,self.CURRENT_LMAX+1)], onchange=self.setLevel, selector_id='lvl_selector')
        self.menu.add.selector('Difficulty :', [(" Easy ", 1.3), ("Medium", 1), (" Hard ", 0.7)], onchange=self.setDifficulty)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)



    def setLevel(self, _, level):
        self.level = level

    def setDifficulty(self, _, val):
        self.difficulty = val

    def nextLevel(self):
        self.level += 1
        self.startGame()

    def startGame(self):
        playerProperties = playerDefaultProperties.copy()
        playerProperties["maxHealth"] *= self.difficulty
        playerProperties["damage"] *= self.difficulty
        self.engine = GameEngine(playerProperties, self, self.level, settings = self.settingsMenu.getSettings())
        score = self.engine.run()
        if score == None:
            self.runMenu()
        elif score == 'Win':
            self.win()
        elif score == 'Lose':
            self.lose()

    def runMenu(self):
        self.lvlSelector.set_value(self.CURRENT_LMAX - 1)
        self.menu.enable()
        self.menu.mainloop(self.screen)

    def runSettings(self):
        self.settingsMenu.runMenu(self)

    def pause(self):
        self.pauseMenu.runMenu()

    def win(self):
        print("win")
        if self.level+1 < Menu.MAX_LEVEL:
            if self.level==self.CURRENT_LMAX:
                print("incrise")
                self.CURRENT_LMAX += 1
                self.lvlSelector.update_items([(str(i), i) for i in range(1, self.CURRENT_LMAX + 1)])
            self.winMenu.runMenu()
            self.lvlSelector.set_value(self.CURRENT_LMAX - 1)
            self.setLevel(None,self.CURRENT_LMAX)
        else:
            self.creditsScreen.runMenu()
            self.lvlSelector.set_value(self.CURRENT_LMAX - 1)
            self.setLevel(None, self.CURRENT_LMAX)

    def lose(self):
        self.loseMenu.runMenu()
        self.lvlSelector.set_value(self.CURRENT_LMAX - 1)
        self.setLevel(None, self.CURRENT_LMAX)

    def getScreen(self):
        return self.screen




