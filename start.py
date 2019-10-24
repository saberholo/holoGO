import pygame
import sys

from env import Env
import character
import items

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
env = Env(9.8, screen)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
bullet = items.StandardBullet(screen)


speed = [10, 10]
fps = 100

while True:
    screen.fill(BLACK)
    clock.tick(fps)
    bullet.obj = bullet.obj.move(speed)
    if bullet.obj.left < 0 or bullet.obj.right > width:
        speed[0] = -speed[0]
    if bullet.obj.top < 0 or bullet.obj.bottom > height:
        speed[1] = -speed[1]


    screen.blit(bullet.surface, bullet.obj)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




        screen.fill(BLACK)
        pygame.draw.circle(screen, [0, 0, 0], [300, 300], 200)



