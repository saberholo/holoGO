import pygame


class Bullet:
    def __init__(self, screen, character, bullet, pos):
        self.screen = screen
        # self.surface = pygame.Surface(bullet['surface'])
        self.obj = pygame.draw.circle(self.screen, bullet['color'], pos, bullet['radius'])


StandardBullet = {
    'type': 'StandardBullet',
    'radius': 20,
    'color': (255, 255, 255),
    'surface': (40, 40)
}


