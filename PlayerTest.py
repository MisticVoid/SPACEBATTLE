import pygame
import time
import math
import PlayerVisual

sizeX = 1920
sizeY =1080

class playerMock:
    def __init__(self):
        self.angle = 0

def main():
    p=playerMock()
    playerView = PlayerVisual.PlayerVisual(100,50,pygame.Color(0,0,120),pygame.Color(0,255,0),p)
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
        screen.blit(background,(0,0))
        #p.angle = a/10 #uncomment to rotate
        #print(playerView.recolorEdge((a/300)%1),((a/300)%1)) #uncomment to change color
        #rotation require correct of position
        screen.blit(playerView.draw(), (sizeX//2, sizeY//2))
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




