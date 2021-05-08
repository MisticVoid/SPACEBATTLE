import pygame_menu
import pygame

class SettingsMenu:
    def __init__(self, menu, sizeX=1920, sizeY=1020):
        self.parent = None

        self.settings = {"MOUSE_CONTROL": True}

        mytheme = pygame_menu.themes.THEME_DARK.copy()
        mytheme.background_color = (0, 0, 0, 0)
        self.menu = pygame_menu.Menu(sizeY, sizeX, 'Settings', theme=mytheme)
        self.menu.add.toggle_switch('Mouse control', True, onchange=self.setMouseControl)
        self.menu.add.button('Back', pygame_menu.events.BACK)

    def getSettings(self):
        return self.settings

    def setMouseControl(self, a):
        self.settings['MOUSE_CONTROL'] = a
