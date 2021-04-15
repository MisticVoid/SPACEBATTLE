from AbstractTurretVisual import AbstractTurretVisual
from pygame import Surface,SRCALPHA,Color,draw,Rect

class RocketTurretVisual(AbstractTurretVisual):
    def __init__(self,size:int,sourceTurret):
        super().__init__(size,size,sourceTurret)
        self.recolorBase(1)
        self.cannonWidth = size * 0.7
        self.cannonhigh = size * 0.7
        self.canon = Surface((self.cannonWidth, self.cannonhigh), SRCALPHA)
        self.drawCanon()

    def drawCanon(self):
        self.canon.fill(Color(0, 0, 0, 0))
        width = self.cannonWidth
        high = self.cannonhigh
        draw.circle(self.canon,Color(255,255,0),(width/2,high/2),high*0.35)
        draw.ellipse(self.canon, Color(255, 0, 0), Rect(0, 0.25 * high, 0.4 * width, 0.5 * high))
        draw.rect(self.canon,Color(255,0,0),Rect(0.2*width,0.25*high,0.6*width,high*0.5))
        draw.ellipse(self.canon, Color(255, 0, 0), Rect(0.6 * width, 0.25 * high, 0.4 * width, 0.5 * high))
        draw.ellipse(self.canon, Color(0, 0, 0), Rect(0.65 * width, 0.3 * high, 0.3 * width, 0.4 * high))
