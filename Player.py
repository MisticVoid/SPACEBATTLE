from typing import *
from math import sin,cos
class Player:
    def __init__(self,posX: Union[int,float],posY: Union[int,float],speed: Union[int,float],acceleration: Union[int,float],angle: Union[int,float],rotationSpeed: Union[int,float]) -> None:
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.acceleration = acceleration
        self.angle = angle
        self.rotationSpeed = rotationSpeed

    def rotateRight(self,deltaTime: float) -> float:
        self.angle -= self.rotationSpeed*deltaTime
        return self.angle

    def rotateLeft(self,deltaTime: float) -> float:
        self.angle += self.rotationSpeed*deltaTime
        return self.angle

    def accelerate(self,deltaTime: float) -> None:
        self.speed += self.acceleration * deltaTime

    def reduceSpeed(self,deltaTime: float) -> None:
        self.speed -= self.acceleration * deltaTime

    def move(self,deltaTime: float) -> Tuple[float,float]:
        self.posX += self.speed * deltaTime * sin(self.angle)
        self.posY += self.speed * deltaTime * cos(self.angle)
        return self.posX,self.posY







