
from MisselAbstract import AbstractMissile
from math import sqrt


class MisselPlacer:
    def __init__(self,missileType,kwargs):
        self.missileType=missileType
        self.kwargs=kwargs

    def placeMissile(self,p1: tuple[float,float],p2: tuple[float,float],dist: float,angel: float)->AbstractMissile:
        dx=(p2[0]-p1[0])
        dy=(p2[1]-p1[1])
        d=sqrt(dx**2+dy**2)
        posX = p1[0]+dx*dist/d
        posY = p1[1] + dy * dist / d
        return self.missileType(posX,posY,angle=angel,**self.kwargs)


# use example:
# m = MisselPlacer(AbstractMissile,{"sizeX": 10,"sizeY": 5,"damage": 100,"speed": 100})
# p=m.placeMissile((0,0),(1,1),10,0)






















