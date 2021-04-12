import pygame
from Player import *
from GameEngine import *
from MapElement import *
import Geometry


class Level:
    def __init__(self, playerProperties, sizeX: int, sizeY: int, gameEngine):
        self.screenSizeX = sizeX
        self.screenSizeY = sizeY

        self.screen = pygame.display.set_mode((sizeX, sizeY))
        self.background = pygame.Surface((sizeX, sizeY))
        self.engine = gameEngine

        p = playerProperties
        self.player = Player(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])

        self.mapEl = []

        # letter replace next lines with map loader
        el=MapElement(0, 0, 1000, 1000, "space1.jpeg", ((0, 0), (1000, 0), (1000, 1000), (0, 500)))
        self.addMapEl(el)
        el = MapElement(1000, 1000, 100, 100, "space1.jpeg")  # if el is a rect it not need cords
        self.addMapEl(el)
        el = MapElement(1000, 450, 1000, 100, "space1.jpeg")
        self.addMapEl(el)

    def addMapEl(self,element):
        self.mapEl.append(element)

    def update(self, deltaTime):
        self.player.nextCycle(deltaTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()

        keys = pygame.key.get_pressed()

        #print(self.player.posX, self.player.posY)

        if keys[K_UP]:
            self.player.accelerate(deltaTime)
        if keys[K_DOWN]:
            self.player.reduceSpeed(deltaTime)
        if keys[K_LEFT]:
            self.player.rotateLeft(deltaTime)
        if keys[K_RIGHT]:
            self.player.rotateRight(deltaTime)


    def display(self):
        s = self.player.draw()
        x, y = int(self.player.posX), int(self.player.posY)
        self.screen.fill(pygame.Color(0, 0, 0))

        for element in self.mapEl:
            self.blend(self.screen,element,x,y)
        #self.screen.blit(self.mapEl.draw(), (self.screenSizeX//2-int(self.mapEl.posX)-x, self.screenSizeY//2-int(self.mapEl.posY)-y))

        pygame.draw.circle(s, (255, 0, 0), (s.get_rect().width // 2, s.get_rect().height // 2), 1)
        self.screen.blit(s, (self.screenSizeX//2 - s.get_rect().width//2, self.screenSizeY//2 - s.get_rect().height//2))
        #print(in_MapElement(self.mapEl, self.player))    # for testing if player in mapElement
        pygame.display.flip()

    def blend(self,screen,element,playerPosX,playerPosY):
        xl = element.posX - playerPosX+self.screenSizeX//2
        xr = xl + element.sizeX
        yu = element.posY - playerPosY+self.screenSizeY//2
        yd = yu + element.sizeY
        #print(xl, xr, yu, yd)
        if (0<=xl<=self.screenSizeX or 0<=xr<=self.screenSizeX) and (0<=yu<=self.screenSizeY or 0<=yd<=self.screenSizeY):
            xlr = max(0, xl)  # not sure how pyGame represent coordinates so check if min and max are correct
            xrr = min(xr, self.screenSizeX)
            yur = max(yu, 0)
            ydr = min(yd, self.screenSizeY)
            R = Rect(max(0,-xl), max(0,-yu), xrr - xlr, ydr -yur)
            screen.blit(element.draw(), (xlr, yur), R)

# def in_MapElement(mapElement: MapElement, player: Player):
#     x, y = player.posX, player.posY
#     if not (player.posX > mapElement.posX and player.posX < mapElement.posX+mapElement.sizeX and player.posY > mapElement.posY and player.posY < mapElement.posY + mapElement.sizeY):
#         return False
#     if mapElement.points == None:
#         return True
#     else:
#         return Geometry.inPolygon((player.posX, player.posY), mapElement.points)
