import pygame
from Player import *
from GameEngine import *
from MapElement import *
import Geometry
from KeyState import KeyState
from StandardTurret import StandardTurret
from RocketTurret import RocketTurret


class Level:
    def __init__(self, playerProperties, sizeX: int, sizeY: int, gameEngine):
        self.screenSizeX = sizeX
        self.screenSizeY = sizeY

        self.screen = pygame.display.set_mode((sizeX, sizeY))
        self.background = pygame.Surface((sizeX, sizeY))
        self.engine = gameEngine

        self.player = Player(**playerProperties)

        self.keyControl = {pygame.K_SPACE:KeyState(lambda: self.addMissile(self.player.shoot()))}

        self.mapEl = []
        self.missiles = []  # latter replace with something more efficient
        self.turrets = []

        # letter replace next lines with map loader
        el=MapElement(0, 0, 1000, 1000, "space1.jpeg", ((0, 0), (1000, 0), (1000, 1000), (0, 500)))
        self.addMapEl(el)
        el = MapElement(1000, 1000, 100, 100, "space1.jpeg")  # if el is a rect it not need cords
        self.addMapEl(el)
        el = MapElement(1000, 400, 1000, 200, "space1.jpeg")
        self.addMapEl(el)

        self.turrets.append(StandardTurret(500,500,75,20,100,2,pi/2,0,1000))
        self.turrets.append(RocketTurret(500,700,75,100,100,5,pi/2,0,350,self.player))

    def addMapEl(self,element):
        self.mapEl.append(element)

    def update(self, deltaTime):
        self.player.nextCycle(deltaTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()

            if event.type == pygame.KEYDOWN:
                if event.key in self.keyControl:
                    self.keyControl[event.key].press()
                    self.keyControl[event.key].execSingle()

            if event.type == pygame.KEYUP:
                if event.key in self.keyControl:
                    self.keyControl[event.key].release()


        keys = pygame.key.get_pressed()


        if keys[K_UP]:
            self.player.accelerate(deltaTime)
        if keys[K_DOWN]:
            self.player.reduceSpeed(deltaTime)
        if keys[K_LEFT]:
            self.player.rotateLeft(deltaTime)
        if keys[K_RIGHT]:
            self.player.rotateRight(deltaTime)

        for missile in self.missiles:
            missile.nextCycle(deltaTime)

        for turret in self.turrets:
            turret.nextCycle(deltaTime,self.player.posX,self.player.posY)
            self.addMissile(turret.shoot(self.player.posX,self.player.posY))

    def display(self):
        s = self.player.draw()
        x, y = int(self.player.posX), int(self.player.posY)
        self.screen.fill(pygame.Color(0, 0, 0))

        for element in self.mapEl:
            self.blend(self.screen,element,x,y)

        self.screen.blit(s, (self.screenSizeX//2 - s.get_rect().width//2, self.screenSizeY//2 - s.get_rect().height//2))

        for missile in self.missiles:
            self.blend(self.screen,missile,x,y,True)

        for turret in self.turrets:
            self.blend(self.screen,turret,x,y)
        pygame.display.flip()

    def blend(self,screen,element,playerPosX,playerPosY,center=False):
        surf=element.draw()
        if center:
            xl = element.posX -surf.get_rect().width//2 - playerPosX + self.screenSizeX // 2
            yu = element.posY-surf.get_rect().height//2 - playerPosY + self.screenSizeY // 2
        else:
            xl = element.posX - playerPosX+self.screenSizeX//2
            yu = element.posY - playerPosY + self.screenSizeY // 2
        xr = xl + surf.get_rect().width
        yd = yu + surf.get_rect().height
        if (0<=xl<=self.screenSizeX or 0<=xr<=self.screenSizeX) and (0<=yu<=self.screenSizeY or 0<=yd<=self.screenSizeY):
            xlr = max(0, xl)
            xrr = min(xr, self.screenSizeX)
            yur = max(yu, 0)
            ydr = min(yd, self.screenSizeY)
            R = Rect(max(0,-xl), max(0,-yu), xrr - xlr, ydr -yur)
            #print(R,element.posX,element.posY)
            screen.blit(surf, (xlr, yur), R)

    def addMissile(self,missile):
        if missile is not None:
            self.missiles.append(missile)

