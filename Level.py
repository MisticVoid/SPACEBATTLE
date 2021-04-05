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

        #self.mapEl = MapElement(0, 0, sizeX, sizeY, "space1.jpeg")
        self.mapEl = MapElement(0, 0, 1000, 1000, "space1.jpeg", ((0, 0), (1000, 100), (900, 800), (0, 500)))

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
        self.screen.fill(pygame.Color(255, 0, 0))

        self.screen.blit(self.mapEl.draw(), (self.screenSizeX//2-int(self.mapEl.posX)-x, self.screenSizeY//2-int(self.mapEl.posY)-y))

        pygame.draw.circle(s, (255, 0, 0), (s.get_rect().width // 2, s.get_rect().height // 2), 1)
        self.screen.blit(s, (self.screenSizeX//2 - s.get_rect().width//2, self.screenSizeY//2 - s.get_rect().height//2))
        print(in_MapElement(self.mapEl, self.player))    #for testing if player in map
        pygame.display.flip()

def in_MapElement(mapElement: MapElement, player: Player):
    x, y = player.posX, player.posY
    if not (player.posX > mapElement.posX and player.posX < mapElement.posX+mapElement.sizeX and player.posY > mapElement.posY and player.posY < mapElement.posY + mapElement.sizeY):
        return False
    if mapElement.points == None:
        return True
    else:
        return Geometry.inPolygon((player.posX, player.posY), mapElement.points)
