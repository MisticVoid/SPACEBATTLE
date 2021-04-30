import Geometry as Geo

class ClosestPointCross:
    def __init__(self,x=None,y=None):
        self.closestX=x
        self.closestY=y
        self.A=0
        self.B=0
        self.C=0
        self.O=(0,0)

    def setLine(self,A,B,C,O,ON):
        self.A = A
        self.B = B
        self.C = C
        self.O=O
        self.ON=ON

    def reset(self):
        self.closestX = None
        self.closestY = None

    def analyzeSection(self,p1,p2):
        x,y=Geo.crossPoint(self.A,self.B,self.C,p1,p2,self.O)
        if x is not None:
            if (x-self.O[0])*(self.ON[0]-self.O[0])>=0 and (y-self.O[1])*(self.ON[1]-self.O[1])>=0:
                if abs(x-self.O[0])<abs(self.closestX-self.O[0]) or abs(y-self.O[1])<abs(self.closestY-self.O[1]):
                    self.closestX = x
                    self.closestY = y

    def analyzeShape(self,shape,ShapeType="p"):
        if ShapeType=="p":
            for i in range(len(shape)-1,-1,-1):
                self.analyzeSection(shape[i],shape[i-1])

    def analyzeGroupShapes(self,group,ShapeType="p"):
        for s in group:
            self.analyzeShape(s.getPoints(),ShapeType)

    def getPoint(self):
        return self.closestX,self.closestY




































