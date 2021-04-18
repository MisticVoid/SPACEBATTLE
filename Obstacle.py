from typing import *
from pygame import *
import pygame




class Obstacle:
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, color: Tuple = (0,0,0,0) , points: Union[Tuple, None] = None):  # if points == None then element is a rectangle, no alpha
        self.obstacle = Surface((sizeX, sizeY), SRCALPHA)
        if points is not None:
            self.points = [(p[0] + posX, p[1] + posY) for p in points]
            self.obstacle.fill(Color(0,0,0,0))
            draw.polygon(self.obstacle, Color(*color), points)
        else:
            self.obstacle.fill(Color(*color))
            self.points = [(posX, posY), (posX, posY + sizeY), (posX + sizeX, posY + sizeY), (posX + sizeX, posY)]
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX  # left upper corner
        self.posY = posY

    def draw(self) -> Surface:
        return self.obstacle

    def getPoints(self):
        return self.points

