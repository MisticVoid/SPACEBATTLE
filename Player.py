from typing import *
from math import sin,cos,pi
from MisselPlacer import MisselPlacer
from standardMissel import StandardMissile
from MisselAbstract import AbstractMissile
from Geometry import rotatePoint,orient
from PlayerVisual import PlayerVisual
from pygame import Color,Surface

class Player:
    def __init__(self,posX: Union[int,float],posY: Union[int,float],speed: Union[int,float],maxSpeedForward: Union[int,float],
                 maxSpeedBackward: Union[int,float],acceleration: Union[int,float],angle: Union[int,float],
                 rotationSpeed: Union[int,float],sizeX: int,sizeY: int,maxHealth: int,damage: int,shotDelayTime: float,
                 missileSpeed: int):
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
        self.health = maxHealth
        self.maxHealth = maxHealth
        #self.damage = damage
        self.shootDelayTime = shotDelayTime
        self.shootDelay = 0
        self.missilePlacer = MisselPlacer(StandardMissile, {"size": 5, "damage": damage, "speed": missileSpeed, "colorC": Color(0, 255, 0)})
        self.visual = PlayerVisual(sizeX,sizeY,Color(0,0,255),Color(0,255,0),self)

        self.prevAngle = angle

    def rotateRight(self,deltaTime: float) -> float:
        self.prevAngle = self.angle
        self.angle -= self.rotationSpeed*deltaTime
        self.angle %= 2*pi
        return self.angle

    def rotateLeft(self,deltaTime: float) -> float:
        self.prevAngle = self.angle
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
        p=[0,0,0]
        p[0]=rotatePoint(-self.sizeX//2,-self.sizeY//2,self.angle)
        p[1]=rotatePoint(-self.sizeX//2,self.sizeY//2,self.angle)
        p[2]=rotatePoint(self.sizeX//2,0,self.angle)
        for x in range(3):
            p[x] = (p[x][0]+self.posX,p[x][1]+self.posY)
        return p[0],p[1],p[2]

    def nextCycle(self,deltaTime) -> Tuple[float,float]:
        self.shootDelay-=deltaTime
        self.shootDelay = max(0,self.shootDelay)
        return self.move(deltaTime)

    def shoot(self) -> Union[AbstractMissile,None]:
        if self.shootDelay>0:
            return None
        else:
            self.shootDelay = self.shootDelayTime
            point = self.getPoints()
            return self.missilePlacer.placeMissile((self.posX, self.posY), point[2], self.sizeX // 2 + 5, self.angle)

    def draw(self) -> Surface:
        return self.visual.draw()

    def followMouse(self,deltaTime,mosePos):
        N = 10
        center = (0, 0)

        for _ in range(N):
            o = orient(center, rotatePoint(10, 0, self.angle), (mosePos[0], mosePos[1]), 0)
            if o == -1:
                self.rotateLeft(deltaTime/N)
            elif o == 1:
                self.rotateRight(deltaTime/N)









