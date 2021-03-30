from typing import *
from math import sin,cos,sqrt,atan,pi
class Player:
    def __init__(self,posX: Union[int,float],posY: Union[int,float],speed: Union[int,float],
                 acceleration: Union[int,float],angle: Union[int,float],rotationSpeed: Union[int,float],sizeX: int,
                 sizeY: int,health: int,damage: int) -> None:
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.acceleration = acceleration
        self.angle = angle
        self.rotationSpeed = rotationSpeed
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.diagonal: float = sqrt(sizeX**2+sizeY**2)/2
        self.angleShift: float = atan(sizeX/sizeY)
        self.health = health
        self.damage = damage

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

    def hit(self,damage) -> float:
        self.health = max(self.health-damage,0)
        return self.health

    def getPoints(self) -> Tuple[Tuple[float,float],Tuple[float,float],Tuple[float,float]]:
        return (
            (self.posX+self.diagonal*sin(self.angle+self.angleShift+pi/2),
                self.posY+self.diagonal*cos(self.angle+self.angleShift+pi/2)),
            (self.posX + self.diagonal * sin(self.angle - self.angleShift + 3 * pi / 2),
                self.posY + self.diagonal * cos(self.angle - self.angleShift + 3 * pi / 2)),
            (self.posX + self.sizeX/2 * sin(self.angle),
                self.posY + self.sizeX/2 * cos(self.angle))
            )









