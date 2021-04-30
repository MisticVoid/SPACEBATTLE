from AbstractTurretVisual import AbstractTurretVisual
from pygame import Color,draw,Rect,Surface,SRCALPHA

class LaserTurretVisual(AbstractTurretVisual):
    def __init__(self,size:int,sourceTurret):
        super().__init__(size,size,sourceTurret)
        self.recolorBase(1)
        self.cannonWidth=size*0.6
        self.cannonhigh =size*0.45
        self.canon = Surface((self.cannonWidth,self.cannonhigh),SRCALPHA)
        self.drawCanon()

    def drawCanon(self):
        self.canon.fill(Color(0,0,0,0))
        width = self.cannonWidth
        high  = self.cannonhigh
        draw.rect(self.canon,Color(0,0,0),Rect(0.3*width,0.3*high,0.5*width,0.4*high))
        draw.polygon(self.canon,Color(255,0,0),[(width,0.5*high),(0.5*width,high),(0.8*width,0.5*high),(0.5*width,0)])
        draw.polygon(self.canon,Color(255,0,0),[(0.5*width,0.5*high),(0.0*width,high),(0.3*width,0.5*high),(0.0*width,0)])




