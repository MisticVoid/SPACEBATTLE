import abc
from typing import *
from math import pi
from MisselPlacer import MisselPlacer
from MisselAbstract import AbstractMissile
from math import sqrt

class AbstractTurret(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int,maxHealth: int, coolDown: float,
                 rotationSpeed: float,angle: float,MissileGenerator,kwargs):
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
        self.missilePlacer = MisselPlacer(MissileGenerator,kwargs)
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
        self.visual.recolorEdge(self.health / self.maxHealth)
        return self.health

    def shoot(self,posX:float,posY:float) -> Union[AbstractMissile, None]:
        if self.currentCoolDown > 0 or not self.canShoot(posX,posY):
            return None
        else:
            self.currentCoolDown = self.coolDown
            point = self.getPoint()
            return self.missilePlacer.placeMissile((self.posX+self.sizeX // 2, self.posY+self.sizeY // 2), point,
                                                   self.sizeX*0.45, self.angle)

    def canShoot(self,posX:float,posY:float)->bool:
        pass

    def nextCycle(self,deltaTime: float,posX:float,posY:float)->None:  # position of player required
        pass

    def getPoint(self)->tuple[float,float]:
        pass

    def draw(self):
        return self.visual.draw()
















