from pygame.math import Vector2
import core
import pygame
import random
from Creep_C import Creep_C
import Joueur_C
from Joueur_C import Joueur_C


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [600, 400]

    core.memory("creep", [])
    core.memory("J")

    for i in range(100):
        core.memory("creep").append(Creep_C())

    J.append(Joueur_C())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    for c in core.memory("creep"):
        c.draw(core.screen )

    j


core.main(setup, run)
