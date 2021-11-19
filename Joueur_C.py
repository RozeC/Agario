import self
from pygame.math import Vector2
import core
import pygame
import random
import math


class Joueur_C:

    def __init__(self):

        self.centredecercle = pygame.Vector2(200, 200)
        self.centredecercle = pygame.Vector2(self.centredecercle.x, self.centredecercle.y)
        self.rayonducercle = 10
        self.couleurducercle = (255, 255, 255)
        self.vitesse = pygame.Vector2(0, 0)
        self.gravity_x = 0
        self.gravity_y = 0
        self.centredecercle = pygame.Vector2(self.centredecercle.x + self.gravity_x,
                                            self.centredecercle.y + self.gravity_y)

        pygame.draw.circle(core.screen, self.couleurducercle, self.centredecercle,  self.rayonducercle)



def move (self):

    # Hors limite Y
    if self.centredecercle.y > core.WINDOW_SIZE[1] - self.rayonducercle:
        self.gravity_y = -5
        self.vitesse = self.vitesse - self.vitesse
        self.couleurducercle, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if self.centredecercle.y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
        self.gravity_y = 5
        self.vitesse = self.vitesse - self.vitesse
        self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Hors limite X
    if self.centredecercle.x > core.WINDOW_SIZE[0] - self.rayonducercle:
        self.gravity_x = -5
        self.vitesse = self.vitesse - self.vitesse
        self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if self.centredecercle.x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
        self.gravity_x = 5
        self.vitesse = self.vitesse - self.vitesse
        self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Reset
    if core.getKeyPressList(pygame.K_r):
        self.centredecercle = pygame.Vector2(200, 200)
        self.gravity_x = 0
        self.gravity_y = 0
        self.vitesse = Vector2(0, 0)
        print("reset")

    def move(self, jsp):

        # Up
        if core.getKeyPressList(pygame.K_z):
            self.gravity_y = -5
            print("up")
        # Down
        if core.getKeyPressList(pygame.K_s):
            self.gravity_y = 5
            print("down")

        # Right
        if core.getKeyPressList(pygame.K_d):
            core.memory("gravity_x", 5)
            print("right")

        # Left
        if core.getKeyPressList(pygame.K_q):
            core.memory("gravity_x", -5)
            print("left")

        # Souris
        if core.getMouseLeftClick() is not None:
            self.PS = pygame.Vector2(0, 0)
            self.k = 0.01
            self.l0 = 1
            self.u = 0
            self.pos_souris = pygame.Vector2(0, 0)

            # Pos souris
            self.pos_souris = pygame.Vector2(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1])

            # Vecteur pos_souris - pos_cercle
            self.PS = pygame.Vector2(self.pos_souris.x - self.centredecercle.x, self.pos_souris.y - self.centredecercle.y)

            # Norme vecteur PS
            self.l = core.memory("PS").length()

            # Longueur vecteur PS
            self.u = core.memory("PS").normalize()

            # Calcul Force finale
            self.Fr = self.k * abs(self.l - self.l0) * self.u
            print(self.Fr)

            # Vitesse = vitesse + force
            self.vitesse = self.vitesse + self.Fr

            # pos_cercle = pos_cercle + vitesse
        self.centredecercle = self.centredecercle + self.vitesse

