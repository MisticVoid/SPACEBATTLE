from GameEngine import *
from math import pi


def main():
    #def __init__(self, posX: Union[int, float], posY: Union[int, float], speed: Union[int, float],
    #             maxSpeedForward: Union[int, float],
    #             maxSpeedBackward: Union[int, float], acceleration: Union[int, float], angle: Union[int, float],
    #             rotationSpeed: Union[int, float], sizeX: int, sizeY: int, maxHealth: int, damage: int,
    #             shotDelayTime: float):

    playerProperties = [0, 0, 0, 500, 250, 100, 0, 2*pi, 75, 50, 10, 10, 10]

    engine = GameEngine(playerProperties)

    engine.run()


def sum(T):
    value = 0
    for x in T:
        value += x
    return 1 / ((value / 10) / 10 ** 9)


if __name__ == "__main__":
    main()