import abc
from typing import *
from math import pi

class AbstractTurret(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int,maxHealth: int, coolDown: float,
                 rotationSpeed: float,angle: float):
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

    def shoot(self):
        pass

    def getDamage(self, damage: float):
        pass

    def canShoot(self):
        pass

    def nextCycle(self,deltaTime: float):
        pass
















