from GameEngine import *
from math import pi


def main():
    #def __init__(self, posX: Union[int, float], posY: Union[int, float], speed: Union[int, float],
    #             maxSpeedForward: Union[int, float],
    #             maxSpeedBackward: Union[int, float], acceleration: Union[int, float], angle: Union[int, float],
    #             rotationSpeed: Union[int, float], sizeX: int, sizeY: int, maxHealth: int, damage: int,
    #             shotDelayTime: float):
    playerProperties = {"posX":0,"posY":0,"speed":0,"maxSpeedForward":250,"maxSpeedBackward":100,"acceleration":100,"angle":0,
    "rotationSpeed":2*pi,"sizeX":50,"sizeY":25,"maxHealth":100,"damage":10,"shotDelayTime":1,"missileSpeed":1000}

    engine = GameEngine(playerProperties)

    engine.run()


def sum(T):
    value = 0
    for x in T:
        value += x
    return 1 / ((value / 10) / 10 ** 9)


if __name__ == "__main__":
    main()
