from StandardTurret import StandardTurret
from RocketTurret import RocketTurret
from LaserTurret import LaserTurret
from Obstacle import Obstacle
from MapElement import MapElement

class MapLoader:
    def __init__(self,level,number):
        self.level=level
        self.num=number

    def load(self):
        self.level.mapEl=set()
        self.level.turrets=set()
        self.level.obstacles=set()

        data=True

        f = open("Levels/level"+str(self.num)+".txt")

        while data:
            line = f.readline()[:-1]
            if line=="end":
                data=False
            elif line=="Turret":
                self.level.turrets.add(self.loadTurret(f))
            elif line=="Obstacle":
                self.level.obstacles.add(self.loadObstacle(f))
            elif line=="Element":
                self.level.mapEl.add(self.loadElement(f))
            else:
                print("unknown marker")
                data=False

        f.close()

    def loadTurret(self,f):
        line = f.readline()[:-1]
        V=[0]*9
        for i in range(6):
            V[i] = int(f.readline()[:-1])

        for i in range(6,8):
            V[i] = float(f.readline()[:-1])

        if line=="L":
            V[8] = float(f.readline()[:-1])
        else:
            V[8] = int(f.readline()[:-1])

        if line == "S":
            return StandardTurret(*tuple(V))
        elif line == "R":
            return RocketTurret(*tuple(V),self.level.player)
        elif line == "L":
            return LaserTurret(*tuple(V),self.level)
        else:
            print("unknown marker in Turret")  # throw error or something

    def loadObstacle(self,f):
        C=[0]*4
        for i in range(4):
            C[i]=int(f.readline()[:-1])

        vis = f.readline()[:-1] == 'T'
        N= int(f.readline()[:-1])
        if N==0:
            return Obstacle(*tuple(C),visible=vis)
        P=[0]*N
        for i in range(N):
            x=int(f.readline()[:-1])
            y = int(f.readline()[:-1])
            P[i]=(x,y)
        return Obstacle(*tuple(C),points=tuple(P),visible=vis,color=(50,50,50))

    def loadElement(self,f):
        C = [0] * 4
        for i in range(4):
            C[i] = int(f.readline()[:-1])
        name=f.readline()[:-1]
        N = int(f.readline()[:-1])
        if N==0:
            return MapElement(*tuple(C),name)
        P=[0]*N
        for i in range(N):
            x=int(f.readline()[:-1])
            y = int(f.readline()[:-1])
            P[i]=(x,y)
        return MapElement(*tuple(C), name,tuple(P))


