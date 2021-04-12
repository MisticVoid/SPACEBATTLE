import pygame
from Player import *
from GameEngine import *
from MapElement import *
import Geometry


class Level:
    def __init__(self, playerProperties, sizeX: int, sizeY: int, gameEngine):
        self.screenSizeX = sizeX
        self.screenSizeY = sizeY

        self.screen = pygame.display.set_mode((sizeX, sizeY))
        self.background = pygame.Surface((sizeX, sizeY))
        self.engine = gameEngine

        p = playerProperties
        self.player = Player(*playerProperties)

        self.mapEl = []

        # letter replace next lines with map loader
        el=MapElement(0, 0, 1000, 1000, "space1.jpeg", ((0, 0), (1000, 0), (1000, 1000), (0, 500)))
        self.addMapEl(el)
        el = MapElement(1000, 1000, 100, 100, "space1.jpeg")  # if el is a rect it not need cords
        self.addMapEl(el)
        el = MapElement(1000, 400, 1000, 200, "space1.jpeg")
        self.addMapEl(el)

    def addMapEl(self,element):
        self.mapEl.append(element)

    def update(self, deltaTime):
        self.player.nextCycle(deltaTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()

        keys = pygame.key.get_pressed()


        if keys[K_UP]:
            self.player.accelerate(deltaTime)
        if keys[K_DOWN]:
            self.player.reduceSpeed(deltaTime)
        if keys[K_LEFT]:
            self.player.rotateLeft(deltaTime)
        if keys[K_RIGHT]:
            self.player.rotateRight(deltaTime)


    def display(self):
        s = self.player.draw()
        x, y = int(self.player.posX), int(self.player.posY)
        self.screen.fill(pygame.Color(0, 0, 0))

        for element in self.mapEl:
            self.blend(self.screen,element,x,y)

        pygame.draw.circle(s, (255, 0, 0), (s.get_rect().width // 2, s.get_rect().height // 2), 1)
        self.screen.blit(s, (self.screenSizeX//2 - s.get_rect().width//2, self.screenSizeY//2 - s.get_rect().height//2))
        pygame.display.flip()

    def blend(self,screen,element,playerPosX,playerPosY,center=False):
        if center:
            xl = element.posX -element.sizeX//2 - playerPosX + self.screenSizeX // 2
            yu = element.posY-element.sizeY//2 - playerPosY + self.screenSizeY // 2
        else:
            xl = element.posX - playerPosX+self.screenSizeX//2
            yu = element.posY - playerPosY + self.screenSizeY // 2
        xr = xl + element.sizeX
        yd = yu + element.sizeY
        if (0<=xl<=self.screenSizeX or 0<=xr<=self.screenSizeX) and (0<=yu<=self.screenSizeY or 0<=yd<=self.screenSizeY):
            xlr = max(0, xl)
            xrr = min(xr, self.screenSizeX)
            yur = max(yu, 0)
            ydr = min(yd, self.screenSizeY)
            R = Rect(max(0,-xl), max(0,-yu), xrr - xlr, ydr -yur)
            screen.blit(element.draw(), (xlr, yur), R)

