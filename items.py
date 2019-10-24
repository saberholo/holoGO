import pygame


class StandardBullet:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((100, 100))
        self.obj = pygame.draw.circle(self.surface, [255, 255, 255], [50, 50], 50)

