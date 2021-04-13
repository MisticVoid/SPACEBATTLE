import abc
from typing import *
from math import pi

class AbstractTurret(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int,maxHealth: int, coolDown: float,
                 rotationSpeed: float,angle: float,MissileGenerator):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.damage = damage
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.coolDown = coolDown
        self.currentCoolDown = 0
        self.rotationSpeed = rotationSpeed
        self.angle = angle
        self.MissileGenerator = MissileGenerator
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

    def shoot(self,*args):
        return self.MissileGenerator(*args)

    def canShoot(self):
        pass

    def nextCycle(self,deltaTime: float):
        pass
















