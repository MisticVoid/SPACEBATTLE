import pygame
import MapElement


def main():
    sizeX = 1920
    sizeY = 1080

    pygame.init()
    screen = pygame.display.set_mode((sizeX, sizeY))
    screen.fill(pygame.Color(255,0,0))

    pic = MapElement.MapElement(10,20,200,300,"space1.jpeg")
    pic2 = MapElement.MapElement(500,500,100,100,"space1.jpeg",((0,0),(100,10),(90,80),(0,50)))
    screen.blit(pic.draw(),(pic.posX,pic.posY))
    screen.blit(pic2.draw(), (pic2.posX, pic2.posY))
    pygame.display.flip()
    while True:
        pass






if __name__=="__main__":
    main()


