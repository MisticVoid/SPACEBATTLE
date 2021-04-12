from pygame import *
from typing import *
import os

class MapElement:
    def __init__(self,posX: int,posY: int,sizeX: int,sizeY: int,fileName: str, points: Union[Tuple,None] = None):  # if points == None then element is a rectangle, no alpha
        file = image.load(os.path.join("recourses",fileName))
        file = transform.smoothscale(file, (sizeX, sizeY))
        if points is not None:
            self.mapElement = Surface((sizeX, sizeY), SRCALPHA)
            self.mapElement.fill(Color(0,0,0,0))
            draw.polygon(self.mapElement,Color(255,255,255,255),points)
            self.mapElement.blit(file,(0,0),special_flags=BLEND_RGBA_MULT)
        else:
            self.mapElement = file
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX  # left upper corner
        self.posY = posY

    def draw(self) -> Surface:
        return self.mapElement
























