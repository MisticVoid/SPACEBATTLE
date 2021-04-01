import abc
from typing import *
from math import sin,cos

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

    def collision(self):
        pass



