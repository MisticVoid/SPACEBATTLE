from GameEngine import *
from math import pi
from Menu import *


def main():
    menu = Menu()
    menu.runMenu()


def sum(T):
    value = 0
    for x in T:
        value += x
    return 1 / ((value / 10) / 10 ** 9)


if __name__ == "__main__":
     main()
