import pygame
import math
from Player import *
import time

sizeX = 1920
sizeY =1080

class playerMock:
    def __init__(self):
        self.angle = 0

def main():

    player = Player(sizeX/2,sizeY/2,0,1000,100,200,0,2*pi,80,40,100,1,1)
    pygame.init()
    screen = pygame.display.set_mode((sizeX,sizeY))
    background = pygame.Surface((sizeX,sizeY))
    background.fill((0,0,0))
    pygame.draw.circle(background, (255, 255, 255), (200, 100), 75)
    screen.blit(background, (0, 0))
    a=0
    times = [0]*10
    i=0
    t = time.perf_counter_ns()
    l = 0
    while True:
        if player.posX >1200 or player.posX <800:
            player.rotateRight(times[i] / 10 ** 9)
        screen.blit(background,(0,0))
        #player.rotateRight(times[i]/10**9) #uncomment to rotate right
        #player.rotateLeft(times[i]/10**9) #uncomment to rotate left
        #player.hit(times[i]/10**8)#uncomment to change color
        player.accelerate(times[i]/10**9)
        #print(player.speed)
        player.nextCycle(times[i]/10**9)
        #print(player.posX,player.posY)
        s=player.draw()
        pygame.draw.circle(s, (255, 0, 0), (s.get_rect().width//2, s.get_rect().height//2), 1)
        screen.blit(s, (player.posX-s.get_rect().width/2, player.posY-s.get_rect().height/2))

        pygame.display.flip()
        times[i]=time.perf_counter_ns()-t
        l+=times[i]
        a=l//10**7
        t = time.perf_counter_ns()
        i+=1
        i%=10
        print("fps:",sum(times))




def sum(T):
    value = 0
    for x in T:
        value+=x
    return 1/((value/10)/10**9)





if __name__=="__main__":
    main()