from Player import *
from StandardTurret import StandardTurret
from RocketTurret import RocketTurret
from Obstacle import Obstacle

from LaserTurret import LaserTurret


SECTOR_SIZE = 500

def scale(x):
    return int(x/SECTOR_SIZE)

class Sectors:
    def __init__(self, turrets, obstacles):
        self.turretsMap = {}
        self.obstaclesMap = {}

        for turret in turrets:
            self.addTurret(turret)
        for obstacle in obstacles:
            self.addObstacle(obstacle)

    def getCoords(self, points):
        xl = xr = points[0][0]
        yd = yu = points[0][1]
        for x,y in points:
            xl = min(xl, x)
            xr = max(xr, x)
            yd = max(yd, y)
            yu = min(yu, y)

        return [(x, y) for x in range(scale(xl), scale(xr) + 1) for y in range(scale(yu), scale(yd) + 1)]



    def addTurret(self, el):
        points = el.getPoints()
        coords = self.getCoords(points)
        for pos in coords:
            if pos in self.turretsMap:
                self.turretsMap[pos].add(el)
            else:
                self.turretsMap[pos] = set()
                self.turretsMap[pos].add(el)

    def addObstacle(self, el):
        points = el.getPoints()
        coords = self.getCoords(points)
        for pos in coords:
            if pos in self.obstaclesMap:
                self.obstaclesMap[pos].add(el)
            else:
                self.obstaclesMap[pos] = set()
                self.obstaclesMap[pos].add(el)

    def removeTurret(self, el):
        points = el.getPoints()
        coords = self.getCoords(points)
        for pos in coords:
            self.turretsMap[pos].remove(el)
            if len(self.turretsMap[pos])==0:
                self.turretsMap.pop(pos)

    def removeTurrets(self, turrets):
        for el in turrets:
            self.removeTurret(el)

    def getTurrets(self, points):
        coords = self.getCoords(points)
        total = set()
        for pos in coords:
            if pos in self.turretsMap:
                total = total | self.turretsMap[pos]
        return total

    def getObstacles(self, points):
        coords = self.getCoords(points)
        total = set()
        for pos in coords:
            if pos in self.obstaclesMap:
                total = total | self.obstaclesMap[pos]
        return total



if __name__ == "__main__":
    turrets = []
    obstacles = []
    T = StandardTurret(-1, -1, 75, 20, 100, 2, pi / 2, 0, 1000)
    turrets.append(T)
    for i in range(5, 20, 5):
        turrets.append(StandardTurret(i*200+500, 500, 75, 20, 100, 2, pi / 2, 0, 1000))
        turrets.append(StandardTurret(i*200+500, 700, 75, 100, 100, 5, pi / 2, 0, 600))
        obstacles.append(Obstacle(200 * i - 100, -100, 1200, 100, visible=False))
        obstacles.append(Obstacle(200 * i - 100, 1000, 1200, 100, visible=False))


    sectors = Sectors(turrets, obstacles)

    print(sectors.turretsMap)
    print()
    sectors.removeTurret(T)
    print(sectors.turretsMap)
    print()
    print(sectors.obstaclesMap)





