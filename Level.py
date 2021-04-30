import pygame
from Player import *
from MapElement import *
from KeyState import KeyState
from StandardTurret import StandardTurret
from RocketTurret import RocketTurret, RocketMissile
from Obstacle import Obstacle
from Collision import solveCollisions

MOUSE_CONTROL = True  # change to False to back to a/d rotating

class Level:
    def __init__(self, playerProperties, sizeX: int, sizeY: int, gameEngine):
        self.screenSizeX = sizeX
        self.screenSizeY = sizeY

        self.screen = pygame.display.set_mode((sizeX, sizeY))
        self.background = pygame.Surface((sizeX, sizeY))
        self.engine = gameEngine

        self.player = Player(**playerProperties)

        self.keyControl = {pygame.K_SPACE:KeyState(lambda: self.addPlayerMissile(self.player.shoot()))}

        self.obstacles = [Obstacle(400, 400, 100, 100, (50,50,50), points = ((0, 50), (90, 80), (100, 10), (0,0)))]
        self.obstacles.append(Obstacle(-100, -100, 1200, 100, visible = False))
        self.obstacles.append(Obstacle(-100, -100, 100, 1200, visible = False))
        self.obstacles.append(Obstacle(-100, 1000, 1200, 100, visible=False))


        self.mapEl = []
        self.playerMissiles = set()
        self.missiles = set()
        self.turrets = []

        # letter replace next lines with map loader
        el = MapElement(0, 0, 1000, 1000, "space1.jpeg", ((0, 0), (1000, 0), (1000, 1000), (0, 500)))
        self.addMapEl(el)
        el = MapElement(1000, 1000, 100, 100, "space1.jpeg")  # if el is a rect it not need cords
        self.addMapEl(el)
        el = MapElement(1000, 400, 1000, 2000, "space1.jpeg")
        self.addMapEl(el)


        self.turrets.append(StandardTurret(500,500,75,20,100,2,pi/2,0,1000))
        self.turrets.append(RocketTurret(500,700,75,100,100,5,pi/2,0,600,self.player))

        for i in range(5,50, 5):
            self.turrets.append(StandardTurret(i*200+500, 500, 75, 20, 100, 2, pi / 2, 0, 1000))
            self.turrets.append(RocketTurret(i*200+500, 700, 75, 100, 100, 5, pi / 2, 0, 600, self.player))
            self.obstacles.append(Obstacle(200 * i - 100, -100, 1200, 100, visible=False))
            self.obstacles.append(Obstacle(200 * i - 100, 1000, 1200, 100, visible=False))
            self.addMapEl( MapElement(200*i, 0, 1000, 1000, "space1.jpeg", ) )

        self.obstacles.append(Obstacle(8900, -100, 100, 1200, visible = False))


    def filterElements(self, elements):
        playerPosX, playerPosY = int(self.player.posX), int(self.player.posY)
        filtered = []
        for element in elements:
            xl = element.posX - playerPosX + self.screenSizeX // 2
            yu = element.posY - playerPosY + self.screenSizeY // 2
            xr = xl + element.sizeX
            yd = yu + element.sizeY
            if (0 <= xl <= self.screenSizeX or 0 <= xr <= self.screenSizeX or (xl <= 0 and xr >= self.screenSizeX)) and (
                    0 <= yu <= self.screenSizeY or 0 <= yd <= self.screenSizeY or (yu <= 0 and yd >= self.screenSizeY)):
                filtered.append(element)
        return filtered



    def filterMissiles(self):
        playerPosX, playerPosY = int(self.player.posX), int(self.player.posY)
        toDel = set()
        for element in self.missiles:
            if not isinstance(element, RocketMissile):
                x = element.posX - playerPosX + self.screenSizeX // 2
                y = element.posY - playerPosY + self.screenSizeY // 2
                if not((0 <= x <= self.screenSizeX) and (0 <= y <= self.screenSizeY)):
                    toDel.add(element)

        self.missiles -= toDel
        toDel = set()
        for element in self.playerMissiles:
            x = element.posX - playerPosX + self.screenSizeX // 2
            y = element.posY - playerPosY + self.screenSizeY // 2
            if not ((0 <= x <= self.screenSizeX) and (0 <= y <= self.screenSizeY)):
                toDel.add(element)
        self.playerMissiles -= toDel



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

        if MOUSE_CONTROL:
            mosePos=pygame.mouse.get_pos()
            #print(mosePos,self.player.posX,self.player.posY)
            self.player.followMouse(deltaTime,(mosePos[0]-self.screenSizeX//2, mosePos[1]-self.screenSizeY//2))
        else:
            if keys[K_a]:
                self.player.rotateLeft(deltaTime)
            if keys[K_d]:
                self.player.rotateRight(deltaTime)
        if keys[K_w]:
            self.player.accelerate(deltaTime)
        if keys[K_s]:
            self.player.reduceSpeed(deltaTime)

        turrets = self.filterElements(self.turrets)
        obstacles = self.filterElements(self.obstacles)
        self.filterMissiles()

        #solveCollisions(self.player, self.obstacles, self.turrets, self.playerMissiles, self.missiles, deltaTime)
        solveCollisions(self.player, obstacles, turrets, self.playerMissiles, self.missiles, deltaTime)

        for missile in self.missiles:
            missile.nextCycle(deltaTime)

        for missile in self.playerMissiles:
            missile.nextCycle(deltaTime)

       # for turret in self.turrets:
       #     turret.nextCycle(deltaTime,self.player.posX,self.player.posY)
       #     self.addMissile(turret.shoot(self.player.posX,self.player.posY))

        for turret in turrets:
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

        for missile in self.playerMissiles:
            self.blend(self.screen,missile,x,y,True)

        for turret in self.turrets:
            self.blend(self.screen,turret,x,y)

        for obstacle in self.obstacles:
            self.blend(self.screen,obstacle,x,y)
        pygame.display.flip()

    def blend(self,screen,element,playerPosX,playerPosY,center=False):
        surf=element.draw()
        if not surf:
            return
        if center:
            xl = element.posX -surf.get_rect().width//2 - playerPosX + self.screenSizeX // 2
            yu = element.posY-surf.get_rect().height//2 - playerPosY + self.screenSizeY // 2
        else:
            xl = element.posX - playerPosX+self.screenSizeX//2
            yu = element.posY - playerPosY + self.screenSizeY // 2
        xr = xl + surf.get_rect().width
        yd = yu + surf.get_rect().height
        #if (0 <= xl <= self.screenSizeX or 0 <= xr <= self.screenSizeX) and (0 <= yu <= self.screenSizeY or 0 <= yd <= self.screenSizeY):
        if (0<=xl<=self.screenSizeX or 0<=xr<=self.screenSizeX or (xl<=0 and xr>=self.screenSizeX)) and (0<=yu<=self.screenSizeY or 0<=yd<=self.screenSizeY or (yu<=0 and yd>=self.screenSizeY)):
            xlr = max(0, xl)
            xrr = min(xr, self.screenSizeX)
            yur = max(yu, 0)
            ydr = min(yd, self.screenSizeY)
            R = Rect(max(0,-xl), max(0,-yu), xrr - xlr, ydr -yur)
            #print(R,element.posX,element.posY)
            screen.blit(surf, (xlr, yur), R)

    def addMissile(self,missile):
        if missile is not None:
            self.missiles.add(missile)

    def addPlayerMissile(self,missile):
        if missile is not None:
            self.playerMissiles.add(missile)

