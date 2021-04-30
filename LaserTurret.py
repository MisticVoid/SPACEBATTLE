from TurretAbstract import AbstractTurret
from ClosestPointCross import ClosestPointCross
from Geometry import twoPointToLine,squarePointDis
from laserTurretVisual import LaserTurretVisual
from pygame import draw,Color

class PlayerInstantDamage:
    def damage(self,player,damage):
        player.hit(damage)

class LaserTurret(AbstractTurret):
    def __init__(self, posX: int, posY: int, size: int, maxHealth: int, coolDown: float,
                 rotationSpeed: float, angle: float,aimTime: float,Level, damage: int):
        super().__init__(posX, posY, size, size, maxHealth, coolDown, rotationSpeed, angle)
        self.aimTime=aimTime
        self.aimingTime=0
        self.ClosePointSys=ClosestPointCross(self)
        self.Level=Level
        self.isOnLineV=False
        self.damage=damage
        self.visual = LaserTurretVisual(size,self)
        self.target=None

    def isOnLine(self):
        self.ClosePointSys.reset()
        center = (self.posX + self.sizeX // 2, self.posY + self.sizeY // 2)
        front = self.getPoint()
        self.ClosePointSys.setLine(*twoPointToLine(center, front), center, front)
        self.ClosePointSys.analyzeGroupShapes(self.Level.turrets)
        self.ClosePointSys.analyzeGroupShapes(self.Level.obstacles)
        x, y = self.ClosePointSys.getPoint()
        #print("///",x,y)
        self.ClosePointSys.analyzeShape(self.Level.player.getPoints())
        x2, y2 = self.ClosePointSys.getPoint()
        #print(x2, y2)
        self.isOnLineV=x!=x2 or y!=y2
        self.target=(x2,y2)

    def correctAimingTime(self,deltaTime):
        if self.isOnLineV:
            self.aimingTime+=deltaTime
        else:
            self.aimingTime=0

    def shoot(self,posX:float,posY:float) -> None:
        if self.currentCoolDown == 0 and self.canShoot(posX,posY) and squarePointDis((posX,posY),(self.posX,self.posY))<4000000:
            self.aimingTime = 0
            self.currentCoolDown = self.coolDown
            self.Level.player.hit(self.damage)
        return None

    def canShoot(self, posX: float, posY: float):
        #print(self.aimTime,self.aimingTime,self.isOnLineV,self.angle)
        return self.aimTime<=self.aimingTime and self.isOnLineV

    def nextCycle(self, deltaTime: float, posX: float, posY: float) -> None:
        super().nextCycle(deltaTime,posX,posY)
        #print(self.angle)
        self.isOnLine()
        self.correctAimingTime(deltaTime)

    def effect(self,screen,screenX,screenY,x,y):
        if self.isOnLineV and squarePointDis((x,y),(self.posX,self.posY))<4000000:
            begin=list(self.getPoint())
            begin[0]=begin[0]-x+screenX//2
            begin[1] = begin[1] - y+screenY//2
            target=list(self.target)
            target[0] = target[0] - x+screenX//2
            target[1] = target[1] - y+screenY//2
            draw.line(screen,Color(255,0,0),begin,target)

