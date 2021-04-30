from TurretAbstract import AbstractTurret
from ClosestPointCross import ClosestPointCross
from Geometry import twoPointToLine

class LaserTurret(AbstractTurret):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, maxHealth: int, coolDown: float,
                 rotationSpeed: float, angle: float, MissileGenerator,aimTime: float,Level, kwargs):
        super().__init__(posX, posY, sizeX, sizeY, maxHealth, coolDown, rotationSpeed, angle)
        self.aimTime=aimTime
        self.aimingTime=0
        self.ClosePointSys=ClosestPointCross()
        self.Level=Level
        self.isOnLineV=False
        self.missilePlacer = MissileGenerator(**kwargs)
        #self.visual =

    def isOnLine(self):
        self.ClosePointSys.reset()
        center = (self.posX + self.sizeX // 2, self.posY + self.sizeY // 2)
        front = self.getPoint()
        self.ClosePointSys.setLine(*twoPointToLine(center, front), center, front)
        self.ClosePointSys.analyzeGroupShapes(self.Level.turrets)
        self.ClosePointSys.analyzeGroupShapes(self.Level.obstacles)
        x, y = self.ClosePointSys.getPoint()
        self.ClosePointSys.analyzeShape(self.Level.player.getPoints())
        x2, y2 = self.ClosePointSys.getPoint()
        self.isOnLineV=x!=x2 or y!=y2

    def correctAimingTime(self,deltaTime):
        if self.isOnLineV:
            self.aimingTime+=deltaTime
        else:
            self.aimingTime=0

    def shoot(self,posX:float,posY:float) -> None:
        if self.currentCoolDown == 0 and self.canShoot(posX,posY):
            self.aimingTime = 0
            self.currentCoolDown = self.coolDown
            self.missilePlacer.damage(self.Level.player)
        return None

    def canShoot(self, posX: float, posY: float):
        #print(self.aimTime,self.aimingTime,self.isOnLineV,self.angle)
        return self.aimTime<=self.aimingTime and self.isOnLineV

    def nextCycle(self, deltaTime: float, posX: float, posY: float) -> None:
        super().nextCycle(deltaTime,posX,posY)
        #print(self.angle)
        self.isOnLine()
        self.correctAimingTime(deltaTime)

