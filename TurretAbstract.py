import abc
from typing import *
from math import pi
from MisselAbstract import AbstractMissile
from Geometry import twoPointToLine,distPointFromLine,rotatePoint,orient

class AbstractTurret(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int,maxHealth: int, coolDown: float,
                 rotationSpeed: float,angle: float):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.coolDown = coolDown
        self.currentCoolDown = 0
        self.rotationSpeed = rotationSpeed
        self.angle = angle
        self.disLim = 10
        self.visual = None

    def correctCoolDown(self,deltaTime: float) -> None:
        self.currentCoolDown -= deltaTime
        self.currentCoolDown = max(0, self.currentCoolDown)

    def rotateRight(self,deltaTime: float) -> None:
        self.angle -= self.rotationSpeed*deltaTime
        self.angle %= 2*pi

    def rotateLeft(self,deltaTime: float) -> None:
        self.angle += self.rotationSpeed*deltaTime
        self.angle %= 2*pi

    def getDamage(self, damage: float) -> float:
        self.health = max(self.health - damage, 0)
        self.visual.recolorBase(self.health / self.maxHealth)
        return self.health

    def shoot(self,posX:float,posY:float) -> Union[AbstractMissile, None]:
        if self.currentCoolDown > 0 or not self.canShoot(posX,posY):
            return None
        else:
            self.currentCoolDown = self.coolDown
            point = self.getPoint()
            return self.missilePlacer.placeMissile((self.posX+self.sizeX // 2, self.posY+self.sizeY // 2), point,
                                                   self.sizeX*0.45, self.angle)

    def canShoot(self, posX: float, posY: float):
        p2 = self.getPoint()
        rotatedRight = rotatePoint(0,10,self.angle)
        return distPointFromLine(*twoPointToLine((self.posX + self.sizeX // 2, self.posY + self.sizeY // 2), p2), posX,
                                 posY) < self.disLim and orient((self.posX,self.posY),(self.posX+rotatedRight[0],self.posY+rotatedRight[1]),(posX,posY))==-1

    def nextCycle(self, deltaTime: float, posX: float, posY: float) -> None:
        self.correctCoolDown(deltaTime)
        p2 = self.getPoint()
        center = (self.posX + self.sizeX // 2, self.posY + self.sizeY // 2)
        o = orient(center, p2, (posX, posY))
        if o == -1:
            self.rotateLeft(deltaTime)
        elif o == 1:
            self.rotateRight(deltaTime)

    def getPoint(self) -> tuple[float, float]:
        p = rotatePoint(10, 0, self.angle)
        return p[0] + self.posX + self.sizeX // 2, p[1] + self.posY + self.sizeY // 2

    def getPoints(self) -> List[Tuple[float, float]]:
        return [(self.posX, self.posY), (self.posX, self.posY + self.sizeY), (self.posX + self.sizeX, self.posY + self.sizeY), (self.posX + self.sizeX, self.posY)]

    def draw(self):
        return self.visual.draw()
















