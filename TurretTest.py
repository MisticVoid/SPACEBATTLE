import time
import pygame
from StandardTurret import *

sizeX = 1920
sizeY =1080

def main():
    turretX= 100
    turretY =100
    playerX=200
    playerY=200
    turret = StandardTurret(turretX,turretY,5,5,5,1,1,0,1000)
    pygame.init()
    screen = pygame.display.set_mode((sizeX,sizeY))

    screen.fill(pygame.Color(0,0,0))
    pygame.draw.circle(screen, (255, 0, 0), (turretX,turretY), 1)
    pygame.draw.circle(screen, (0, 255, 0), (playerX, playerY), 1)
    x,y = turret.getCrossPoint(playerX,playerY,10,2*pi/2)
    print(x,y)
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 1)
    pygame.display.flip()
    while True:
        pass




def sum(T):
    value = 0
    for x in T:
        value+=x
    return 1/((value/10)/10**9)




if __name__ == "__main__":
    main()
