from MisselAbstract import AbstractMissile
from Player import Player
from TurretAbstract import AbstractTurret
from Obstacle import Obstacle
from Geometry import *
from math import sin, cos
from Sectors import Sectors



def solveCollisions( player: Player, obstacles: list[Obstacle], turrets: list[AbstractTurret], playerMissiles: list[AbstractMissile], missiles: list[AbstractMissile], sectors: Sectors, deltaTime):

    def Player_Obstacle(player, obstacle):
        if polygonsCollide(player.getPoints(), obstacle.getPoints() )[0]:
            player.angle = player.prevAngle
        flag, point, polygon = polygonsCollide( player.getPoints(), obstacle.getPoints() )
        if flag:
            minDist = distPointFromLine(*(twoPointToLine(polygon[-1], polygon[0])), point[0], point[1] )
            p1, p2 = polygon[-1], polygon[0]
            for i in range(1, len(polygon)):
                d = dist(polygon[i-1], polygon[i], point)
                if d < minDist:
                    minDist, p1, p2 = d, polygon[i-1], polygon[i]

            """ [a, b] _|_ [b, -a] """
            vec = ( (p1[1]-p2[1]), -(p1[0]-p2[0]) )
            vec_len = (minDist+3) / sqrt(vec[0]**2 + vec[1]**2)

            """ different case if obstacle point is inside player """
            if polygon == player.getPoints():
                vec_len*=-1

            player.posX += vec_len * vec[0]
            player.posY += vec_len * vec[1]

            player.speed *= 0.95
        Player_Obstacle2(player, obstacle)

    """ same as player-obstacle collision, but maybe different damage or sth """
    def Player_Turret(player, turret):
        if polygonsCollide(player.getPoints(), turret.getPoints())[0]:
            player.angle = player.prevAngle
        flag, point, polygon = polygonsCollide( player.getPoints(), turret.getPoints() )
        if flag:
            minDist = distPointFromLine(*(twoPointToLine(polygon[-1], polygon[0])), point[0], point[1] )
            p1, p2 = polygon[-1], polygon[0]
            for i in range(1, len(polygon)):
                d = dist(polygon[i-1], polygon[i], point)
                if d < minDist:
                    minDist, p1, p2 = d, polygon[i-1], polygon[i]

            vec = ( (p1[1]-p2[1]), -(p1[0]-p2[0]) )
            vec_len = (minDist+3) / sqrt(vec[0]**2 + vec[1]**2)

            if polygon == player.getPoints():
                vec_len*=-1

            player.posX += vec_len * vec[0]
            player.posY += vec_len * vec[1]

            player.speed *= 0.95
        Player_Turret2(player, turret)

    def Player_Obstacle2(player, obstacle):
        if polygonsCollide2(player.getPoints(), obstacle.getPoints()):
            player.angle = player.prevAngle

        if polygonsCollide2(player.getPoints(), obstacle.getPoints()):
            if player.speed == 0:
                player.speed = 0.01
            for _ in range(100):
                player.posX -= abs(player.speed) / player.speed * 2 * cos(player.angle)
                player.posY -= abs(player.speed) / player.speed * 2 * sin(-player.angle)
                if not polygonsCollide(player.getPoints(), obstacle.getPoints())[0]:
                    break
            player.posX -= abs(player.speed) / player.speed * 3 * cos(player.angle)
            player.posY -= abs(player.speed) / player.speed * 3 * sin(-player.angle)

    
    def Player_Turret2(player, turret):
        if polygonsCollide2(player.getPoints(), turret.getPoints()):
            player.angle = player.prevAngle

        if polygonsCollide2(player.getPoints(), turret.getPoints()):
            if player.speed == 0:
                player.speed = 0.01
            for _ in range(100):
                player.posX -= abs(player.speed) / player.speed * 2 * cos(player.angle)
                player.posY -= abs(player.speed) / player.speed * 2 * sin(-player.angle)
                if not polygonsCollide(player.getPoints(), turret.getPoints())[0]:
                    break
            player.posX -= abs(player.speed)/player.speed * 3 * cos(player.angle)
            player.posY -= abs(player.speed)/player.speed * 3 * sin(-player.angle)


    def Player_Missile(player, missile):
        if inPolygon((missile.posX, missile.posY), player.getPoints()):
            #print("Collision of player and missile")
            player.hit(missile.damage)
            return missile

    def Turret_Missile(turret, missile):
        if inPolygon((missile.posX, missile.posY), turret.getPoints()):
            #print("Collision of turret and missile")
            turret.getDamage(missile.damage)
            return missile

    def Obstacle_Missile(obstacle, missile):
        if inPolygon((missile.posX, missile.posY), obstacle.getPoints()):
            #print("Collision of missile and obstacle")
            return missile

    """
    for turret in turrets:
        Player_Turret(player, turret)

    for obstacle in obstacles:
        Player_Obstacle(player, obstacle)
    """

    for turret in sectors.getTurrets(player.getPoints()):
        Player_Turret(player, turret)

    for obstacle in sectors.getObstacles(player.getPoints()):
        Player_Obstacle(player, obstacle)

    missilesToRemove = set()
    #compare = set()


    for missile in playerMissiles:
        missilesToRemove.add(None)
        #for turret in turrets:
        #    compare.add(Turret_Missile(turret, missile))
        #for obstacle in obstacles:
        #    compare.add(Obstacle_Missile(obstacle, missile))
        for turret in sectors.getTurrets([(missile.posX, missile.posY)]):
            missilesToRemove.add(Turret_Missile(turret, missile))

        for obstacle in sectors.getObstacles([(missile.posX, missile.posY)]):
            missilesToRemove.add(Obstacle_Missile(obstacle, missile))

    #if len(missilesToRemove) != len(compare) or len(missilesToRemove) != len(missilesToRemove & compare):
    #    print("difference for player missiles")
    playerMissiles -= missilesToRemove

    missilesToRemove = set()


    for missile in missiles:
        missilesToRemove.add(Player_Missile(player, missile))

        for obstacle in sectors.getObstacles([(missile.posX, missile.posY)]):
            missilesToRemove.add(Obstacle_Missile(obstacle, missile))

        #for obstacle in obstacles:
        #    compare.add(Obstacle_Missile(obstacle, missile))

    missiles -= missilesToRemove
