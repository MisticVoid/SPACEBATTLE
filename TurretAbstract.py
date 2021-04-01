import abc
from typing import *

class AbstractTurret(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int,maxHealth: int, coolDown: float, rotationSpeed: float):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.damage = damage
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.coolDown = coolDown
        self.rotationSpeed = rotationSpeed
        self.visual = None

    def shoot(self):
        pass

    def rotateLeft(self,deltaTime: float):
        pass

    def rotateRight(self,deltaTime: float):
        pass

    def getCrossPoint(self):  # where to aim
        pass

    def getDamage(self, damage: float):
        pass

    def canShoot(self):
        pass
















