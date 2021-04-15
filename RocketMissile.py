from MisselAbstract import AbstractMissile
from RocketMissileVisual import RocketMissileVisual
from Geometry import orient,rotatePoint
from math import pi
from pygame import Color

class RocketMissile(AbstractMissile):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int, angle: float, speed: float,
                 rotationSpeed: float,colorC:Color,target):
        super().__init__(posX, posY, sizeX, sizeY, damage, angle, speed)
        self.target=target
        self.pointsOrigin=[(self.sizeX/2,0),(self.sizeX/4,-self.sizeY/2),(self.sizeX/2,-self.sizeY/2),
                           (self.sizeX/4,self.sizeY/2),(self.sizeX/4,self.sizeY/2)]
        self.rotationSpeed=rotationSpeed
        self.visual=RocketMissileVisual(self.sizeX,self.sizeY,colorC,self)

    def nextCycle(self,deltaTime: float) -> None:
        p2 = self.getPoint()
        center = (self.posX, self.posY)
        o = orient(center, p2, (self.target.posX, self.target.posY))
        if o == -1:
            self.rotateLeft(deltaTime)
        elif o == 1:
            self.rotateRight(deltaTime)
        self.move(deltaTime)

    def rotateRight(self, deltaTime: float) -> None:
        self.angle -= self.rotationSpeed * deltaTime
        self.angle %= 2 * pi

    def rotateLeft(self, deltaTime: float) -> None:
        self.angle += self.rotationSpeed * deltaTime
        self.angle %= 2 * pi

    def collision(self):
        pass

    def getPoint(self)->tuple[float,float]:
        x,y=rotatePoint(self.pointsOrigin[0][0],self.pointsOrigin[0][1],self.angle)
        return x+self.posX,y+self.posY

    def getPoints(self)->tuple[tuple[float,float]:5]:
        """return point of rocket, include current rotation"""
        return ((x+self.posX,y+self.posY) for p in self.pointsOrigin for x,y in rotatePoint(p[0],p[1],self.angle))






