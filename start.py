import pygame
import sys

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
color = (0, 100, 100)
holo = pygame.image.load('pic/holo.jpeg')
obj = pygame.draw.circle(screen, [0, 0, 0], [100, 100], 50)
holorect = holo.get_rect()
speed = [10, 10]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        holorect = holorect.move(speed)
        if holorect.left < 0 or holorect.right > width:
            speed[0] = -speed[0]
        if holorect.top < 0 or holorect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(color)
        screen.blit(holo, holorect)

        pygame.display.flip()
