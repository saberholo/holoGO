import pygame
import sys

from env import Env
import character
import items

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
env = Env(10, screen, 100)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
bullet = items.Bullet(screen, 0, items.StandardBullet, (100, 100))


speed = [10, 2]

while True:
    screen.fill(BLACK)
    clock.tick(env.fps)
    bullet.obj = bullet.obj.move(env.speed_update(speed))
    env.bound(bullet, speed, width, height)

    screen.blit(bullet.screen, bullet.obj)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            bullet = items.Bullet(screen, 0, items.StandardBullet, pos)





