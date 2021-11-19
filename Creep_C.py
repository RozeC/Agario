from pygame.math import Vector2
import core
import pygame
import random
import math


class Creep_C:
    def __init__(self):

        self.pos_C = Vector2(random.randint(0, 600), random.randint(0, 400))
        self.couleur_C = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon_C = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_C, self.pos_C, self.rayon_C)