import pygame


class Env:
    def __init__(self, gravitational_constance, screen):
        self.G = gravitational_constance
        self.screen = screen

    def speed_update(self):
        pass