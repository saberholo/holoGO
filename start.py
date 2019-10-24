import pygame
import sys

from env import Env
import character
import items

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
env = Env(9.8, screen)
color = (0, 0, 0)
holo = pygame.image.load('pic/holo.jpeg')
holorect = holo.get_rect()
bullet = items.StandardBullet(screen)


speed = [1, 1]

while True:
    bullet.obj = bullet.obj.move(speed)
    if bullet.obj.left < 0 or bullet.obj.right > width:
        speed[0] = -speed[0]
    if bullet.obj.top < 0 or bullet.obj.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(bullet.surface, bullet.obj)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # holorect = holorect.move(speed)



