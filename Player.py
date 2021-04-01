from typing import *
from math import sin,cos,sqrt,atan,pi
from PlayerVisual import *
class Player:
    def __init__(self,posX: Union[int,float],posY: Union[int,float],speed: Union[int,float],maxSpeedForward: Union[int,float],
                 maxSpeedBackward: Union[int,float],acceleration: Union[int,float],angle: Union[int,float],
                 rotationSpeed: Union[int,float],sizeX: int,sizeY: int,maxHealth: int,damage: int,shotDelayTime: float):
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.maxSpeedForward = maxSpeedForward
        self.maxSpeedBackward = -maxSpeedBackward
        self.acceleration = acceleration
        self.angle = angle
        self.rotationSpeed = rotationSpeed
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.diagonal: float = sqrt(sizeX**2+sizeY**2)/2
        self.angleShift: float = atan(sizeX/sizeY)
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.damage = damage
        self.shootDelayTime = shotDelayTime
        self.shootDelay = 0
        self.visual = PlayerVisual(sizeX,sizeY,Color(0,0,255),Color(0,255,0),self)

    def rotateRight(self,deltaTime: float) -> float:
        self.angle -= self.rotationSpeed*deltaTime
        self.angle %= 2*pi
        return self.angle

    def rotateLeft(self,deltaTime: float) -> float:
        self.angle += self.rotationSpeed*deltaTime
        self.angle %= 2*pi
        return self.angle

    def accelerate(self,deltaTime: float) -> None:
        self.speed += self.acceleration * deltaTime
        self.speed = min(self.speed,self.maxSpeedForward)

    def reduceSpeed(self,deltaTime: float) -> None:
        self.speed -= self.acceleration * deltaTime
        self.speed = max(self.speed, self.maxSpeedBackward)

    def move(self,deltaTime: float) -> Tuple[float,float]:
        self.posX += self.speed * deltaTime * cos(self.angle)
        self.posY += self.speed * deltaTime * sin(-self.angle)
        return self.posX,self.posY

    def hit(self,damage) -> float:
        self.health = max(self.health-damage,0)
        self.visual.recolorEdge(self.health/self.maxHealth)
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

    def nextCycle(self,deltaTime) -> Tuple[float,float]:
        self.shootDelay-=deltaTime
        self.shootDelay = max(0,self.shootDelay)
        return self.move(deltaTime)

    def shoot(self) -> bool:
        if self.shootDelay>0:
            return False
        else:
            self.shootDelay=self.shootDelayTime
            return True

    def draw(self) -> Surface:
        return self.visual.draw()









