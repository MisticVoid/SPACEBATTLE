from typing import *
from pygame import *
from Player import *
from math import pi

class PlayerVisual:
    def __init__(self,sizeX: int,sizeY: int, bodyColor: Color,EdgeColor: Color,sourcePlayer: Player,edgeWidth: int =5):
        self.sizeX= sizeX
        self.sizeY = sizeY
        self.surface = Surface((sizeX,sizeY),SRCALPHA)
        self.bodyColor = bodyColor
        self.EdgeColor = EdgeColor
        self.sourcePlayer = sourcePlayer
        self.edgeWidth = edgeWidth

    def draw(self) -> Surface:
        self.surface.fill((0,0,0,0))
        draw.polygon(self.surface,self.bodyColor,[(0,0),(0,self.sizeY),(self.sizeX,self.sizeY//2)])
        draw.polygon(self.surface, self.EdgeColor, [(0, 0), (0, self.sizeY), (self.sizeX, self.sizeY // 2)], self.edgeWidth)
        return self.rotate(self.sourcePlayer.angle)

    def recolorEdge(self,value: float) -> Color:
        self.EdgeColor = Color(int(min(255*(2-2*value),255)),int(min(255*value*2,255)),0)
        return self.EdgeColor

    def rotate(self,angle: float) -> Surface:
        return transform.rotate(self.surface,angle*180/pi)








