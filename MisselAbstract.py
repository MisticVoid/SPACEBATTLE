import abc
from typing import *
from math import sin,cos
from pygame import Surface

class AbstractMissile(abc.ABC):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int,angle: float,speed: float):
        self.posX = posX
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.damage = damage
        self.angle = angle
        self.speed = speed
        self.visual = None

    def move(self, deltaTime: float) -> None:
        self.posX += self.speed * deltaTime * cos(self.angle)
        self.posY += self.speed * deltaTime * sin(-self.angle)

    def nextCycle(self,deltaTime: float) -> None:
        pass

    def collision(self):
        pass

    def getPoints(self):
        return [self.posX, self.posY]

    def draw(self) -> Surface:
        return self.visual.draw()


